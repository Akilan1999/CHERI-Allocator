# git pull orgin main
cc -g -Wall -o matrix_multiply-pthread.out -mabi=purecap-benchmark -lpthread matrix_multiply-pthread.c

time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o matrix_multiply_regular_200.txt ./matrix_multiply-pthread.out 200 -create_files > matrix_multiply_200_regular_out.txt
# Run multiple PMCStat paramters
# sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 200 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 200 -create_files > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 200 -create_files > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 200 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 200 -create_files > test.out

time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o matrix_multiply_regular_1000.txt ./matrix_multiply-pthread.out 1000 -create_files > matrix_multiply_1000_regular_out.txt

time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o matrix_multiply_regular_3000.txt ./matrix_multiply-pthread.out 3000 -create_files > matrix_multiply_3000_regular_out.txt

# sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 1000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 1000 -create_files > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 1000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 1000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 1000 -create_files > test.out

# sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./matrix_multiply-pthread.out 5000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 5000 -create_files > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./matrix_multiply-pthread.out 5000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./matrix_multiply-pthread.out 5000 -create_files > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./matrix_multiply-pthread.out 5000 -create_files > test.out
