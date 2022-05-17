#include <stdio.h>
#include <math.h>
#define eps 1e-3
// CFLAGS=-Wall -g -O2 -lm

int main() {
    double pr = pow(0.95, 10) + 10*pow(0.95, 9)*0.05, ans = 0.914;
    if (fabs(pr - ans) < eps) printf("Answer is verified.\n");   // 3 d.p. precision
    return 0;
}