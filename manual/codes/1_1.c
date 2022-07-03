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
bernoulli("../data/ber.dat", 1000);
gaussian("../data/gau_noise.dat", 1, 1000);

//Chi-squared random numbers
chi2("../data/chi.dat", sz);

//Rayleigh random numbers
ral("../data/ral.dat", 1, sz);

//Rayleigh*Bernoulli + Gaussian
//Generate files for Rayleigh Distribution
//with 0 <= gamma <= 10
bernoulli("../data/ber_new.dat", sz);
for (int i = 1; i < 11; i++) { 
	char file[18] = "../data/ral_xy.dat";
	file[13] = (i%10) + '0';
	file[12] = (i/10) + '0';
	ral(file, i, sz);
}
return 0;
}
