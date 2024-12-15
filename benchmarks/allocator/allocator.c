/* Copyright (c) 2007-2009, Stanford University
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*     * Redistributions of source code must retain the above copyright
*       notice, this list of conditions and the following disclaimer.
*     * Redistributions in binary form must reproduce the above copyright
*       notice, this list of conditions and the following disclaimer in the
*       documentation and/or other materials provided with the distribution.
*     * Neither the name of Stanford University nor the
*       names of its contributors may be used to endorse or promote products
*       derived from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY STANFORD UNIVERSITY ``AS IS'' AND ANY
* EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
* DISCLAIMED. IN NO EVENT SHALL STANFORD UNIVERSITY BE LIABLE FOR ANY
* DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
* (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
* ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/ 

// #define STDDEFINES_H_

#include <assert.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/errno.h>
#include <stdint.h>
#include <stdio.h>
#include	<unistd.h>


#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include	<sys/types.h>

#include <cheriintrin.h>
#include <cheri/cheric.h>

#include <sys/stat.h>
#include <fcntl.h>

// #include "bitmap.h"
// #include "simple.h"

#define	MAXPAGESIZES	2

/* Debug printf */
#define dprintf(...) fprintf(stdout, __VA_ARGS__)

// Expirement work

#define FILENAME "/dev/contigmem"

// static void INITREGULARALLOC() __attribute__((constructor));

static char *heap_start;
static char *heap;
static size_t HEAP_SIZE = 1024 * 1024 * 1024;

void *ptr;
int MallocCounter;


static size_t sizeUsed;

// Quick malloc implementation with mmap
void *my_malloc(size_t sz)
{
   sz = __builtin_align_up(sz, _Alignof(max_align_t));

   // printf("%d \n", sz);
   // printf("%d Malloc counter\n", MallocCounter);

   MallocCounter -= sz;
   void *ptrLink = &ptr[MallocCounter];
   ptrLink = cheri_setbounds(ptrLink, sz);

   return ptrLink;

//   if (heap + sz > heap_start + HEAP_SIZE) return NULL;
//   heap += sz;
//   return heap - sz;
     
}

// Quick cheri free implementation
void my_free(void *ptr) { 

   // printf("free called \n");

   // get bounds from 
   int len = cheri_getlen(ptr);
   
   // printf("free len %d \n", len);

   munmap(ptr, len);
}

static int
pagesizes(size_t ps[MAXPAGESIZES])
{
	int pscnt;

	pscnt = getpagesizes(ps, MAXPAGESIZES);
	// ATF_REQUIRE_MSG(pscnt != -1, "getpagesizes failed; errno=%d", errno);
	// ATF_REQUIRE_MSG(ps[0] != 0, "psind 0 is %zu", ps[0]);
	// ATF_REQUIRE_MSG(pscnt <= MAXPAGESIZES, "invalid pscnt %d", pscnt);
	// if (pscnt == 1){
   //    printf("pscnt is 1");
   // }
     
	// 	atf_    tc_skip("no large page support");
	return (pscnt);
}

// static void INITREGULARALLOC() {

// }

// __attribute__((constructor))
// static void malloc_init() {
//    fprintf(stderr, "here");
//    size_t sz;
//    // Pre Allocate 400 MB 
//    sz = 1073741824;

//    int error, fd, pscnt, pn;

//    size_t ps[MAXPAGESIZES];

//    size_t size[3];

//    pn = getpagesizes(size, 3);
//    dprintf("page size is [%d]", size[2]);

//    pscnt = pagesizes(ps);

// 	fd = shm_create_largepage(SHM_ANON, O_CREAT | O_RDWR, 1, SHM_LARGEPAGE_ALLOC_DEFAULT, 0);

//    if (fd < 0 && errno == ENOTTY) {
//       perror("sh_create_largepages");
//       close(fd);
//       exit(EXIT_FAILURE);
//    }
//    // if (fd < 0)
//    //     perror("no large page supported");
//    //     exit(EXIT_FAILURE);
// 	// if (fd < 0 && errno == ENOTTY)
// 	// 	atf_tc_skip("no large page support");
// 	// ATF_REQUIRE_MSG(fd >= 0, "shm_create_largepage failed; errno=%d", errno);

// 	if (ftruncate(fd, sz) < 0) {
//         perror("ftruncate");
//         close(fd);
//         exit(EXIT_FAILURE);
//     }
// 	// if (error != 0 && errno == ENOMEM)
// 	// 	/*
// 	// 	 * The test system might not have enough memory to accommodate
// 	// 	 * the request.
// 	// 	 */
// 	// 	atf_tc_skip("failed to allocate %zu-byte superpage", sz);
// 	// ATF_REQUIRE_MSG(error == 0, "ftruncate failed; errno=%d", errno);

//    ptr = mmap(NULL, sz,
//     PROT_READ|PROT_WRITE, MAP_SHARED,fd,0);

//    // Added error handling
//     if(ptr == MAP_FAILED)
//     {
//         perror("mmap");
//         exit(EXIT_FAILURE);
//     }

//     MallocCounter = (int)sz;
  
// }


// __attribute__((destructor))
// static void malloc_exit() {
//   fprintf(stderr, "lol");
// }

static int initialized = 0; /* Is library initialized? */

/** Shared library constructor. */
__attribute__((constructor)) void shlib_init(void)
{
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

    MallocCounter = (int)sz;
}

// /** Shared library destructor. */
// __attribute__((destructor)) void shlib_fini(void)
// {
//   printf("Destructor[%d]\n", initialized);
//   fflush(stdout);
//   initialized = 0;
// }

/** Shared library function that creates something. */
// void shlib_create_function(void)
// {
//   printf("create function[%d]\n", initialized);
//   fflush(stdout);
// }

// /** Undo shlib_create_function(). */
// void shlib_destroy_function(void)
// {
//   printf("destroy function[%d]\n", initialized);
//   fflush(stdout);
// }
