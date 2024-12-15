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

// #include "bitmap.h"
// #include "simple.h"

#define	MAXPAGESIZES	2


// init_malloc(void) {
//    // Init malloc implementation
//    INITREGULARALLOC();

//    // init_alloc(100,100000);
// //    brm_init();
//   //alloc_init(104857632);
// }

// void* MALLOC(size_t sz) {
//    // malloc implementation
//    return MALLOCCHERI(sz);
// //    return malloc_buddy(sz);
// //    return alloc(sz);
//    // return (void *)alloc_chunk();
// }

// void FREE(void *ptr) {
//    // free implementation
//    FREECHERI(ptr);
//    // free_chunk(ptr);
//    //free_mem(ptr);
// }


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

// static inline void *MALLOC(size_t size)
// {
//    void * temp = malloc(size);
//    assert(temp);
//    return temp;
// }

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

// #define GET_TIME(start, end, duration)                                     \
//    duration.tv_sec = (end.tv_sec - start.tv_sec);                         \
//    if (end.tv_nsec >= start.tv_nsec) {                                     \
//       duration.tv_nsec = (end.tv_nsec - start.tv_nsec);                   \
//    }                                                                       \
//    else {                                                                  \
//       duration.tv_nsec = (1000000000L - (start.tv_nsec - end.tv_nsec));   \
//       duration.tv_sec--;                                                   \
//    }                                                                       \
//    if (duration.tv_nsec >= 1000000000L) {                                  \
//       duration.tv_sec++;                                                   \
//       duration.tv_nsec -= 1000000000L;                                     \
//    }

// static inline unsigned int time_diff (
//     struct timeval *end, struct timeval *begin)
// {
// #ifdef TIMING
//     uint64_t result;

//     result = end->tv_sec - begin->tv_sec;
//     result *= 1000000;     /* usec */
//     result += end->tv_usec - begin->tv_usec;

//     return result;
// #else
//     return 0;
// #endif
// }

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
int MallocCounter;

size_t sizeUsed;

// INITAlloc(void) {

//    size_t sz;
//    // Pre Allocate 600 MB 
//    sz = 100000000;

//    int fd = open(FILENAME, O_RDWR, 0600);

//     if (fd < 0) {
//         perror("open");
//         exit(EXIT_FAILURE);
//     }

//     off_t offset = 0; // offset to seek to.

//     if (ftruncate(fd, sz) < 0) {
//         perror("ftruncate");
//         close(fd);
//         exit(EXIT_FAILURE);
//     }

//    //  ptr = mmap(NULL, sz,
//    //  PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON,-1,0);

//     ptr = mmap(NULL, sz,
//     PROT_READ|PROT_WRITE, MAP_SHARED,fd,0);

//    // Added error handling
//     if(ptr == MAP_FAILED)
//     {
//         perror("mmap");
//         exit(EXIT_FAILURE);
//     }

//     MallocCounter = (int)sz;

// }

// Quick malloc implementation with mmap
void* my_malloc(size_t sz)
{
   printf("called");
   sz = __builtin_align_up(sz, _Alignof(max_align_t));

   // printf("%d \n", sz);
   printf("%d Malloc counter\n", MallocCounter);

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
     
	// 	atf_tc_skip("no large page support");
	return (pscnt);
}

