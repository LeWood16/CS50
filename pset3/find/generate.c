/**
 * generate.c
 *
 * Generates pseudorandom numbers in [0,MAX), one per line.
 *
 * Usage: generate n [s]
 *
 * where n is number of pseudorandom numbers to print
 * and s is an optional seed
 */
 
#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// upper limit on range of integers that can be generated
#define LIMIT 65536

int main(int argc, string argv[])
{
    // if the number of arguments entered in aren't two or three,
    if (argc != 2 && argc != 3)
    {
        printf("Usage: ./generate n [s]\n");
        return 1;
    }

    // convert the n argument entered in (a string) to an integer;
    int n = atoi(argv[1]);

    // if there are three arguments (i.e. the program name, the n, and the [s]), generate pseudorandom numbers via the seed argument;
    if (argc == 3)
    {
        srand48((long) atoi(argv[2]));
    }
    else
    {
        srand48((long) time(NULL));
    }

    // generate not-negative double-precision floating-point values, one until n is reached
    for (int i = 0; i < n; i++)
    {
        printf("%i\n", (int) (drand48() * LIMIT));
    }

    // success
    return 0;
}
