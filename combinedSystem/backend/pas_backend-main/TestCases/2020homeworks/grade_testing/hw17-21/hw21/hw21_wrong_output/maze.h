#ifndef MAZE_H
#define MAZE_H
#define COL 9
#define ROW 9
bool read_maze(int maze[ROW][COL], char* filename);
bool find_empty(int maze[ROW][COL],int *row,int *col);
bool judge(int maze[ROW][COL],int row,int col);
void solve_sudoku(int maze[ROW][COL],bool flag);
void print_maze(int maze[ROW][COL]);
#endif
