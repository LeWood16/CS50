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


int ascii_arr(char a);

int ascii_arr(char a){
    // input is a string of alpha characters (i.e. the key to the viginere sequence);
    // output is an array of ascii numbers, mutated by their proxomity to a being 0;
    int l = strlen(a);
    char arra[l];
    
    for (int j = 0; j < l; j++){
        arra[j] = a[j];
    }
    
    return *arra;
}



// create a function to construct an array of numbers based on ascii values of characters (i.e. a would be 0, b 1, c 2, etc. same for uppercase,
// but preserve case!)




// take a sequence of characters, and turn in into an array of integers (0 to 26, depending on letter);

// make sure key is alphabetical with isalpha function














int main(int argc, string argv[])
{
    
    // initialize key and plaintext variables;    
   char *key;
   char *text;
   key = argv[1];)
   int testArr = ascii_arr(key);



   // if argument count isn't right, kick out of program;
    if ((argc != 2) || !(all_alpha(key))){
        return 1;
    } else {
        
    // otherwise, set key to first argument, prompt user for plaintext, and store plaintext into 'text' string;
       printf("plaintext:");
       text = get_string();
    }
    

    /*
    
    for (int i = 0, n = sizeof(arr) / sizeof(int); i < n ; i++){
        printf("%i ", arr[i]);
    }
    */
    printf("test arr:%i\n", testArr);
      // print new line when finished
    printf("\n");


}