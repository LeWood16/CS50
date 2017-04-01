#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    printf("How much change is due? ");
    do 
    {
        change = get_float();
    }
    while (change < 0);
    
    
    
    int count;
    count = 0;
    
    while (change > 0){
        if (change % 25 == 0){ // if all change can be in quarters, 
            count++;
            change = change - 25;
        } else if (change % 10 == 0){
            count++;
            change = change - 10;
        } else if (change % 5 == 0){
            count++;
            change = change - 5;
        } else if (change % 1 == 0){
            count++;
            change = change - 1;
        }
        
    }
    
    
    if (count == 1){
       printf("%i coin is given back as change.\n", count);
    } else {
       printf("%i coins are given back as change.\n", count);
    }
    
}