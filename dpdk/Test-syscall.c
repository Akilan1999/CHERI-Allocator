#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>

struct syscall_alloc {
	int                       size;
    int                       malloc;
    // void                      *addr;
};


int
main(int argc, char *argv[])
{
	    struct syscall_alloc st;
	    st.size = 7;
	    //st.addr = NULL;
        st.malloc = 1;

        
        

        // struct syscall_alloc *ref = &st;

        printf("Malloc called \n");


        int tid;
	    tid = syscall(210,st);

         printf("resp %d \n", tid);

        // struct proc * process = pfind(tid);

        

        printf("size %lu \n", st.size);



	    // struct syscall_alloc st1;
	    //st1.size = 2;
	    //st1.addr = st.addr;
	    // st.Malloc = 0;


	    // tid = syscall(210, st1);
            // tid = syscall(SYS_tgkill, getpid(), tid);
}
// // Define the new variable type which is a struct.
// // This definition must be visible to any function that is accessing the
// // members of a variable of this type.
// struct some_struct {
//     unsigned int total;
// };

// /*
//  * Modifies the struct that exists in the calling function.
//  *   Function test() takes a pointer to a struct some_struct variable
//  *   so that any modifications to the variable made in the function test()
//  *   will be to the variable pointed to.
//  *   A pointer contains the address of a variable and is not the variable iteself.
//  *   This allows the function test() to modify the variable provided by the
//  *   caller of test() rather than a local copy.
//  */
// int test(struct some_struct *state) {
//     state->total = 4;
//     return 0;
// }

// /* 
//  * Modifies the local copy of the struct, the original
//  * in the calling function is not modified.
//  * The C compiler will make a copy of the variable provided by the
//  * caller of function test2() and so any changes that test2() makes
//  * to the argument will be discarded since test2() is working with a
//  * copy of the caller's variable and not the actual variable.
//  */
// int test2(struct some_struct state) {
//     state.total = 8;
//     return 0;
// }

// /*
//  * Make a local copy of the argument then modify the local copy.
//  * Until the assignment of the local copy to the argument is made,
//  * the changes to the local copy are not made to the argument.
//  * To make any changes made to the local copy in the argument,
//  * you need to assign the local copy to the argument.
//  */
// int test3(struct some_struct *state) {
//     struct some_struct state_copy;
//     state_copy = *state;    // make a local copy of the struct
//     state_copy.total = 12;  // modify the local copy of the struct
//     *state = state_copy;    /* assign the local copy back to the original in the
//                               calling function. Assigning by dereferencing pointer. */
//     return 0;
// }

// int main () {
//     struct some_struct s;

//     /* Set the value then call a function that will change the value. */
//     s.total = 5;
//     test(&s);
//     printf("after test(): s.total = %d\n", s.total);

//     /*
//      * Set the value then call a function that will change its local copy 
//      * but not this one.
//      */
//     s.total = 5;
//     test2(s);
//     printf("after test2(): s.total = %d\n", s.total);

//     /* 
//      * Call a function that will make a copy, change the copy,
//        then put the copy into this one.
//      */
//     test3(&s);
//     printf("after test3(): s.total = %d\n", s.total);

//     return 0;
// }