cc -g -Wall -shared -o malloc-huge.so -mabi=purecap-benchmark -lpthread HugePage/bitmap_alloc.c
cc -g -Wall -shared -o malloc-regular.so -mabi=purecap-benchmark -lpthread Regular/bitmap_alloc.c