#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "hw08.h"
 
#ifdef TEST_MAIN
int main(int argc, char * * argv)
{
  if(argc != 3)
  {
    return EXIT_FAILURE;
  }

  int count = countVector(argv[1]);
  
  if(count < 1)
  {
    return EXIT_FAILURE;
  }

  Vector * arr;
  arr = malloc(sizeof(Vector) * count);
  
  if(!readVector(argv[1], arr, count))
  {
    return EXIT_FAILURE;
  }
  
  #ifdef DEBUG
  printVector(vecArr, countVec);
  #endif 
  
  #ifdef DEBUG
  printf("\n");
  printVector(vecArr, countVec);
  #endif 

  qsort(arr, count, sizeof(Vector), compareVector);
  
  if(!writeVector(argv[2], arr, count))
  {
    free(arr);
    return EXIT_FAILURE;
  }

  free(arr);
  return EXIT_SUCCESS;
}
#endif