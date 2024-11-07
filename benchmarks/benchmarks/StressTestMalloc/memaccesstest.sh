sh build.sh
time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -p ll_cache_miss_rd -o memaccesstest-cheri.stat ./memaccesstest.out