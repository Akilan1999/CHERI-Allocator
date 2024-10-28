cc -g -Wall -o memaccesstest.out -mabi=purecap-benchmark -lpthread memaccesstest.c
cc -g -Wall -o loadmem.out -mabi=purecap-benchmark -lpthread loadmem.c
cc -g -Wall -o glibc-bench.out -mabi=purecap-benchmark -lpthread glibc-bench.c