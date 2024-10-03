/* SPDX-License-Identifier: BSD-3-Clause
 * Copyright(c) 2010-2014 Intel Corporation
 */

#include <sys/cdefs.h>
__FBSDID("$FreeBSD$");

#include <sys/param.h>
#include <sys/bio.h>
#include <sys/bus.h>
#include <sys/conf.h>
#include <sys/kernel.h>
//#include <sys/malloc.h>
#include "malloc.h"
#include <sys/module.h>
#include <sys/proc.h>
#include <sys/lock.h>
#include <sys/rwlock.h>
#include <sys/mutex.h>
#include <sys/systm.h>
#include <sys/sysctl.h>
#include <sys/vmmeter.h>
#include <sys/eventhandler.h>
#include <sys/time.h>

#include <machine/bus.h>

#include <vm/vm.h>
#include <vm/pmap.h>
#include <vm/vm_param.h>
#include <vm/vm_object.h>
#include <vm/vm_page.h>
#include <vm/vm_pager.h>
#include <vm/vm_phys.h>

// -- Debug contigous allocator header files -- 
#include <sys/cdefs.h>
// #include "opt_ddb.h"
// #include "opt_vm.h"

#include <sys/asan.h>
#include <sys/kdb.h>
#include <sys/msan.h>
#include <sys/queue.h>
#include <sys/sbuf.h>
#include <sys/smp.h>
#include <sys/vmem.h>
#ifdef EPOCH_TRACE
#include <sys/epoch.h>
#endif

#include <cheri/cheric.h>

// #include <vm/vm_domainset.h>
#include "vm_domainset.h"
#include <vm/vm_pageout.h>
#include <vm/vm_kern.h>
#include "vm_extern.h"
#include <vm/vm_map.h>
#include <vm/vm_pagequeue.h>
#include <vm/uma.h>
#include <vm/uma_int.h>
#include <vm/uma_dbg.h>

#ifdef DEBUG_MEMGUARD
#include <vm/memguard.h>
#endif
#ifdef DEBUG_REDZONE
#include <vm/redzone.h>
#endif

#if defined(INVARIANTS) && defined(__i386__)
#include <machine/cpu.h>
#endif

#include <ddb/ddb.h>

#ifdef KDTRACE_HOOKS
#include <sys/dtrace_bsd.h>

bool	__read_frequently			dtrace_malloc_enabled;
dtrace_malloc_probe_func_t __read_mostly	dtrace_malloc_probe;
#endif

#if defined(INVARIANTS) || defined(MALLOC_MAKE_FAILURES) ||		\
    defined(DEBUG_MEMGUARD) || defined(DEBUG_REDZONE)
#define	MALLOC_DEBUG	1
#endif

#if defined(KASAN) || defined(DEBUG_REDZONE)
#define	DEBUG_REDZONE_ARG_DEF	, unsigned long osize
#define	DEBUG_REDZONE_ARG	, osize
#else
#define	DEBUG_REDZONE_ARG_DEF
#define	DEBUG_REDZONE_ARG
#endif

// -----------------------------

// -------------------- Inside contig malloc 
#include <sys/domainset.h>

#include <cheri/cheric.h>

#include <vm/vm_object.h>
#include <vm/vm_radix.h>

// -------------------------------------

// #define RTE_CONTIGMEM_DEFAULT_BUF_SIZE 1073741824

// added to print uint 
// 64
// #include <inttypes.h>

struct contigmem_buffer {
	void           *addr;
	int             refcnt;
	struct mtx      mtx;
};

struct contigmem_vm_handle {
	int             buffer_index;
};

static int              contigmem_load(void);
static int              contigmem_unload(void);
static int              contigmem_physaddr(SYSCTL_HANDLER_ARGS);

static d_mmap_single_t  contigmem_mmap_single;
static d_open_t         contigmem_open;
static d_close_t        contigmem_close;

// RTE_CONTIGMEM_DEFAULT_NUM_BUFS = 3;
// RTE_CONTIGMEM_DEFAULT_BUF_SIZE = 1073741824;

