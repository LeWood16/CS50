/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>


#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // TODO: implement a searching algorithm
    
    
    if (n < 0){ // if negative length of array. return false;
        return false;
    }
    
    int m = n/2;// find the middle;
    
    while(n > 0){ // while there is still an array to search,
        if (values[m] == value){ // if the middle is the value, return true;
            return true;
        } else if (value < values[m]){ // if the middle value is higher than what we're looking for
            n = m;
            m = m/2;
            // search lower (left);
        } else if (value > values[m]){ // if the middle value is lowers than what we're looking for
            n = m;
            m = m + m/2;
            // search higher (right);
        } else {
            return false;
        }
    }
}

/**
 * Sorts array of n values.
 */
 
void sort(int values[], int n)
{
    // bubble sort, make from scratch :D
    for (int i = 0; i < n; i++){          // for each element in the array,
        for (int j = 1; j < n; j++){      // run through this comparison test n times (i.e. this for loop runs n^2 times)
            if (values[j-1] > values[j]){ // if the previous value is greater than the current one,
                int a = values[j];
                int b = values[j-1];
                values[j] = b;
                values[j-1] = a;       // swap them;
            }  else {
                continue;              // otherwise go to the next step in the algorithm;
            }
        }
    }
    // TODO: implement an O(n^2) sorting algorithm
    return;
}


