#include <stdio.h>
#include <math.h>

int main(){
    double n = 3.14159;
    double R;
    scanf("%lf", &R);
    double A = n * pow(R, 2);

    printf("A=%.4lf\n", A);
    return 0;
}