static int              contigmem_num_buffers = 1;
static int64_t          contigmem_buffer_size = (512*1024*1024);
// static int64_t          contigmem_buffer_size = 1073741824;

static eventhandler_tag contigmem_eh_tag;
static struct contigmem_buffer contigmem_buffers[RTE_CONTIGMEM_MAX_NUM_BUFS];
static struct cdev     *contigmem_cdev = NULL;
static int              contigmem_refcnt;

TUNABLE_INT("hw.contigmem.num_buffers", &contigmem_num_buffers);
TUNABLE_QUAD("hw.contigmem.buffer_size", &contigmem_buffer_size);

static SYSCTL_NODE(_hw, OID_AUTO, contigmem, CTLFLAG_RD, 0, "contigmem");

SYSCTL_INT(_hw_contigmem, OID_AUTO, num_buffers, CTLFLAG_RD,
	&contigmem_num_buffers, 0, "Number of contigmem buffers allocated");
SYSCTL_QUAD(_hw_contigmem, OID_AUTO, buffer_size, CTLFLAG_RD,
	&contigmem_buffer_size, 0, "Size of each contiguous buffer");
SYSCTL_INT(_hw_contigmem, OID_AUTO, num_references, CTLFLAG_RD,
	&contigmem_refcnt, 0, "Number of references to contigmem");

static SYSCTL_NODE(_hw_contigmem, OID_AUTO, physaddr, CTLFLAG_RD, 0,
	"physaddr");

MALLOC_DEFINE(M_CONTIGMEM, "contigmem", "contigmem(4) allocations");

static int contigmem_modevent(module_t mod, int type, void *arg)
{
	int error = 0;

	switch (type) {
	case MOD_LOAD:
		error = contigmem_load();
		break;
	case MOD_UNLOAD:
		error = contigmem_unload();
		break;
	default:
		break;
	}

	return error;
}

moduledata_t contigmem_mod = {
	"contigmem",
	(modeventhand_t)contigmem_modevent,
	0
};

DECLARE_MODULE(contigmem, contigmem_mod, SI_SUB_DRIVERS, SI_ORDER_ANY);
MODULE_VERSION(contigmem, 1);

static struct cdevsw contigmem_ops = {
	.d_name         = "contigmem",
	.d_version      = D_VERSION,
	.d_flags        = D_TRACKCLOSE,
	.d_mmap_single  = contigmem_mmap_single,
	.d_open         = contigmem_open,
	.d_close        = contigmem_close,
};

static void
vm_domainset_iter_ignore(struct vm_domainset_iter *di, int domain)
{
	KASSERT(DOMAINSET_ISSET(domain, &di->di_valid_mask),
	    ("%s: domain %d not present in di_valid_mask for di %p",
	    __func__, domain, di));
	DOMAINSET_CLR(domain, &di->di_valid_mask);
}

static __always_inline void
kmem_alloc_san(vm_offset_t addr, vm_size_t size, vm_size_t asize, int flags)
{
	if ((flags & M_ZERO) == 0) {
		kmsan_mark((void *)addr, asize, KMSAN_STATE_UNINIT);
		kmsan_orig((void *)addr, asize, KMSAN_TYPE_KMEM,
		    KMSAN_RET_ADDR);
	} else {
		kmsan_mark((void *)addr, asize, KMSAN_STATE_INITED);
	}
	kasan_mark((void *)addr, size, asize, KASAN_KMEM_REDZONE);
}

