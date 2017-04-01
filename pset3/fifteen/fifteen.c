/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);



int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = get_int();
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    
    
    // test init
    
    // start test
    /*
    int tile = 1;
    for (int i = 0; i < d; i++){
        for (int j = 0; j < d; j++){
            board[i][j] = tile;
            tile++;
        }
    }
    board[d-1][d-1] = 0;
    */
    // end test 
    
    //start actual
    
    int tile = d*d - 1;               // start the tile progression at the highest possible tile value;
    for (int i = 0; i < d; i++){    // for each row.
        for (int j = 0; j < d; j++){// for each column,
            board[i][j] = tile;     // set value for tile;
            tile--;
        }
    }
    
    if (d % 2 == 0) { // if dimensions are even,
        int a = board[d-1][d-3];
        int b = board[d-1][d-2];
        board[d-1][d-2] = a;
        board[d-1][d-3] = b; // switch the '1' and '2' tiles;
 
    }
    
    // end actual
}

/**
 * Prints the board in its current state.
 */
void draw(void)
{
    
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
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile)
{
    
    int tileValue, tileX, tileY;
    int up, down, right, left;
    for (int i = 0; i < d; i++){
        for (int j = 0; j < d; j++){
            if (board[i][j] == tile){
                tileValue = board[i][j];
                tileX = i;
                tileY = j;
            } else {
                continue;
            }
        }
    }
    // make exception functions for if the square is on the sides!!!
    up = board[tileX-1][tileY]; // store all values of surrounding tiles
    down = board[tileX+1][tileY];
    right = board[tileX][tileY+1];
    left = board[tileX][tileY-1];
    
    if (tileY < d - 1 && right == 0){        // if not on the right border, check right for zero;
        board[tileX][tileY] = 0;
        board[tileX][tileY+1] = tileValue;// swap them;
        return true;
    } else if (tileY > 0 && left == 0){  // if not on the left border, check left for zero;
        board[tileX][tileY] = 0;
        board[tileX][tileY-1] = tileValue;// swap them;
        return true;
    } else if (tileX > 0 && up == 0){    // if not on the top border, check above for zero;
        board[tileX][tileY] = 0;
        board[tileX-1][tileY] = tileValue;// swap them;
        return true;
    } else if (tileX < d && down == 0){   // if not on the bottom border, check below for zero;
        board[tileX][tileY] = 0;
        board[tileX+1][tileY] = tileValue;// swap them;
        return true;
    } else {
        return false;
    }

}

/**
 * Returns true if game is won (i.e., board is in winning configuration), 
 * else false.
 */
bool won(void)
{
    int tile = 1;   // initialize tile as the first value (the empty tile);
    
    if (board[d-1][d-1] != 0){
        return false;
    }
    
    for (int i = 0; i < d; i++){        // for each row,
        for (int j = 0; j < d; j++){    // for each column,
            if (board[i][j] != tile){   // if tile is not in ascending order,
                return false;           // return false (the player hasn't won yet);
            } else {
                tile++;                 // move the tile to its next appropriate value;
            }
        }
    }
    
    return true;                        // return true if all the tiles are appropriately aligned;
}
