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

#ifndef STDDEFINES_H_
#define STDDEFINES_H_

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
#include <stdbool.h>  // For boolean data type (bool, true, false)

#define	MAXPAGESIZES	2


//#define TIMING

/* Debug printf */
#define dprintf(...) fprintf(stdout, __VA_ARGS__)

/* Wrapper to check for errors */
#define CHECK_ERROR(a)                                       \
   if (a)                                                    \
   {                                                         \
      perror("Error at line\n\t" #a "\nSystem Msg");         \
      assert ((a) == 0);                                     \
   }

static inline void *MALLOC(size_t size)
{
   void * temp = malloc(size);
   assert(temp);
   return temp;
}

static inline void *CALLOC(size_t num, size_t size)
{
   void * temp = calloc(num, size);
   assert(temp);
   return temp;
}

static inline void *REALLOC(void *ptr, size_t size)
{
   void * temp = realloc(ptr, size);
   assert(temp);
   return temp;
}

static inline char *GETENV(char *envstr)
{
   char *env = getenv(envstr);
   if (!env) return "0";
   else return env;
}

#define GET_TIME(start, end, duration)                                     \
   duration.tv_sec = (end.tv_sec - start.tv_sec);                         \
   if (end.tv_nsec >= start.tv_nsec) {                                     \
      duration.tv_nsec = (end.tv_nsec - start.tv_nsec);                   \
   }                                                                       \
   else {                                                                  \
      duration.tv_nsec = (1000000000L - (start.tv_nsec - end.tv_nsec));   \
      duration.tv_sec--;                                                   \
   }                                                                       \
   if (duration.tv_nsec >= 1000000000L) {                                  \
      duration.tv_sec++;                                                   \
      duration.tv_nsec -= 1000000000L;                                     \
   }

static inline unsigned int time_diff (
    struct timeval *end, struct timeval *begin)
{
#ifdef TIMING
    uint64_t result;

    result = end->tv_sec - begin->tv_sec;
    result *= 1000000;     /* usec */
    result += end->tv_usec - begin->tv_usec;

    return result;
#else
    return 0;
#endif
}

// static inline void get_time (struct timeval *t)
// {
// #ifdef TIMING
//     gettimeofday (t, NULL);
// #endif
// }

// Expirement work

#define FILENAME "/dev/contigmem"

static char *heap_start;
static char *heap;
static size_t HEAP_SIZE = 1024 * 1024 * 1024;

void *ptr;
void *ptr1;
void *ptr2;
int MallocCounter;

size_t sizeUsed;

INITAlloc(void) {

   size_t sz;
   // Pre Allocate 600 MB 
   sz = 100000000;

   int fd = open(FILENAME, O_RDWR, 0600);

    if (fd < 0) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    off_t offset = 0; // offset to seek to.

    if (ftruncate(fd, sz) < 0) {
        perror("ftruncate");
        close(fd);
        exit(EXIT_FAILURE);
    }

   //  ptr = mmap(NULL, sz,
   //  PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON,-1,0);

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

// Quick malloc implementation with mmap
void* MALLOCCHERI(size_t sz)
{
   sz = __builtin_align_up(sz, _Alignof(max_align_t));

    if (sz > MallocCounter) {
      printf("%d Threashold exceeded\n", sz);
      INITREGULARALLOC(1);
    }

   MallocCounter -= sz;

   // printf("%d \n", sz);
   printf("%d Malloc counter new\n", MallocCounter);

   void *ptrLink = &ptr[MallocCounter];
   ptrLink = cheri_bounds_set(ptrLink, sz);

   return ptrLink;

//   if (heap + sz > heap_start + HEAP_SIZE) return NULL;
//   heap += sz;
//   return heap - sz;
     
}

// Quick cheri free implementation
void FREECHERI(void *ptr) { 

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
     
	// 	atf_tc_skip("no large page support");
	return (pscnt);
}

INITREGULARALLOC(int full) {
   size_t sz;
   // Hard-coded for 1GB huge page
   sz = 1073741824;

   int error, fd, pscnt, pn;

   size_t ps[MAXPAGESIZES];

   size_t size[3];

   // Point to initially to pointer 1 
   if (full == 1) {
      ptr = ptr2;
   } 
   else {
      ptr = ptr1;
   }
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
// Standard Alloc 
// void* MALLOCREGULAR(size_t sz) {
   
// }


// void* CLEARALLOC(void) {
// /
// }

#endif // STDDEFINES_H_


