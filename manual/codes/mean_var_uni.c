#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Mean of uniform
double m=mean("uni.dat");
printf("Mean: %lf\n",m);
int sz = 1000000;
double **smpl=loadtxt("uni.dat", 1000000, 1);
double var = 0;
for (int i = 0; i < sz; i++) 
{
smpl[i][0] = pow((smpl[i][0] - m),2);
var += smpl[i][0];
}
var /= sz;
printf("Variance: %lf\n",var);
return 0;
}
