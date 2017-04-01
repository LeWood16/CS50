#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string str;
    printf("Enter your name:");
    
 
        str = get_string();
        int leng = strlen(str);
        char space = 32;
        char c;


        if (str != NULL){
            for (int i = 0; i < leng; i++){     // for every char in str,
                c = str[i];
                if (c > 90){
                    c = c - 32;
                }

                if (i == 0 && c > 90){
                    printf("%c", str[0] - 32);      // print first letter of name as first initial;
                } else if (i == 0 && c < 91){
                    printf("%c", c);                // capitalize it if it's lowercase
                    
                } else if (c == space){
                    if (str[i-1] > 90){
                        printf("%c", str[i+1] - 32);
                    } else {
                        printf("%c", str[i+1]);    // otherwise print anything right before a space;
                    }
                }
                

            }
            printf("\n");
        }
    
    
    
    
    
}