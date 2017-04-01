#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc > 1){
        // iterate over strings in argv, starting at index 1 (excluding program name)
        
        
        // for each argument word,
        for (int i = 1; i < argc; i++){
            
            // for each character in each word,
            for (int j = 0, k = strlen(argv[i]); j < k; j++){
                
                // print each character;
                printf("%c", argv[i][j]);
            }
        }
                // print a new line once all that is done;
                printf("\n");
        
    } else {
        printf("Error; no message passed\n");
    }
}