static vm_page_t
kmem_alloc_contig_pages(vm_object_t object, vm_pindex_t pindex, int domain,
    int pflags, u_long npages, vm_paddr_t low, vm_paddr_t high,
    u_long alignment, vm_paddr_t boundary, vm_memattr_t memattr)
{
	vm_page_t m;
	int tries;
	bool wait, reclaim;

	VM_OBJECT_ASSERT_WLOCKED(object);

	wait = (pflags & VM_ALLOC_WAITOK) != 0;
	reclaim = (pflags & VM_ALLOC_NORECLAIM) == 0;
	pflags &= ~(VM_ALLOC_NOWAIT | VM_ALLOC_WAITOK | VM_ALLOC_WAITFAIL);
	pflags |= VM_ALLOC_NOWAIT;
	for (tries = wait ? 3 : 1;; tries--) {
		m = vm_page_alloc_contig_domain(object, pindex, domain, pflags,
		    npages, low, high, alignment, boundary, memattr);
		if (m != NULL || tries == 0 || !reclaim)
			break;

		VM_OBJECT_WUNLOCK(object);
		if (vm_page_reclaim_contig_domain(domain, pflags, npages,
		    low, high, alignment, boundary) == ENOMEM && wait)
			vm_wait_domain(domain);
		VM_OBJECT_WLOCK(object);
	}
	return (m);
}

static void *
kmem_alloc_contig_domain(int domain, vm_size_t size, int flags, vm_paddr_t low,
    vm_paddr_t high, u_long alignment, vm_paddr_t boundary,
    vm_memattr_t memattr)
{
	vmem_t *vmem;
	vm_object_t object;
	vm_pointer_t addr;
	vm_offset_t offset, tmp;
	vm_page_t end_m, m;
	vm_size_t asize;
	u_long npages;
	int pflags;

#ifdef __CHERI_PURE_CAPABILITY__
	size = CHERI_REPRESENTABLE_LENGTH(size);
#endif
	object = kernel_object;
	asize = round_page(size);
	vmem = vm_dom[domain].vmd_kernel_arena;
	if (vmem_alloc(vmem, asize, flags | M_BESTFIT, &addr))
		return (NULL);
	addr = cheri_kern_andperm(addr, CHERI_PERMS_KERNEL_DATA);
	offset = addr - VM_MIN_KERNEL_ADDRESS;
	pflags = malloc2vm_flags(flags) | VM_ALLOC_WIRED;
	npages = atop(asize);
	VM_OBJECT_WLOCK(object);
	printf("reaches to contig pages");
	m = kmem_alloc_contig_pages(object, atop(offset), domain,
	    pflags, npages, low, high, alignment, boundary, memattr);
	if (m == NULL) {
		VM_OBJECT_WUNLOCK(object);
		vmem_free(vmem, addr, asize);
		return (NULL);
	}
	KASSERT(vm_page_domain(m) == domain,
	    ("kmem_alloc_contig_domain: Domain mismatch %d != %d",
	    vm_page_domain(m), domain));
	end_m = m + npages;
	tmp = addr;
	for (; m < end_m; m++) {
		if ((flags & M_ZERO) && (m->flags & PG_ZERO) == 0)
			pmap_zero_page(m);
		vm_page_valid(m);
		VM_OBJECT_ASSERT_CAP(object, VM_PROT_RW_CAP);
		vm_page_aflag_set(m, PGA_CAPSTORE | PGA_CAPDIRTY);
		// To modify pmap_enter to use only huge pages
		pmap_enter(kernel_pmap, tmp, m, VM_PROT_RW_CAP,
		    VM_PROT_RW_CAP | PMAP_ENTER_WIRED, 0);
		tmp += PAGE_SIZE;
	}
	VM_OBJECT_WUNLOCK(object);
	kmem_alloc_san(addr, size, asize, flags);
#ifdef __CHERI_PURE_CAPABILITY__
	KASSERT(cheri_gettag(addr), ("Expected valid capability"));
	KASSERT(cheri_getlen(addr) == asize,
	    ("Inexact bounds expected %zx found %zx",
	    (size_t)asize, (size_t)cheri_getlen(addr)));
#endif
	return ((void *)addr);
}

