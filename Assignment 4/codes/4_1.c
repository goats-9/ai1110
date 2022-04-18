#include <stdio.h>

int main() {
    int n = 1000;
    int e = 455;
    int f = 545;
    double pr_e = (1.0)*e/n;  // for type conversion
    double pr_f = (1.0)*f/n;
    printf("The probability of getting heads is %.3f.\nThe probability of getting tails is %.3f.\nThe sum of these two probabilities is %.3f.", pr_e, pr_f, pr_e + pr_f);
    return 0;
}