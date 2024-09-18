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

#define FILENAME "/dev/contigmem"

void *malloc(size_t sz) {
    int *ptr;
    int len = sz + sizeof(sz);

    ptr = mmap(0, len, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);

    *ptr = len;

    // To probably set exact bounds on it
    return (void *)(&ptr[1]);
}

// Currently not implementing free
// This is to ensure the PureCap
// program can terminate itself
// even though there is memory not
// cleared.
void free(void *ptr) {
    int *ptr = (int *)ptr;
    int len;

    ptr--;
    len = *ptr;

    munmap((void *)ptr, len);
}
