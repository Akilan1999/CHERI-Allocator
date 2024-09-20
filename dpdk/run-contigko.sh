# # pull changes
# git pull origin main

# remove freebsd build directory to force build
rm -rf /home/akilan/Alloc-Test/Allocator/dpdk/build-hybrid/kernel/freebsd

# build the changes
ninja -j4 -C build-hybrid

# remove previous contig kernel module running
sudo kldunload contigmem.ko

# entering directory of the contig build .ko files
cd /home/akilan/Alloc-Test/Allocator/dpdk/build-hybrid/kernel/freebsd

# Copyping files to /boot/modules
sudo cp contigmem.ko /boot/modules/

# Run the new contig kernel module
sudo kldload /boot/modules/contigmem.ko

# # Get back to the DPDK directory
# cd /home/akilan/CHERI-Allocator/dpdk

# # Run HelloWorld
# sudo ./build-hybrid/examples/dpdk-helloworld

# Show the dmesg to see the debug prints
# sudo dmesg

