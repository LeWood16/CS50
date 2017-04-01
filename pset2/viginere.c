#include <stdio.h>
#include <cs50.h>
#include <string.h>


bool lc(char a);
bool uc(char a);
bool not_a_letter(char a);
bool overflow(char a, int key);



bool lc(char a){
    int lower_min = 97;
    int lower_max = 122;
    if (a > lower_min - 1 && a < lower_max + 1){ // lowercase ascii range (if lowercase),
        return true;
    } else {
        return false;
    }
}


bool uc(char a){
    int upper_min = 65;
    int upper_max = 90;
    if (a > upper_min - 1 && a < upper_max + 1){ // uppercase ascii range (if uppercase),
        return true;
    } else {
        return false;
    }
}

bool not_a_letter(char a){
    if (a < 65 || a > 122){ 
        return true;
    } else {
        return false;
    }
}

bool overflow(char a, int key){
    // for each character in plaintext,
    if (lc(a) && (a + key > 122)){ // if lowercase AND it overflows,
        return true;
    } else if (uc(a) && (a + key > 90)){ // if uppercase AND if overflows,
        return true;
    } else {
        return false;
    }
}

bool all_alpha(char a[]);

bool all_alpha(char a[]){
    for (int i = 0, n = strlen(a); i < n; i++){
        if (not_a_letter(a[i])){ // if a character is neither an uppercase nor lowercase letter,
            return false;          // return false
        }
    }
    
    return true;                  // if no non-alphabetic character is found, return true;
}




// take a sequence of characters, and turn in into an array of integers (0 to 26, depending on letter);

// make sure key is alphabetical with isalpha function



int main(int argc, string argv[])
{
    
    // initialize key and plaintext variables;    
   char *key;
   char *text;
   key = argv[1];


   // if argument count isn't right, kick out of program;
    if ((argc != 2) || !(all_alpha(key))){
        return 1;
    } else {
        
    // otherwise, set key to first argument, prompt user for plaintext, and store plaintext into 'text' string;


       printf("plaintext:");
       text = get_string();
    }


    
 //   int lower_vigi = lower_min = atoi(argv[1]);

    // for each character in plaintext,
    int lower_min = 97;
    int lower_max = 122;
    int upper_min = 65;
    int upper_max = 90;

    for (int i = 0, n = strlen(text); i < n; i++){
        
        
        if (not_a_letter(text[i])){ 
            // if not a letter, print exactly as it was entered in;
            printf("%c", text[i]);           
            
        // if lowercase,    
        } else if (lc(text[i])){ // lowercase ascii range (if lowercase),

            // if key would cause lowercase to overflow, wrap it around instead 97-122
            if (overflow(text[i], key)){
                int extra = text[i] + key - lower_max - 1; // set up an overflow integer to add to lower_min, thus wrapping around
                printf("%c", lower_min + extra);

                
            } else {
                printf("%c", text[i] + key); // if no overflow, simply add key to ascii value and return enciphered lowercase character
            }
            
            // printing to the same as earlier text
        
        // if uppercase,   
        } else if (uc(text[i])){ // uppercase ascii range (if uppercase),

            // if key would cause uppercase to overflow, wrap it around instead 65-90
            if (overflow(text[i], key)){

                
                int extra = text[i] + key - upper_max - 1; // set up an overflow integer to add to upper_min, thus wrapping around
                printf("%c", upper_min + extra);
                
            } else {
                printf("%c", text[i] + key); // if no overflow, simply add key to ascii value and return enciphered uppercase character

            }

            
        }

    
    }
    
      // print new line when finished
    printf("\n");

}