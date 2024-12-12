#===============================================================================
# User Options
#===============================================================================

# Compiler can be set below, or via environment variable
CC    = cc
OPTIMIZE    = yes
OPENMP      = no
DEBUG       = yes
PROFILE     = no
MPI         = no
AML         = no

#===============================================================================
# Program name & source code list
#===============================================================================

program = XSBench

source = \
Main.c \
io.c \
Simulations.c \
GridInit.c \
XSutils.c \
Materials.c

obj = $(source:.c=.o)

#===============================================================================
# Sets Flags
#===============================================================================

# Standard Flags

# Linker Flags
LDFLAGS = -lm

# LLVM Compiler
# ifneq (,$(findstring clang,$(CC)))
#   CFLAGS += -flto
#   ifeq ($(OPENMP),yes)
# 	CFLAGS += -fopenmp -DOPENMP
#   endif
# endif

# # Intel Compiler
# ifneq (,$(findstring intel,$(CC)))
#   CFLAGS += -ipo
#   ifeq ($(OPENMP),yes)
# 	CFLAGS += -fopenmp -DOPENMP
#   endif
# endif

# # Debug Flags
# ifeq ($(DEBUG),yes)
#   CFLAGS += -g
#   LDFLAGS  += -g
# endif

# Profiling Flags

# Optimization Flags

# AML

CFLAGS += -g -Wall -mabi=purecap-benchmark -lpthread

#===============================================================================
# Targets to Build
#===============================================================================

$(program): $(obj) XSbench_header.h Makefile
	$(CC) $(CFLAGS) $(obj) -o $@ $(LDFLAGS)

%.o: %.c XSbench_header.h Makefile
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(program) $(obj)

edit:
	vim -p $(source) XSbench_header.h

run:
	./$(program)
