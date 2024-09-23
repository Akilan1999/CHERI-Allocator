# # pull changes
# git pull origin main

# remove freebsd build directory to force build
rm -rf /home/akilan/Alloc-Test/Allocator/dpdk/build-hybrid/kernel/freebsd

export PKG_CONFIG_PATH=`pwd`/config/hybrid

# sudo CC=clang meson -Dexamples=helloworld -Denable_kmods=true build-hybrid

# build the changes
sudo ninja -j4 -C build-hybrid

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

