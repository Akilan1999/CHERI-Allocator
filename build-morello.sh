# Building shared object files for morello

cc -shared -march=purecap-benchmark -fPIC alloc.c -o alloc.so
cc -shared -march=purecap-benchmark -fPIC alloc.c -o regularalloc.so


