git pull origin main
cc -g -Wall -o histogram-pthread.out -mabi=purecap-benchmark -lpthread histogram-pthread.c

# sudo sh build.sh

# sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-200000.txt ./kmeans-pthread.out -d 40 -c 100 -p 200000 -s 1000 > kmeans-bounds-reg-200000-out.txt
# sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-150000.txt ./kmeans-pthread.out -d 40 -c 100 -p 150000 -s 1000 > kmeans-bounds-reg-150000-out.txt
# sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-100000.txt ./kmeans-pthread.out -d 40 -c 100 -p 100000 -s 1000 > kmeans-bounds-reg-100000-out.txt
# sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-10000.txt ./kmeans-pthread.out -d 40 -c 100 -p 10000 -s 1000 > kmeans-bounds-reg-10000-out.txt
# sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-1000.txt ./kmeans-pthread.out -d 40 -c 100 -p 1000 -s 1000 > kmeans-bounds-reg-1000-out.txt

# Run multiple PMCStat paramters
sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o histogram-small-mmap.txt ./histogram-pthread.out histogram_datafiles/small.bmp > histogram-small-out-mmap.txt
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/small.bmp > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/small.bmp > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp > test.out

sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o histogram-med-mmap.txt ./histogram-pthread.out histogram_datafiles/med.bmp > histogram-med-out-mmap.txt

# sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/med.bmp > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/med.bmp > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/med.bmp > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp > test.out

sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o histogram-large-mmap.txt ./histogram-pthread.out histogram_datafiles/large.bmp > histogram-large-out-mmap.txt

# sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/large.bmp > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp > test.out
# sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/large.bmp > test.out
# sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/large.bmp > test.out
# sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp > test.out