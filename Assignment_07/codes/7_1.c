/*
Code by Gautam Singh
April 25, 2022
License
https://www.gnu.org/licenses/gpl-3.0.en.html
CFLAGS=-Wall -g -lm -O2
*/

#include <stdio.h>
#include <math.h>

int main() {
    double e = 10e-6;   // Limit of float precision
    double pr_a = 6.0/11, pr_b = 5.0/11, pr_aub = 7.0/11;
    double pr_anb = pr_a + pr_b - pr_aub, pr_a_b = pr_anb/pr_b, pr_b_a = pr_anb/pr_a;
    if (abs(pr_anb - 4.0/11) < e) printf("Solution to part (i) verified.\n");
    if (abs(pr_a_b - 4.0/5) < e) printf("Solution to part (ii) verified.\n");
    if (abs(pr_b_a - 2.0/3) < e) printf("Solution to part (iii) verified.\n");
    return 0;
}