#include <ctype.h>
#include <stdio.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <stdlib.h>

#include "dictionary.h"

typedef struct node
{
    char val;
    struct node *next;
}
node;



// make a linked list using above stuff and thingz



bool load(const char *dictionary);

bool load(const char *dictionary)
{

    FILE *fp = fopen(dictionary, "r");
        if (fp == NULL){
            fprintf(stderr, "Could not open %s.\n", dictionary);
            return 1;
        }
    return true;
}




void print_list(node * head) {
    node * current = head;
    
    while (current != NULL) {
        printf("%c\n", current->val);
        current = current->next;
    }
}


void push(node * head, char val[]) {
    node * current = head;
    while (current->next != NULL){
        current = current->next;
    }
    
    current->next = malloc(sizeof(node));
    current->next->val = *val;
    current->next->next = NULL;
}

int main(int argc, char *argv[])
{
    
    if (argc != 2){
        printf("usage: ./test dictionary");
        return 1;
    }
    
    char *dictionary = argv[1];
    
     FILE *fp = fopen(dictionary, "r");
        if (fp == NULL){
            fprintf(stderr, "Could not open %s.\n", dictionary);
            return 1;
        }

    
    node * head = NULL;
    head = malloc(sizeof(node));
    if (head == NULL){
        return 1;
    }
    
    
    for (int c = fgetc(fp); c != EOF; c = fgetc(fp)){
        push(head, c);
    }
    
    /*
    head->val = 1;
    head->next = NULL;
    push(head, 't');
    push(head, 'e');
    push(head, 's');
    push(head, 't');
    */

    
    print_list(head);
    
    
    
    
    
    
    
    
    
    
    
    /*
   // char* text = "./texts/alice.txt";
    char* dictionary = "./dictionaries/small";
    
    bool loaded = load(dictionary);
    
    FILE *fp = fopen(dictionary, "r");
        if (fp == NULL){
            fprintf(stderr, "Could not open %s.\n", dictionary);
            return 1;
        }
    

    // check for correct number of args
    if (argc < 1)
    {
        printf("Usage: speller\n");
        return 1;
    }


    // spell-check each word in text
    for (int c = fgetc(fp); c != EOF; c = fgetc(fp))
    {
        printf("%c", c);
    }
    
    printf("\n");
    
    if (!loaded)
    {
        printf("dictionary did not load\n");
    } else 
    {
        printf("dictionary has successfully loaded\n");    
    }


  //  printf("dictionary name:%s\n", dictionary);
  
  */

}
