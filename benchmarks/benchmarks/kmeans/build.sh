git pull origin main
cc -g -Wall -o kmeans-pthread.out -mabi=purecap-benchmark -lpthread kmeans-pthread.c
sudo pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk  ./kmeans-pthread.out
