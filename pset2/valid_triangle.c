#include <stdio.h>
#include <cs50.h>
#include <string.h>


    bool valid_triangle(float a, float b, float c);
    
    bool valid_triangle(float a, float b, float c)
    {
        if (a <=0 || b <=0 || c<=0){ // if any side is zero or negative, return false;
            return false;
        }
        
        // check that the sum of any two sides are greater than the third
        
        if (a + b <= c || b + c <= a || a + c <= b){
            return false;
        }
        
        
        // if both of these are passed, the sides can make up a valid triangle
        return true;
    }




int main(void)
{
        
    float a;
    float b;
    float c;
    printf("side one:\n");
    a = get_float();
    printf("side two:\n");
    b = get_float();    
    printf("side three:\n");
    c = get_float();    
    
    bool answer;
    answer = valid_triangle(a, b, c);
    if (answer == true){
        printf("Sides make a valid triangle!\n");
    } else {
        printf("Sides cannot make a valid triangle.\n");
    }
}