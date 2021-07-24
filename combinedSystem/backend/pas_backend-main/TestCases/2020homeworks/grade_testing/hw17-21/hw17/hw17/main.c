#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "tree.h"
int main(int argc, char * * argv)
{
  if (argc < 2) return EXIT_FAILURE;
  // NOTE: rtv: judge whether successful in reading file
  //       List: Store the input character as integers
  //       num: Size of List
  bool rtv;
  int *List;
  int num = 0;
  
  List = malloc(sizeof(int) * 1000);
  rtv = readfile(argv[1], List, &num);
  if (rtv == false) return EXIT_FAILURE;
  
  // NOTE: tr: the huffman tree
  //       path: a string to store path 
  Tree * tr = NULL;
  char * path=malloc(sizeof(char)*1000);

  tr = buildTree(List,num);
  printPath(tr->root,path,0);

  //free(List)
  freeTree(tr);
  free(path);
  return EXIT_SUCCESS;
}
