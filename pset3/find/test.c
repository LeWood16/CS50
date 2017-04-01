#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>




int main(void)
{
    char arr[11] = {3, 2, 1, 5, 7, 8, 13, 20, 24, 42, 6};
    int i;
    int n = 11;
    int m = n - (n/2);

    for (i = 0; i < n; i++){
        for (int j = 1; j < n; j++){
            if (arr[j-1] > arr[j]){ // start at the 1th index, and compare it to the 0th;
                int a = arr[j];
                int b = arr[j-1];
                arr[j] = b;
                arr[j-1] = a;
            }  else {
                continue;
            }
        }
    }


    printf("middle of %i: %i\n", n, m);
}