git pull origin main
cc -g -Wall -o test.out -mabi=purecap-benchmark GetInfo.c -v
./test.out
