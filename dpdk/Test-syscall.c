#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>

struct syscall_alloc {
	unsigned long             size;
    int                      malloc;
    // void                      *addr;
};


int
main(int argc, char *argv[])
{
	    struct syscall_alloc st;
	    st.size = 2;
	    //st.addr = NULL;
        st.Malloc = 1;

        printf("Malloc called");

	    syscall(210,st);

	    // struct syscall_alloc st1;
	    //st1.size = 2;
	    //st1.addr = st.addr;
	    // st.Malloc = 0;


	    // tid = syscall(210, st1);
            // tid = syscall(SYS_tgkill, getpid(), tid);
}