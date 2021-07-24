#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "maze.h"

/*
    read in maze 
    store - as 0
    1: 49
*/
bool read_maze(int maze[ROW][COL], char* filename)
{
    FILE *fptr = fopen(filename,"r");
    if(fptr==NULL) return false;
    char c;
    int ind = 0;
    while((c = fgetc(fptr)) != EOF)
    {
        if(c=='\n') continue;
        int row = ind/COL;
        int col = ind%COL;
        maze[row][col] = c=='-' ? 0 : c-48; 
        ind++;
    }
    //fclose(fptr);
    return true;
}
/*
    This function find the empty space to fill in the sudoku
*/
bool find_empty(int maze[ROW][COL],int *row,int *col)
{
    for(int i=0;i<ROW;i++)
        for(int j=0;j<COL;j++)
            if(maze[i][j]==0)
            {
                *row = i;
                *col = j;
                return true;
            }
    return false;
}

/*
    This function judge whether fill in the number is valid
*/
bool judge(int maze[ROW][COL],int row,int col)
{
    // each block
    int row_start = (row/3) * 3;
    int col_start = (col/3) * 3;
    for(int i=row_start;i<row_start+3;i++)
        for(int j=col_start;j<col_start+3;j++)
            if(i!=row && j!=col && maze[i][j]==maze[row][col]) 
                return false;
    // each row
    for(int j=0;j<COL;j++)
        if(j!=col && maze[row][j]==maze[row][col])
            return false;
    // each column
    for(int i=0;i<ROW;i++)
        if(i!=row && maze[i][col]==maze[row][col])
            return false;

    return true;
}
/*
    This funtion solve for the sudoku
*/
void solve_sudoku(int maze[ROW][COL],bool flag)
{
    int next_row,next_col;
    bool empty = find_empty(maze,&next_row,&next_col);
    if(empty == false) // all filled and meet requirement
    {
        print_maze(maze);
        flag = false; //find the answer
        return;
    }

    for(int i=1;i<10;i++)
    {
        maze[next_row][next_col]=i;
        if(judge(maze,next_row,next_col)&&flag) //skip if not valid or already find answer
            solve_sudoku(maze,flag);
    }
    maze[next_row][next_col]=0; // change back
    return;
}
/*
    This function is try to print the answer
*/
void print_maze(int maze[ROW][COL])
{
    for(int i=0;i<ROW;i++)
    {
        for(int j=0;j<COL;j++)
            printf("%d",maze[i][j]);
        printf("\n");
    }
    return;
}