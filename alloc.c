#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

#include <dlfcn.h>
#include <sys/fcntl.h>
#include <sys/stat.h>

#define FILENAME "/dev/contigmem"

//static char *heap_start;
//static char *heap;
//static size_t HEAP_SIZE = 1024 * 1024 * 1024;

void *malloc(size_t sz) {
    printf("here");
    int fd = open
            (FILENAME, O_RDWR | O_CREAT, 0600);
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

    int *ptr = mmap(NULL, sz,
                    PROT_READ | PROT_WRITE, MAP_SHARED,
                    fd, offset);
    if(ptr == MAP_FAILED)
    {
        perror("mmap");
        exit(EXIT_FAILURE);
    }

    int len = sz + sizeof(sz);

    *ptr = len;

    // To probably set exact bounds on it
    return (void *)(&ptr[1]);
}

// Currently not implementing free
// This is to ensure the PureCap
// program can terminate itself
// even though there is memory not
// cleared.
void free(void *ptr) { }

// void *realloc(void *ptr, size_t sz) {
//  void *new_ptr = malloc(sz);
//  if (ptr && new_ptr) memmove(new_ptr, ptr, sz);
//  return new_ptr;
//}
