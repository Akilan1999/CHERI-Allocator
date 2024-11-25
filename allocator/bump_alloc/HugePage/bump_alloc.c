/**********************************
 * bump_alloc.c
 * Jeremy.Singer@glasgow.ac.uk
 *
 * This is a simple bump-pointer allocator.
 * It mmaps a large buffer of SIZE bytes,
 * then allocates this space in word-sized
 * chunks to client code (in main fn).
 *
 * Initial simple memory allocator test.
 * Explore capability narrowing operations
 * and intrinsics for bound reporting.
 */

#include <cheriintrin.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

#include "bump_alloc.h"

int count = 0;       /* number of bytes allocated so far*/
int max = 0;         /* upper limit for count */
char *buffer = NULL; /* the allocation buffer */

void init_alloc()
{
    // /* request memory for our allocation buffer
    //  * NB mmap min bounds for capability is 1 page (4K)
    //  */
    // char *res = mmap(NULL, size_in_bytes, PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, -1, 0);

    // if (res == MAP_FAILED)
    // {
    //     perror("error in initial mem allocation");
    //     exit(-1);
    // }

    // buffer = res;
    // max = size_in_bytes;
    // return;

     size_t sz;
   // Pre Allocate 400 MB 
   sz = 1073741824;

   int error, fd, pscnt, pn;

   size_t ps[MAXPAGESIZES];

   size_t size[3];

   pn = getpagesizes(size, 3);
   printf("page size is [%d]", size[2]);

   pscnt = pagesizes(ps);

	fd = shm_create_largepage(SHM_ANON, O_CREAT | O_RDWR, 1, SHM_LARGEPAGE_ALLOC_DEFAULT, 0);

   if (fd < 0 && errno == ENOTTY) {
      perror("sh_create_largepages");
      close(fd);
      exit(EXIT_FAILURE);
   }
   // if (fd < 0)
   //     perror("no large page supported");
   //     exit(EXIT_FAILURE);
	// if (fd < 0 && errno == ENOTTY)
	// 	atf_tc_skip("no large page support");
	// ATF_REQUIRE_MSG(fd >= 0, "shm_create_largepage failed; errno=%d", errno);

	if (ftruncate(fd, sz) < 0) {
        perror("ftruncate");
        close(fd);
        exit(EXIT_FAILURE);
    }
	// if (error != 0 && errno == ENOMEM)
	// 	/*
	// 	 * The test system might not have enough memory to accommodate
	// 	 * the request.
	// 	 */
	// 	atf_tc_skip("failed to allocate %zu-byte superpage", sz);
	// ATF_REQUIRE_MSG(error == 0, "ftruncate failed; errno=%d", errno);

   ptr = mmap(NULL, sz,
    PROT_READ|PROT_WRITE, MAP_SHARED,fd,0);

   // Added error handling
    if(ptr == MAP_FAILED)
    {
        perror("mmap");
        exit(EXIT_FAILURE);
    }

    buffer = ptr;

    // Hard-coded huge page size
    max = 1073741824;

    return ptr;
}

/*
 * allocate len bytes with bump pointer allocator
 * this is our simplistic `malloc` function
 */
void *malloc(size_t len)
{
    char *chunk = buffer + count;
    size_t rounded_len; /* for CHERI alignment */
    size_t new_count;   /* for buffer overflow check */

    /* ensure we can represent the capability accurately,
     * see p30 of CHERI C/C++ Prog Guide (June 2020)
     * www.cl.cam.ac.uk/techreports/UCAM-CL-TR-947
     */
    chunk = __builtin_align_up(chunk, ~cheri_representable_alignment_mask(len) + 1);
    rounded_len = cheri_representable_length(len);

    new_count = (chunk + rounded_len) - buffer;
    if (new_count > max)
    {
        /* out of bounds - don't allocate anything */
        chunk = 0;
    }
    else
    {
        /* restrict capability range before returning ptr */
        chunk = cheri_bounds_set_exact(chunk, rounded_len);

        /* update bytes allocated count */
        count = new_count;
    }

    return chunk;
}