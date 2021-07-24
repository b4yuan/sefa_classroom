#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "maze.h"
int main(int argc, char * * argv)
{
  // argv[1]: input file
  if (argc < 2)
    {
      return EXIT_FAILURE;
    }
  int maze[ROW][COL];
  bool rtf = read_maze(maze,argv[1]);
  if(rtf==false) return EXIT_FAILURE;
  solve_sudoku(maze,true);
  return EXIT_SUCCESS;
}
