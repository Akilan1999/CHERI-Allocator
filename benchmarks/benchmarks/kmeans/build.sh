git pull origin main
cc -g -Wall -o kmeans-pthread.out -mabi=purecap-benchmark -lpthread kmeans-pthread.c
sudo pmcstat -d -w 1 -p L2D_TLB ./kmeans-pthread.out
