git pull origin main
rm build-hybrid/examples/dpdk-helloworld
ninja -j4 -C build-hybrid
sudo ./build-hybrid/examples/dpdk-helloworld
