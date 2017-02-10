#ifndef DIM
#define DIM 10
#endif

#ifndef FILE_PATH
#define FILE_PATH "outMatrix.txt"
#endif


#include <stdio.h>
#include <omp.h>
#include <time.h>
#include <stdlib.h>

int main()
{
        FILE * fp = fopen(FILE_PATH,"w");
        srand( (unsigned int) time(NULL));
        int i,j;
        #pragma omp parallel for collapse(2) private(i,j)
        for(i=0; i<DIM; i++)
        {
                for(j=0; j<DIM; j++)
                {
                        int random = rand();
                        fprintf(fp, "%d\t%d\t%d\n", i,j, random);
                }
        }
	fclose(fp);
}
