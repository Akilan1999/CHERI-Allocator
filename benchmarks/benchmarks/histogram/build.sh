git pull origin main
cc -g -Wall -o histogram-pthread.out -mabi=purecap-benchmark -lpthread histogram-pthread.c

# Run multiple PMCStat paramters
sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/small.bmp -o ll_cache_miss_rd_histogram_small.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp -o L2D_TLB_histogram_small.txt
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/small.bmp -o DTLB_WALK_histogram_small.txt
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/small.bmp -o L1D_TLB_RD_histogram_small.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp -o L2D_TLB_histogram_small.txt

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/med.bmp -o ll_cache_miss_rd_histogram_med.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp -o L2D_TLB_histogram_med.txt
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/med.bmp -o DTLB_WALK_histogram_med.txt
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/med.bmp -o L1D_TLB_RD_histogram_med.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp -o L2D_TLB_histogram_med.txt

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/large.bmp -o ll_cache_miss_rd_histogram_large.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp -o L2D_TLB_histogram_large.txt
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/large.bmp -o DTLB_WALK_histogram_large.txt
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/large.bmp -o L1D_TLB_RD_histogram_large.txt
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp -o L2D_TLB_histogram_large.txt