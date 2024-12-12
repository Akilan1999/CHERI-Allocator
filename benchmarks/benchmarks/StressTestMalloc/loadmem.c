#include <stdio.h>
#include <stdlib.h>
#include "malloc.h"

// #define malloc      MALLOCCHERI
// #define free        FREECHERI

// performing various sizes of mallocs are free
void
bench (unsigned long n) {
    int *ptr;
    unsigned long i;
    // printf("Enter number of int(4 byte) you want to allocate:");
 
    printf("Allocating %lu bytes......\n",n*sizeof(int));
    ptr=(int*)malloc(n*sizeof(int));
    if (ptr==NULL){
        printf("ERROR!Memory not allocated!");
        exit(0);
    }
    printf("Filling int into memory.....\n");
    for (i = 0; i < n; i++){
        ptr[i] = 1;
    }
    // printf("Sleep 10 seconds......\n");
    // sleep(10);
    // printf("Free memory.\n");
    free(ptr);
}

int main(){

//  INITREGULARALLOC();
//  bench(8);
//  bench(30);
//  bench(100);
//  bench(600);
// Run one by one
 bench(10);
 bench(100);
 bench(1000);
 bench(10000);
 bench(100000);

//  int *ptr;
//  unsigned long i,n;
//  printf("Enter number of int(4 byte) you want to allocate:");
//  scanf("%lu",&n);
 
//  printf("Allocating %lu bytes......\n",n*sizeof(int));
//  ptr=(int*)malloc(n*sizeof(int));
//  if (ptr==NULL){
//    printf("ERROR!Memory not allocated!");
//    exit(0);
//  }
//  printf("Filling int into memory.....\n");
//  for (i = 0; i < n; i++){
//     ptr[i] = 1;
//  }
//  printf("Sleep 10 seconds......\n");
//  sleep(10);
//  printf("Free memory.\n");
//  free(ptr);
//  return 0;
}