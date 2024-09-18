/*-
 * SPDX-License-Identifier: BSD-2-Clause
 *
 * Copyright (c) 1999 Assar Westerlund
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#include <sys/param.h>
#include <sys/proc.h>
#include <sys/module.h>
#include <sys/sysproto.h>
#include <sys/sysent.h>
#include <sys/kernel.h>
#include <sys/systm.h>

#include <sys/malloc.h>
#include <sys/types.h>

#include <machine/bus.h>



MALLOC_DEFINE(M_CONTIGMEM, "contigmem", "contigmem(4) allocations");

// struct syscall_hello {
// 	unsigned long             size;
// };

struct syscall_alloc {
	int                       size;
	int                       malloc; 
	// int                       *newSize;
	// void                      *addr;
};

// syscall for allocating contigous memory.
static int
Alloc(struct thread *td, struct syscall_alloc *uap)
{    

	// struct syscall_alloc *uap;
    // uap = (struct syscall_alloc *)arg;

	struct syscall_alloc state_copy;

	state_copy = *uap;

	int uap_size = 4;
	// int malloc = uap->malloc;

	printf("size %d \n", state_copy.size);

	// printf("malloc tried 1 %d \n",*uap->malloc);

	if(state_copymalloc == 1) {
		 // Calculate next power of 2 

	printf("Malloc called \n");

	int alignment  =  1;
    
	// 2 refers to the size
    while  ( alignment  <=  uap_size) {
      alignment  =  alignment  <<  1 ;
    }

	// uap->size = 3;

	// td->td_retval[0] = uap;


    // printf("Changing size \n"); 

	state_copy.size = 10;

	*uap = state_copy;

	// *arg = uap;

	printf("alignment %d \n", alignment);

	// To call contig alloc and free based on 
	// hardcoded physical allocations and adding 
	// doing array allocations and frees. 
	// void *addr;

	// int alignmentInt;
	// // alignmentInt = nextPowerOf2(2);
	// unsigned long alignment = ( unsigned long ) alignmentInt ;

    // addr = contigmalloc(uap_size, M_CONTIGMEM, M_ZERO,
	// 		0, BUS_SPACE_MAXADDR, alignment, 0);

	// uap->addr = addr;

	// printf("Malloc complete");

	// to write address to /proc and to read allocated address from /proc 

	return (4); 

	} else {

		// printf("Free called complete");

        // contigfree(uap->addr,uap->size, M_CONTIGMEM);

	    // printf("Free complete");
	}




	return (0);
}

// // syscall for allocating contigous memory.
// static int
// Free(struct thread *td, void *arg)
// {    

// 	struct syscall_alloc *uap;
//     uap = (struct syscall_alloc *)arg;

// 	unsigned long uap_size = uap->size;

// 	printf("free size %lu \n", uap_size);


//     // // Calculate next power of 2 

// 	// unsigned long  alignment  =  1;
    
// 	// // 2 refers to the size
//     // while  ( alignment  <=  uap_size) {
//     //   alignment  =  alignment  <<  1 ;
//     // }

// 	// printf("alignment %lu \n", alignment);

// 	// // To call contig alloc and free based on 
// 	// // hardcoded physical allocations and adding 
// 	// // doing array allocations and frees. 
// 	// void *addr;

// 	// int alignmentInt;
// 	// // alignmentInt = nextPowerOf2(2);
// 	// unsigned long alignment = ( unsigned long ) alignmentInt ;

// 	contigfree(uap->addr,uap->size, M_CONTIGMEM);

//     // addr = contigmalloc(uap_size, M_CONTIGMEM, M_ZERO,
// 	// 		0, BUS_SPACE_MAXADDR, alignment, 0);

//     // int *addr1;
// 	// addr1 = contigmalloc(2, M_CONTIGMEM, M_ZERO,
// 	// 		0, BUS_SPACE_MAXADDR, alignment, 0);

// 	// uap->addr = addr;

// 	// addr1[0] = 2;

// 	// printf("address 0 %i \n", addr[0]);
// 	// printf("address 0 %i \n", addr1[0]);

// 	// contigfree(addr,2, M_CONTIGMEM);
// 	// contigfree(addr1,2, M_CONTIGMEM);

// 	// printf("contigfree complete");

// 	// printf("hello kernel 1\n");

// 	// printf("hello kernel\n");
// 	return (0);
// }
// define custom args.
/*
 * The function for implementing the syscall.
 */
// static int
// hello(struct thread *td, void *arg)
// {    

// 	struct syscall_hello *uap;
//     uap = (struct syscall_hello *)arg;

// 	unsigned long uap_size = uap->size;

// 	printf("size %lu \n", uap_size);


//     // Calculate next power of 2 

// 	unsigned long  alignment  =  1;
    
// 	// 2 refers to the size
//     while  ( alignment  <=  2) {
//       alignment  =  alignment  <<  1 ;
//     }

// 	printf("alignment %lu \n", alignment);

// 	// To call contig alloc and free based on 
// 	// hardcoded physical allocations and adding 
// 	// doing array allocations and frees. 
// 	int *addr;

// 	// int alignmentInt;
// 	// // alignmentInt = nextPowerOf2(2);
// 	// unsigned long alignment = ( unsigned long ) alignmentInt ;

//     addr = contigmalloc(2, M_CONTIGMEM, M_ZERO,
// 			0, BUS_SPACE_MAXADDR, alignment, 0);

// 	addr[0] = 1;

//     int *addr1;
// 	addr1 = contigmalloc(2, M_CONTIGMEM, M_ZERO,
// 			0, BUS_SPACE_MAXADDR, alignment, 0);

// 	addr1[0] = 2;

// 	printf("address 0 %i \n", addr[0]);
// 	printf("address 0 %i \n", addr1[0]);

// 	contigfree(addr,2, M_CONTIGMEM);
// 	contigfree(addr1,2, M_CONTIGMEM);

// 	printf("contigfree complete");

// 	printf("hello kernel 1\n");

// 	printf("hello kernel\n");
// 	return (0);
// }

// calculate next power of 2 
// int nextPowerOf2 (unsigned  int  x) {
// int  value  =  1;

// while  ( value  <=  x) {
// value  =  value  <<  1 ;
// }

// return  value;
// }

/*
 * The `sysent' for the new syscall
 */
static struct sysent Malloc_sysent = {
	.sy_narg = 1,
	.sy_call = (sy_call_t*)Alloc
};

// static struct sysent Free_sysent = {
// 	.sy_narg = 0,
// 	.sy_call = Free
// };

/*
 * The offset in sysent where the syscall is allocated.
 */
static int Mallocoffset = NO_SYSCALL;
// static int Freeoffset = NO_SYSCALL;

/*
 * The function called at load/unload.
 */
static int
load(struct module *module, int cmd, void *arg)
{
	int error = 0;

	switch (cmd) {
	case MOD_LOAD :
		printf("Malloc syscall loaded at %d\n", Mallocoffset);
		// printf("Free syscall loaded at %d\n", Freeoffset);
		break;
	case MOD_UNLOAD :
		printf("Malloc syscall unloaded from %d\n", Mallocoffset);
		// printf("Free syscall unloaded from %d\n", Freeoffset);
		break;
	default :
		error = EOPNOTSUPP;
		break;
	}
	return (error);
}

SYSCALL_MODULE(syscall, &Mallocoffset, &Malloc_sysent, load, NULL);
// SYSCALL_MODULE(syscall, &Freeoffset, &Free_sysent, load, NULL);