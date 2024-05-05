git pull origin main
cc -g -Wall -o matrix_multiply.out -mabi=purecap-benchmark -lpthread matrix_multiply.c
sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply.out
