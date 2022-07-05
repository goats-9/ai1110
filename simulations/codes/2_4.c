#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "1_1.h"

int  main(void) //main function begins
{
char *str = "../data/gau.dat";
printf("Mean: %lf\nVariance: %lf\n",mean(str), variance(str));
return 0;
}
