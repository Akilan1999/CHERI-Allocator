/* matrix9.c - array of arrays */

/* 
   Course: Design and Analysis of Parallel Algorithms
   By:     Murray Cole, Edinburgh University
   From:   http://www.inf.ed.ac.uk/teaching/courses/dapa/overheads.pdf
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double startTime;

// showElapsed(id,m)
// int id;
// char * m;
// {  printf("%d: %s %f secs\n",id,m,(clock()-startTime)/CLOCKS_PER_SEC);
// }

int * makeVector(n)
int n;
{  return (int *)malloc(n*sizeof(int));  }

int ** makeMatrix(m,n)
int m,n;
{  int ** newm = (int **)malloc(m*sizeof(int *));
   int i;
   for(i=0;i<m;i++)
    newm[i] = makeVector(n);
   return newm;
}

readMatrix(fin,M,m,n)
FILE * fin;
int ** M;
int m,n;
{  int i,j;

   for(i=0;i<m;i++)
    for(j=0;j<n;j++)
     fscanf(fin,"%d",&(M[i][j]));
}

writeMatrix(fout,M,m,n)
FILE * fout;
int ** M;
int m,n;
{  int i,j;

   for(i=0;i<m;i++)
   {  for(j=0;j<n;j++)
       fprintf(fout,"%d ",M[i][j]);
     // putc('\n',fout);
   }
}

matrixProdCole(M1,M2,M3,m,n,z)
int **M1,**M2,**M3;
int m,n,z;
{ int i,j,k,ii,jj,kk,temp;
  int *pa, *pb;

  for (jj=0; jj<m; jj=jj+z)
    for (kk=0; kk<n; kk=kk+z)
      for (i=0; i<m; i++)
	for (j=jj; j < jj+z; j++) {
	  pa = &M1[i][kk]; pb = &M2[kk][j];
	  temp = (*pa++)*(*pb);
	  for (k=kk+1; k < kk+z; k++) {
	    pb = pb+m;
	    temp += (*pa++)*(*pb);
	  }
	  M3[i][j] += temp;
	}
}

matrixProd(M1,M2,M3,m,n)
int **M1,**M2,**M3;
int m,n;
{  int i,j,k;
   
   for(i=0;i<m;i++)
    for(j=0;j<m;j++)
    {  M3[i][j]=0;
       for(k=0;k<n;k++)
        M3[i][j] = M3[i][j]+M1[i][k]*M2[k][j];
    }
}

main(argc,argv)
int argc;
char ** argv;
{  FILE * fin;
   FILE * fout;
   int ** m1;
   int ** m2;
   int ** m3;
   int m,n;
   double startT,stopT;

   fin = fopen(argv[1],"r");
   fscanf(fin,"%d %d",&m,&n);
   m1 = makeMatrix(m,n);
   readMatrix(fin,m1,m,n);
   m2 = makeMatrix(n,m);
   readMatrix(fin,m2,n,m);
   fclose(fin);
   //writeMatrix(stdout,m1,m,n);
   //putchar('\n');
   //writeMatrix(stdout,m2,n,m);
   //putchar('\n');
   m3 = makeMatrix(m,m);
   startT = clock();
   // matrixProd(m1,m2,m3,m,n);
   matrixProdCole(m1,m2,m3,m,n,10);
   stopT = clock();
   printf("%d * %d; SEQUENTIAL; %f secs\n",
	  m,n, (stopT-startT)/CLOCKS_PER_SEC);
   //writeMatrix(stdout,m3,m,m);
   fout = fopen("MRESULT_SEQ9","w");
   writeMatrix(fout,m3,m,m);
   fclose(fout);
}