sudo sh build.sh

sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-200000.txt ./kmeans-pthread.out -d 40 -c 100 -p 200000 -s 1000 > kmeans-bounds-reg-200000-out.txt
sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-150000.txt ./kmeans-pthread.out -d 40 -c 100 -p 150000 -s 1000 > kmeans-bounds-reg-150000-out.txt
sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-100000.txt ./kmeans-pthread.out -d 40 -c 100 -p 100000 -s 1000 > kmeans-bounds-reg-100000-out.txt
sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-10000.txt ./kmeans-pthread.out -d 40 -c 100 -p 10000 -s 1000 > kmeans-bounds-reg-10000-out.txt
sudo time pmcstat -d -w 1 -p l1d_tlb_rd -p l2d_tlb_rd -p l1d_tlb_refill -p cpu_cycles -p dtlb_walk -p stall_backend -o kmeans-reg-alloc-1000.txt ./kmeans-pthread.out -d 40 -c 100 -p 1000 -s 1000 > kmeans-bounds-reg-1000-out.txt