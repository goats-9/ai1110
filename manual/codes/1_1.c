#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "1_1.h"

int  main(void) //main function begins
{

//Sample size
int sz = 1000000;

//Uniform random numbers
uniform("uni.dat", sz);

//Gaussian random numbers
gaussian("gau.dat", 1, sz);

//Triangular random numbers
triangular("tri.dat", sz);
//Mean of uniform
//printf("%lf",mean("uni.dat"));

//5*Bernoulli + Gaussian
bernoulli("ber.dat", 1000);
gaussian("gau_noise.dat", 1, 1000);

//Chi-squared random numbers
chi2("chi.dat", sz);

//Rayleigh random numbers
ral("ral.dat", 1, sz);

//Rayleigh*Bernoulli + Gaussian
//Generate files for Rayleigh Distribution
//with 0 <= gamma <= 10
bernoulli("ber_new.dat", sz);
for (int i = 1; i < 11; i++) { 
	char file[11] = "ral_xy.dat";
	file[5] = (i%10) + '0';
	file[4] = (i/10) + '0';
	ral(file, i, sz);
}
return 0;
}
