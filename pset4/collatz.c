#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int collatz(int n);

int collatz(int n)
{
    if (n == 1)
        return 0;
    // even numbers
    else if ((n % 2) == 0)
    {
        return 1 + collatz(n / 2);
    }
    // odd numbers
    else 
        return 1 + (collatz(3*n + 1));
}


int main(int argc, string argv[])
{
    if (argc < 2 || argv[1] == NULL)
    {
        return 1;
    }

    int a = atoi(argv[1]);


    printf("num is now 1; steps taken:%i\n", collatz(a));
}