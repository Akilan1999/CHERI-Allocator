# Building shared object files for morello

cc -g -Wall -shared -mabi=purecap-benchmark -fPIC alloc.c -o alloc.so
cc -g -Wall -shared -mabi=purecap-benchmark -fPIC alloc.c -o regularalloc.so