static void *
kmem_alloc_contig_domainset(struct domainset *ds, vm_size_t size, int flags,
    vm_paddr_t low, vm_paddr_t high, u_long alignment, vm_paddr_t boundary,
    vm_memattr_t memattr)
{
	struct vm_domainset_iter di;
	vm_page_t bounds[2];
	void *addr;
	int domain;
	int start_segind;

	start_segind = -1;

	vm_domainset_iter_policy_init(&di, ds, &domain, &flags);
	do {
		addr = kmem_alloc_contig_domain(domain, size, flags, low, high,
		    alignment, boundary, memattr);
		if (addr != NULL)
			break;
		if (start_segind == -1)
			start_segind = vm_phys_lookup_segind(low);
		if (vm_phys_find_range(bounds, start_segind, domain,
		    atop(round_page(size)), low, high) == -1) {
			vm_domainset_iter_ignore(&di, domain);
		}
	} while (vm_domainset_iter_policy(&di, &domain) == 0);

	return (addr);
}

static void *
kmem_alloc_contig(vm_size_t size, int flags, vm_paddr_t low, vm_paddr_t high,
    u_long alignment, vm_paddr_t boundary, vm_memattr_t memattr)
{

	return (kmem_alloc_contig_domainset(DOMAINSET_RR(), size, flags, low,
	    high, alignment, boundary, memattr));
}

static void * 
contigmalloc(unsigned long size, struct malloc_type *type, int flags,
    vm_paddr_t low, vm_paddr_t high, unsigned long alignment,
    vm_paddr_t boundary)
{
    printf("contigmalloc called");
	void *ret;

	ret = (void *)kmem_alloc_contig(size, flags, low, high, alignment,
	    boundary, VM_MEMATTR_DEFAULT);
	if (ret != NULL)
		malloc_type_allocated(type, ret, round_page(size));
#ifdef __CHERI_PURE_CAPABILITY__
	KASSERT(cheri_gettag(ret), ("Expected valid capability"));
#endif

	return (ret);
}

// -------------------- Contigous kernel module load -------------------------------

static int
contigmem_load()
{

	int buffer_size;
	buffer_size = (int)contigmem_buffer_size;

	// get page size 
	printf("%d buffer size \n",buffer_size);

	char index_string[8], description[32];
	int  i, error = 0;
	void *addr;

	if (contigmem_num_buffers > RTE_CONTIGMEM_MAX_NUM_BUFS) {
		printf("%d buffers requested is greater than %d allowed\n",
				contigmem_num_buffers, RTE_CONTIGMEM_MAX_NUM_BUFS);
		error = EINVAL;
		goto error;
	}

	if (contigmem_buffer_size < PAGE_SIZE ||
			(contigmem_buffer_size & (contigmem_buffer_size - 1)) != 0) {
		printf("buffer size 0x%lx is not greater than PAGE_SIZE and "
				"power of two\n", contigmem_buffer_size);
		error = EINVAL;
		goto error;
	}

	for (i = 0; i < contigmem_num_buffers; i++) {
		addr = contigmalloc(contigmem_buffer_size, M_CONTIGMEM, M_NOWAIT,
			0, BUS_SPACE_MAXADDR, contigmem_buffer_size, 0);
		if (addr == NULL) {
			printf("contigmalloc failed for buffer %d\n", i);
			error = ENOMEM;
			goto error;
		}

#ifndef RTE_ARCH_ARM_PURECAP_HACK
		printf("%2u: virt=%p phys=%p\n", i, addr,
			(void *)pmap_kextract((vm_offset_t)addr));
#endif

		mtx_init(&contigmem_buffers[i].mtx, "contigmem", NULL, MTX_DEF);
		contigmem_buffers[i].addr = addr;
		contigmem_buffers[i].refcnt = 0;

		snprintf(index_string, sizeof(index_string), "%d", i);
		snprintf(description, sizeof(description),
				"phys addr for buffer %d", i);
		SYSCTL_ADD_PROC(NULL,
				&SYSCTL_NODE_CHILDREN(_hw_contigmem, physaddr), OID_AUTO,
				index_string, CTLTYPE_U64 | CTLFLAG_RD,
				(void *)(uintptr_t)i, 0, contigmem_physaddr, "LU",
				description);
	}

	contigmem_cdev = make_dev_credf(0, &contigmem_ops, 0, NULL, UID_ROOT,
			GID_WHEEL, 0600, "contigmem");

	return 0;

error:
	for (i = 0; i < contigmem_num_buffers; i++) {
		if (contigmem_buffers[i].addr != NULL) {
			contigfree(contigmem_buffers[i].addr,
				contigmem_buffer_size, M_CONTIGMEM);
			contigmem_buffers[i].addr = NULL;
		}
		if (mtx_initialized(&contigmem_buffers[i].mtx))
			mtx_destroy(&contigmem_buffers[i].mtx);
	}

	return error;
}

