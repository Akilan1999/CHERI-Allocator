git pull origin main
cc -g -Wall -o histogram-pthread.out -mabi=purecap-benchmark -lpthread histogram-pthread.c

# Run multiple PMCStat paramters
sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/small.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/small.bmp

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/med.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/med.bmp

sudo pmcstat -d -w 1 -p ll_cache_miss_rd ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -p DTLB_WALK ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -p L1D_TLB_RD ./histogram-pthread.out histogram_datafiles/large.bmp
sudo pmcstat -d -w 1 -p L2D_TLB ./histogram-pthread.out histogram_datafiles/large.bmp