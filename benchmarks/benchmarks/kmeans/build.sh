git pull origin main
cc -g -Wall -o kmeans-pthread.out -mabi=purecap-benchmark -lpthread kmeans-pthread.c
sudo pmcstat -d -w 5 -p l1d_tlb_rd ./kmeans-pthread.out
