git pull orgin main
cc -g -Wall -o matrix_multiply-pthread.out -mabi=purecap-benchmark -lpthread matrix_multiply-pthread.c


# Run multiple PMCStat paramters
sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 200 -create_files > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 200 -create_files > test.out
sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 200 -create_files > test.out
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 200 -create_files > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 200 -create_files > test.out

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 1000 -create_files > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 1000 -create_files > test.out
sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 1000 -create_files > test.out
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 1000 -create_files > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 1000 -create_files > test.out

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 5000 > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 5000 > test.out
sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 5000 > test.out
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 5000 > test.out
sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 5000 > test.out
