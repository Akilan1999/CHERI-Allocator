cc -g -Wall -shared -o malloc-huge.so -mabi=purecap-benchmark -lpthread HugePage/bump_alloc.c
cc -g -Wall -shared -o malloc-regular.so -mabi=purecap-benchmark -lpthread Regular/bump_alloc.c