static int
contigmem_unload()
{
	int i;

	if (contigmem_refcnt > 0)
		return EBUSY;

	if (contigmem_cdev != NULL)
		destroy_dev(contigmem_cdev);

	if (contigmem_eh_tag != NULL)
		EVENTHANDLER_DEREGISTER(process_exit, contigmem_eh_tag);

	for (i = 0; i < RTE_CONTIGMEM_MAX_NUM_BUFS; i++) {
		if (contigmem_buffers[i].addr != NULL)
			contigfree(contigmem_buffers[i].addr,
				contigmem_buffer_size, M_CONTIGMEM);
		if (mtx_initialized(&contigmem_buffers[i].mtx))
			mtx_destroy(&contigmem_buffers[i].mtx);
	}

	return 0;
}

static int
contigmem_physaddr(SYSCTL_HANDLER_ARGS)
{
	uint64_t	physaddr;
	int		index = (int)(uintptr_t)arg1;

	physaddr = (uint64_t)vtophys(contigmem_buffers[index].addr);
	return sysctl_handle_64(oidp, &physaddr, 0, req);
}

static int
contigmem_open(struct cdev *cdev, int fflags, int devtype,
		struct thread *td)
{

	printf("Contigmem opened \n");

	atomic_add_int(&contigmem_refcnt, 1);

	return 0;
}

static int
contigmem_close(struct cdev *cdev, int fflags, int devtype,
		struct thread *td)
{

	atomic_subtract_int(&contigmem_refcnt, 1);

	return 0;
}

static int
contigmem_cdev_pager_ctor(void *handle, vm_ooffset_t size, vm_prot_t prot,
		vm_ooffset_t foff, struct ucred *cred, u_short *color)
{
	struct contigmem_vm_handle *vmh = handle;
	struct contigmem_buffer *buf;

	// TODO: add track to check on mmap to see if 
	// this is called with debug metrics

	printf("Create page called \n");

	buf = &contigmem_buffers[vmh->buffer_index];

	atomic_add_int(&contigmem_refcnt, 1);
    
	// Looks like a Mutex lock
	mtx_lock(&buf->mtx);
	// To check if memset is called
    // memset -	fill memory with a constant byte
    // The  memset()  function	fills  the  first  n  bytes of the memory area
    // pointed to by s with the	constant byte c.
	// Setting the bytes to 0.
	if (buf->refcnt == 0)
		memset(buf->addr, 0, contigmem_buffer_size);
	buf->refcnt++;

	// Looks like a Mutex unlock
	mtx_unlock(&buf->mtx);

	return 0;
}

// Creating machanism to count the impact 
// page faults in co-relation to run times. 

long time_taken;

static void
contigmem_cdev_pager_dtor(void *handle)
{
	struct contigmem_vm_handle *vmh = handle;
	struct contigmem_buffer *buf;

	// printf("Destroyed page called \n");

	buf = &contigmem_buffers[vmh->buffer_index];

	mtx_lock(&buf->mtx);
	buf->refcnt--;
	mtx_unlock(&buf->mtx);

	free(vmh, M_CONTIGMEM);

	// printf("Total time taken %ld \n",time_taken);

	time_taken = 0;

	atomic_subtract_int(&contigmem_refcnt, 1);
}

