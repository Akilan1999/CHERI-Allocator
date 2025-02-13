// Quick malloc implementation with mmap
// void* malloc(size_t sz)
// {
//    sz = __builtin_align_up(sz, _Alignof(max_align_t));
//    MallocCounter -= sz;
//    void *ptrLink = &ptr[MallocCounter];
//    ptrLink = cheri_setbounds(ptrLink, sz);

//    return ptrLink;
// }

// // Quick cheri free implementation
// void free(void *ptr) { 
//    int len = cheri_getlen(ptr);
//    munmap(ptr, len);
// }

// Init_alloc(void) {
//    size_t sz;
//    // Pre Allocate 400 MB 
//    sz = 1073741824;

//    fd = shm_create_largepage(SHM_ANON, O_CREAT | O_RDWR, 1, SHM_LARGEPAGE_ALLOC_DEFAULT, 0);

//     ptr = mmap(NULL, sz,
//     PROT_READ|PROT_WRITE, MAP_SHARED,fd,0);

//     MallocCounter = (int)sz;
// }

FUNCTION malloc(sz):
    sz = ALIGN_UP(sz, MAX_ALIGNMENT)  // Align size to max alignment
    MallocCounter = MallocCounter - sz  // Update remaining memory
    ptrLink = &ptr[MallocCounter]  // Calculate pointer address
    ptrLink = SET_BOUNDS(ptrLink, sz)  // Set bounds for memory safety and to track the length of the pointer
    RETURN ptrLink  // Return allocated memory pointer

FUNCTION free(ptr):
    len = GET_LENGTH(ptr)  // Get length of memory block from the defined bounds
    UNMAP(ptr, len)  // Release memory block

FUNCTION Init_alloc():
    sz = 1 GB // Define pre-allocated memory size
    fd = CREATE_LARGE_PAGE_MEMORY(sz)  // Create shared memory
    ptr = MAP_MEMORY(sz)  // Map memory region
    MallocCounter = sz  // Initialize memory counter
