#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    printf("How tall is the half-pyramid? ");
   // int height = get_int();
    do 
    {
        height = get_int();
    }
    while (height > 23 || height < 0);
    char block[] = "#";
    char space[] = " ";
    int blocks = 1;
    int spaces = height;

    for (int i = height; i > 0; i--){ // levels of pyramid
 
        for (int k = 1; k < spaces; k++){ // spaces per level
             printf("%c", *space);
        }
 
        for (int j = 0; j < blocks + 1; j++){ // blocks per level
             printf("%c", *block);
        }

        blocks++;
        spaces--;
        printf("\n");
    }

}