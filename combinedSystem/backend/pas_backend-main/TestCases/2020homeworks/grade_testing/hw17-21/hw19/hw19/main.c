#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "maze.h"
int main(int argc, char * * argv)
{
  if (argc < 2) return EXIT_FAILURE;
  //NOTE: Read the dimension of Maze
  int width = 0 ,height = 0;
  bool fr = find_dimension(&width,&height,argv[1]);
  if(!fr) return EXIT_FAILURE;
  //printf("%d %d\n",width,height);

  //NOTE: Read Maze with the size
  //      start: the index of starting point
  if(width==0 || height==0) return EXIT_SUCCESS;
  int * maze;
  int start;
  maze = malloc(width*height*sizeof(int));
  fr = read_maze(width,height,maze,argv[1],&start);
  if(!fr) return EXIT_FAILURE;
  
  //NOTE: bfs maze
  bfs(width,height,maze,start);
  //NOTE: fill in unreachable
  //print_maze(maze,width,height);
  fill_all(maze,width*height+1);

  //print the maze
  print_maze(maze,width,height);
  free(maze);
  return EXIT_SUCCESS;
}
