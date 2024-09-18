akilan@cheribsd:~/CHERI-Allocator/dpdk $ cat run-contigko.sh
# pull changes
git pull origin main

# remove freebsd build directory to force build
rm -rf /home/akilan/CHERI-Allocator/dpdk/build-hybrid/kernel/freebsd

# build the changes
ninja -j4 -C build-hybrid

# remove previous contig kernel module running
sudo kldunload Malloc.ko

# entering directory of the contig build .ko files
cd /home/akilan/CHERI-Allocator/dpdk/build-hybrid/kernel/freebsd

# Copyping files to /boot/modules
sudo cp Malloc.ko /boot/modules/

# Run the new syscall kernel module
sudo kldload /boot/modules/Malloc.ko

# cd into
cd /home/akilan/CHERI-Allocator/dpdk

cc Test-syscall.c -o syscall.out

sudo ./syscall.out


# Show the dmesg to see the debug prints
# sudo dmesg
