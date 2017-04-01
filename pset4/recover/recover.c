/**
 * my attempt at recover.
 */
       
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char *argv[])
{

    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // remember filenames
    char *imagefile = argv[1];


    // open input file 
    FILE *inptr = fopen(imagefile, "r");
    if (inptr == NULL){
        fprintf(stderr, "Could not open %s.\n", imagefile);
        return 1;
    }
    
	// These are the starting bytes of a jpeg file.
	uint8_t checkjpg1[4] = {0xff, 0xd8, 0xff, 0xe0};
	uint8_t checkjpg2[4] = {0xff, 0xd8, 0xff, 0xe1};    
    
    // counter for number of jpegs in file; used to create filenames;
    int jpgcount = 0;

    // open file indicator
    int open = 0;
    FILE* outp;
    
    uint8_t buffer[512];
    uint8_t check[4];
    fread(buffer, 512, 1, inptr);
    
    while(fread(buffer, 512, 1, inptr) > 0){ // while there are still bytes to check in the file,
        for (int i = 0; i < 4; i++){
            check[i] = buffer[i]; // check values are now the first 4 values of the current buffer array;
        }
        
        // check for a jpeg;
        if((memcmp(checkjpg1, check, 4) == 0) || memcmp(checkjpg2, check, sizeof(check)) == 0){
            
            // construct the filename
            char filename[8];
            sprintf(filename, "%03d.jpg", jpgcount);
            
            if(open == 0){
                outp = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, outp);
                open = 1;
            }
            if(open == 1){
                fclose(outp);
                outp = fopen(filename, "w");
                fwrite(buffer, sizeof(buffer), 1, outp);
                jpgcount++;
            }
        } else {
            if(open == 1){
                fwrite(buffer, sizeof(buffer), 1, outp);
            }
        }
        
    }
    
    if(outp){
        fclose(outp);
    }
    
        fclose(inptr);
        return 0;
}