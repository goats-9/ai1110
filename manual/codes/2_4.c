#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

double getVar(double **smpl, int sz, double m) { 
double var = 0;
for (int i = 0; i < sz; i++) 
{
smpl[i][0] = pow((smpl[i][0] - m),2);
var += smpl[i][0];
}
var /= sz;
return var;
}

int  main(void) //main function begins
{
 
//Mean of uniform
double m=mean("gau.dat");
double **smpl=loadtxt("gau.dat", 100000, 1);
printf("Mean: %lf\n",m);
int sz = 1000000;
printf("Variance: %lf\n",getVar(smpl, sz, m));
return 0;
}
