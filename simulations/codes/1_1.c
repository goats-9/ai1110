#include <stdio.h>
#include <stdlib.h>
#include "1_1.h"

int  main(void) //main function begins
{

//Sample size
int sz = 1000000;

//Uniform random numbers
uniform("../data/uni.dat", sz);

//Gaussian random numbers
gaussian("../data/gau.dat", 1, sz);

//Triangular random numbers
triangular("../data/tri.dat", sz);
//Mean of uniform
//printf("%lf",mean("uni.dat"));

//5*Bernoulli + Gaussian
bernoulli("../data/ber.dat", sz);
double **b = loadtxt("../data/ber.dat", sz, 1);
double **g = loadtxt("../data/gau.dat", sz, 1);
FILE *fp = fopen("../data/ber_gau.dat", "w");
for (int i = 0; i < sz; i++) { 
fprintf(fp, "%lf\n", 5*b[i][0] + g[i][0]);
}
fclose(fp);

//Chi-squared random numbers
chi2("../data/chi.dat", sz);

//Rayleigh random numbers
ral("../data/ral.dat", 2, sz);

//Rayleigh*Bernoulli + Gaussian
//Generate files for Rayleigh Distribution
//with 0 <= gamma <= 10
for (int i = 1; i < 11; i++) { 
	char file[19] = "../data/ral_xy.dat";
	file[13] = (i%10) + '0';
	file[12] = (i/10) + '0';
	ral(file, i, sz);
}
return 0;
}
