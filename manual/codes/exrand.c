#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{

//Sample size
int sz = 1000000;

//Uniform random numbers
uniform("uni.dat", sz);

//Gaussian random numbers
gaussian("gau.dat", sz);

//Triangular random numbers
triangular("tri.dat", sz);
//Mean of uniform
//printf("%lf",mean("uni.dat"));

//5*Bernoulli + Gaussian
bernoulli("ber.dat", 1000);
gaussian("gau_noise.dat", 1000);
double **x = loadtxt("ber.dat", 1000, 1);
double **n = loadtxt("gau_noise.dat", 1000, 1);
FILE *fp = fopen("ber_gau.dat", "w");
for (int i = 0; i < 1000; i++) {
fprintf(fp, "%lf\n", 5*x[i][0] + n[i][0]);
} 
//Remove intermediate files
//remove("ber.dat");
//remove("gau_noise.dat");
fclose(fp);
return 0;
}
