cc -g -Wall -Wextra -lstatic -Wno-unused-parameter -mabi=purecap-benchmark -c allocator.c -o alloc.o
ar rcs alloc.a alloc.o
# cc -O3 -g -W -Wall -Wextra -Wno-unused-parameter -shared -fPIC -o alloc.so 
cp alloc.o ../benchmarks/kmeans/
cp alloc.a ../benchmarks/kmeans/
cp alloc.o /home/akilan/Alloc-Test/cheri_malloc_blog
cp alloc.a /home/akilan/Alloc-Test/cheri_malloc_blog