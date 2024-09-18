//
// Created by Akilan on 07/03/2024.
//

#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

#include <dlfcn.h>
#include <sys/fcntl.h>
#include <sys/stat.h>

#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/wait.h>

#include <assert.h>
#include <sys/time.h>
#include <stdint.h>
#include <stdio.h>

#define FILENAME "/dev/contigmem"



static inline void *MALLOC(size_t size)
{
//    void * temp = malloc(size);
//    assert(temp);
//    return temp;

// Ensuring malloc this is mmap and phyiscally contigous
    
    // void *ptr = malloc(size);
    // return ptr;
}

// Currently not implementing free
// This is to ensure the PureCap
// program can terminate itself
// even though there is memory not
// cleared.
static inline void *FREE(void *ptr)
{
    // int *pt = ptr;
    // size_t size;
    // --pt;
    // size = *pt;
    // if(munmap(pt, size) == -1)
    // {
    //     perror("munmap");
    //     exit(EXIT_FAILURE);
    // }
    // free(ptr);
}


inline void *MALLOCPHYSICALLCONTIGOUS(size_t size) {
    int fd = open
            (FILENAME, O_RDWR | O_CREAT, 0600);
    if (fd < 0) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    off_t offset = 0; // offset to seek to.

    if (ftruncate(fd, size) < 0) {
        perror("ftruncate");
        close(fd);
        exit(EXIT_FAILURE);
    }

    int *ptr = mmap(NULL, size,
                    PROT_READ | PROT_WRITE, MAP_SHARED,
                    fd, offset);
    if(ptr == MAP_FAILED)
    {
        perror("mmap");
        exit(EXIT_FAILURE);
    }

    *ptr = size;

    return ptr;
}

