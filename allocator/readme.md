# Convention for benchmarking various allocators
We demonstrate the standard emitters each C memory allocator should follow to standardize the code being benchmarked. 

There are 3 factors on the design for benchmarking these C programs:
- Standard interface to test various memory allocators.
- Automating the extracting of various performance counters. 
- Parsing and analyzing the various benchmark metrics extracted. 

## Standard interface to test various memory allocators
The interface goes as the following:
- ```Malloc```, ```Free``` and ``ìnit_alloc``.
- The folder structure is as follows: 
```
- <Allocator name>
   - HugePages 
   - Original
   - README (Explaining the Allocator design with the source of the allocator)
```
- The linkage of the C program should consist either of a shared object file 
which is preferred. Or with a header file which can compile the appropriate 
file at compile. 
   - [x] To write a script to compile and link shared object files.
   - [ ] Automate generating header files.

## Automating the extracting of various performance counters and Parsing and analyzing the various benchmark metrics extracted.
The extraction library to generate the decided performance counters is implemented. 
ARM unclear documentation from the A profile manual gives a unclear picture of 
exactly what the performance counters do. The script to extract it and to generate graphs
is completely isolated. This makes process from running to generating the end graphs 
pretty tedious. 

### Steps to resolve this: 
- [ ] To build runners that runs with different memory allocators and the wall clock 
and metrics in semantically comparable file which is followed as a basic standard. 
This means.
```
Ex: 
 - performance-benchmark.stat
 - performance-huge-benchmark.stat
```
- [ ] Extract results to a certain folder and then immediate run python program to generate the graphs.
- [ ] Numeric values represented as a table. 
- [ ] Generate graphs in semantically readable folder structure. 
- [ ] Save generated data which can be loaded as graphs. 