static int
contigmem_cdev_pager_fault(vm_object_t object, vm_ooffset_t offset, int prot,
		vm_page_t *mres)
{


	vm_paddr_t paddr;
	vm_page_t m_paddr, page;
	vm_memattr_t memattr, memattr1;

	// printf("test page 12=%lu",(*mres)->pindex);
	// printf("offset=%p", *offset);

    struct timespec bin;

	nanotime(&bin);

	// printf("Page fault \n");

	// printf("Time Page fault start %ld\n",bin.tv_nsec);

	memattr = object->memattr;

	VM_OBJECT_WUNLOCK(object);

	paddr = offset;

	m_paddr = vm_phys_paddr_to_vm_page(paddr);
	if (m_paddr != NULL) {
		memattr1 = pmap_page_get_memattr(m_paddr);
		if (memattr1 != memattr) {
			printf("different memory attributes");
			memattr = memattr1;
		}
	}

	if (((*mres)->flags & PG_FICTITIOUS) != 0) {
		/*
		 * If the passed in result page is a fake page, update it with
		 * the new physical address.
		 */
		printf("Fake page \n");
		page = *mres;
		VM_OBJECT_WLOCK(object);
		vm_page_updatefake(page, paddr, memattr);
	} else {
		/*
		 * Replace the passed in reqpage page with our own fake page and
		 * free up the original page.
		 */
		page = vm_page_getfake(paddr, memattr);
		VM_OBJECT_WLOCK(object);
#if __FreeBSD__ >= 13
		vm_page_replace(page, object, (*mres)->pindex, *mres);
#else
		vm_page_t mret = vm_page_replace(page, object, (*mres)->pindex);
		KASSERT(mret == *mres,
		    ("invalid page replacement, old=%p, ret=%p", *mres, mret));
		vm_page_lock(mret);
		vm_page_free(mret);
		vm_page_unlock(mret);
#endif
		*mres = page;
	}

	page->valid = VM_PAGE_BITS_ALL;

	struct timespec bin1;

	nanotime(&bin1);

	// printf("Time Page fault end %ld\n",bin1.tv_nsec);

	time_taken = time_taken + (bin1.tv_nsec - bin.tv_nsec);

	return VM_PAGER_OK;
}

static struct cdev_pager_ops contigmem_cdev_pager_ops = {
	.cdev_pg_ctor = contigmem_cdev_pager_ctor,
	// Regular page
	.cdev_pg_dtor = contigmem_cdev_pager_dtor,
	// Page fault
	.cdev_pg_fault = contigmem_cdev_pager_fault,
};

static int
contigmem_mmap_single(struct cdev *cdev, vm_ooffset_t *offset, vm_size_t size,
		struct vm_object **obj, int nprot)
{

	// Testing if this is called when file is opened
	printf("contigmem_mmap_single called \n");

	struct contigmem_vm_handle *vmh;
	uint64_t buffer_index;

	/*
	 * The buffer index is encoded in the offset.  Divide the offset by
	 *  PAGE_SIZE to get the index of the buffer requested by the user
	 *  app.
	 */
	buffer_index = *offset / PAGE_SIZE;
	if (buffer_index >= contigmem_num_buffers)
		return EINVAL;

	if (size > contigmem_buffer_size)
		return EINVAL;

    // Allocates unitialized space in the kernel 
	vmh = malloc(sizeof(*vmh), M_CONTIGMEM, M_NOWAIT | M_ZERO);
	if (vmh == NULL)
		return ENOMEM;
	vmh->buffer_index = buffer_index;
    
	*offset = (vm_ooffset_t)vtophys(contigmem_buffers[buffer_index].addr);

	// printf("test virt=%p",vm_ooffset_t);

	// Print offset ? 
	
	// Allocates to a particular page
	*obj = cdev_pager_allocate(vmh, OBJT_DEVICE, &contigmem_cdev_pager_ops,
			size, nprot, *offset, curthread->td_ucred);

	return 0;
}

// Todo: 
// - Get the automated flow working. (Done)
// - Print physical address of sample C programs (Done)
// - Check grouping of TLB entries. 
// - Get writing for EuroSys. (Started)

// - Test kmeans mmap vs modified mmap (seems to have same runtime)
// - Test block based behavoir ()
// - 
