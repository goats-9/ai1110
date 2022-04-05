#include <stdio.h>
#include <math.h>
// Use -lm flag when compiling

int main() {
    int x = 1;
    if (3*atan(x) + atan(1/x) == M_PI) printf("The solution x = %d is correct.\n", x);
    else printf("The solution x = %d is incorrect.\n", x);
    return 0;
}