#include <stdio.h>
#include <math.h>
#define eps 1e-6
// CFLAGS=-Wall -g -O2 -lm

int main() {
    double pr_e = 0.4;
    double pr_f = 0.6;
    double pr_ef = 0.2;
    double pr_a = 1 - pr_ef;
    double pr_b = pr_ef/pr_f;
    double pr_c = pr_ef/pr_e;
    if (pr_a == 0.8) printf("Answer to (a) verified.\n");
    if (abs(pr_b - 1.0/3) < eps) printf("Answer to (b) verified.\n");   // Float precision
    if (pr_c == 0.5) printf("Answer to (c) verified.\n");
    return 0;
}