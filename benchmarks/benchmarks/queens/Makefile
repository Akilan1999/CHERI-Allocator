CC = cc
BINARY = ./nqueens
CFLAGS += -Wall -g -mabi=purecap-benchmark

all: clean compile clear run

run:
	# run and test input file
	$(BINARY)

clean:
	rm *.o

clear:
	clear

compile: nqueens.o
	$(CC) $(CFLAGS) -o $(BINARY) nqueens.o

nqueens.o:
	# Ultra fast compilation
	$(CC) $(CFLAGS) -c -O3 ./nqueens.c
