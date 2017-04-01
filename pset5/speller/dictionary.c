/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>

#include "dictionary.h"

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    // TODO
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    
    FILE *fp = fopen(dictionary, "r");
        if (fp == NULL){
            fprintf(stderr, "Could not open %s.\n", dictionary);
            return 1;
        }
        
    // TODO
    typedef struct sllist 
    {
        int val;
        struct sllist* next;
    }
    sllnode;
    
    sllnode* create(int val);
    
    if (sllnode == NULL){
        return false;
    }
    
    sllnode* new = create(6);
    
    
    
    return false;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    int counter = 0;
    // TODO
    return 0;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    // TODO
    return false;
}
