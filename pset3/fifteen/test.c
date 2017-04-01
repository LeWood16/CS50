#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(void)
{
    int max = 9;
    int board[max][max];
    int d = 4;

    int tile = d*d - 1;               // start the tile progression at the highest possible tile value;
    for (int i = 0; i < d; i++){    // for each row.
        for (int j = 0; j < d; j++){// for each column,
            board[i][j] = tile;     // set value for tile;
            tile--;
        }
    }
    
    if (d % 2 == 0) { // if dimesions are even,
        int a = board[d-1][d-3];
        int b = board[d-1][d-2];
        board[d-1][d-2] = a;
        board[d-1][d-3] = b; // switch the '1' and '2' tiles;
 
    }

    for (int i = 0; i < d; i++){        // for each row,
        for (int j = 0; j < d; j++){    // for each column,
            if (board[i][j] < 10){
                printf("%i  ", board[i][j]); // if tile value is a single digit, print two spaces to preserve the game design;
            } else {
                printf("%i ", board[i][j]);  // otherwise, just print the one preceeding space;
            }
        }
        printf("\n"); // print a new line for the next row;
    }
    
    int tileV = 11;
    int tileValue, tileX, tileY;
    int up, down, right, left;
    for (int i = 0; i < d; i++){
        for (int j = 0; j < d; j++){
            if (board[i][j] == tileV){
                tileValue = board[i][j];
                tileX = i;
                tileY = j;
            } else {
                continue;
            }
        }
    }
    
    up = board[tileX-1][tileY];
    down = board[tileX+1][tileY];
    right = board[tileX][tileY+1];
    left = board[tileX][tileY-1];
    
    printf("up value:%i\n", up);
    printf("down value:%i\n", down);
    printf("right value:%i\n", right);
    printf("left value:%i\n", left);


}