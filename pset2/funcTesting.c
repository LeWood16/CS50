#include <stdio.h>
#include <cs50.h>
#include <string.h>


    float multiply_two_reals(float a, float b);
    
    float multiply_two_reals(float a, float b)
    {
        return a * b;
    }

    int add_two_ints(int c, int d);
    
        int add_two_ints(c, d)
    {
        return c + d;
    }


int main(void)
{
        printf("double one: ");
        float a = GetFloat();

       printf("double twp: ");
        float b = GetFloat();


    
    float c = multiply_two_reals(a, b);

    printf("result of multiplying %f and %f is %f\n", a, b, c);
    
    
}