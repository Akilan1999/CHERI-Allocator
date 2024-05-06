git pull origin main
cc -g -Wall -o histogram-pthread.out -mabi=purecap-benchmark -lpthread histogram-pthread.c

# Run multiple PMCStat paramters
sudo pmcstat -d -w 1 -O ll_cache_miss_rd_histogram_small.txt -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_small.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -O DTLB_WALK_histogram_small.txt -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -O L1D_TLB_RD_histogram_small.txt -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_small.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp

sudo pmcstat -d -w 1 -O ll_cache_miss_rd_histogram_med.txt -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_med.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -O DTLB_WALK_histogram_med.txt -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -O L1D_TLB_RD_histogram_med.txt -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_med.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp

sudo pmcstat -d -w 1 -O ll_cache_miss_rd_histogram_large.txt -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_large.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -O DTLB_WALK_histogram_large.txt -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -O L1D_TLB_RD_histogram_large.txt -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -O L2D_TLB_histogram_large.txt -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp