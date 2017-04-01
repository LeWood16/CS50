#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("How many minutes for your shower? :");
    int minutes = get_int();
    int bottles;
    bottles = minutes * 1.5 * 128 / 16;
    printf("Bottles of water equivalent for your shower:  %i\n", bottles);
}