INITREGULARALLOC(void) {
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


// ------------------------------ bitmap allocator ----------------------------

#define BITS_PER_BYTE 8

char *buffer = NULL;          /* allocation buffer */
unsigned char *bitmap = NULL; /* bitmap for the buffer */

int buffer_size = 0;     /* size of buffer (in bytes) */
int bitmap_size = 0;     /* size of bitmap (in bytes) */
int bytes_per_chunk = 0; /* size of single chunk (in bytes) */

void init_alloc(int num_chunks, int chunk_size)
{
    int i = 0;

    /* we need to increase the num_chunks
     * so every bit in bitmap will be used
     */
    int adjusted_num_chunks = (num_chunks % BITS_PER_BYTE == 0)
                                  ? num_chunks
                                  : (num_chunks + (BITS_PER_BYTE - (num_chunks % BITS_PER_BYTE)));

    /* we need to increase the chunk_size
     * so chunks will be CHERI aligned
     * (i.e. 16 bytes for RISC-V 64-bit arch)
     */
    int adjusted_chunk_size =
        (chunk_size % (sizeof(void *)) == 0)
            ? chunk_size
            : (chunk_size + (sizeof(void *)) - (chunk_size % (sizeof(void *))));

    /* check this chunk size is small enough so we can represent
     * bounds precisely with CHERI compressed representation
     */
    adjusted_chunk_size = cheri_representable_length(adjusted_chunk_size);

    /* request memory for our allocation buffer */
    char *res = mmap(NULL, adjusted_num_chunks * adjusted_chunk_size, PROT_READ | PROT_WRITE,
                     MAP_ANON | MAP_PRIVATE, -1, 0);
    /* request memory for our bitmap */
    bitmap = (void *) mmap(NULL, adjusted_num_chunks / BITS_PER_BYTE,
                                    PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, -1, 0);

    if (res == MAP_FAILED || bitmap == MAP_FAILED)
    {
        perror("error in initial mem allocation");
        exit(-1);
    }

    /* NB mmap min bounds for capability is 1 page (4K) */
    buffer = res;
    /* check buffer is aligned */
    assert((uintptr_t) buffer % sizeof(void *) == 0);
    /* check bitmap is aligned */
    assert((uintptr_t) bitmap % sizeof(void *) == 0);

    bytes_per_chunk = adjusted_chunk_size;
    buffer_size = adjusted_num_chunks * adjusted_chunk_size;
    bitmap_size = adjusted_num_chunks / BITS_PER_BYTE;

    /* zero bitmap, since all chunks are free initially */
    for (i = 0; i < bitmap_size; i++)
    {
        bitmap[i] = 0;
    }

    // set exact bounds for buffer and bitmap?
    buffer = cheri_setbounds(buffer, buffer_size);
    bitmap = cheri_setbounds(bitmap, bitmap_size);
    return;
}

/*
 * allocate fixed size chunk with bitmap allocator
 * this is our simplistic `malloc` function
 */
char *alloc_chunk()
{
    unsigned char updated_byte = 0;
    int chunk_index = 0;
    char *chunk = NULL;
    // iterate over all bits in bitmap, looking for a 0
    // when we find a 0, set it to 1 and
    // return the corresponding chunk
    // (setting its capability bounds)
    int i = 0;
    while (bitmap[i] == (unsigned char) 0xff)
    {
        i++;
        if (i >= bitmap_size)
            break;
    }
    // do we have a 0?
    if (i < bitmap_size && bitmap[i] != (unsigned char) 0xff)
    {
        // find the lowest 0 ...
        int j = 0;
        // right shift until bottom bit is 0
        for (j = 0; j < BITS_PER_BYTE; j++)
        {
            int bit = (bitmap[i] >> j) & 1;
            if (bit == 0)
            {
                break;
            }
        }
        // now i is the word index, j is the bit index
        // set this bit to 1 ...
        // and work out the chunk to allocate
        updated_byte = bitmap[i] + (unsigned char) (1 << j);
        bitmap[i] = updated_byte;

        chunk_index = i * BITS_PER_BYTE + j;
        chunk = buffer + (chunk_index * bytes_per_chunk);

        /* restrict capability range before returning ptr */
        chunk = cheri_setbounds(chunk, bytes_per_chunk);
    }

    return chunk;
}

void free_chunk(void *chunk)
{
    vaddr_t base = cheri_getbase(chunk);
    vaddr_t buff_base = cheri_getbase(buffer);
    /* calculate chunk index in buffer */
    int chunk_index = (base - buff_base) / bytes_per_chunk;
    assert(chunk_index >= 0);
    /* calculate corresponding bitmap index */
    int bitmap_index = chunk_index / BITS_PER_BYTE;
    assert(bitmap_index < bitmap_size);
    int bitmap_offset = chunk_index % BITS_PER_BYTE;
    /* set this bitmap entry to 0 */
    unsigned char updated_byte = bitmap[bitmap_index] & (unsigned char) (~(1 << bitmap_offset));
    bitmap[bitmap_index] = updated_byte;
    return;
}

int num_used_chunks()
{
    int i = 0;
    int used_chunks = 0;

    while (i < bitmap_size)
    {
        unsigned char x = bitmap[i];
        if (x != 0)
        {
            /* some used chunks here */
            unsigned char j;
            for (j = 1; j <= x; j = j << 1)
            {
                if (x & j)
                {
                    used_chunks++;
                }
            }
        }
        i++;
    }
    return used_chunks;
}

#endif // STDDEFINES_H_