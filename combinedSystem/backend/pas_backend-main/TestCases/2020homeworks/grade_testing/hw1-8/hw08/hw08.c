#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "hw08.h"

#ifdef TEST_COUNTVECTOR
int countVector(char * filename)
{
  Vector * arr;

  FILE * fptr = fopen(filename, "r");
  if(!fptr)
  {
    return (-1);
  }

  fseek(fptr, 0, SEEK_END);

  long bytes = ftell(fptr);
  int elem = bytes / sizeof(Vector);
 
  arr = malloc(sizeof(Vector) * elem);
  
  fclose(fptr);
  
  //new file
  FILE * newfptr = fopen(filename, "r");
  int read = fread(arr, sizeof(Vector), elem, newfptr);

  if(read != elem)
  {
    free(arr);
    return (-1);
  }

  int next = fgetc(newfptr);
  
  if(next != EOF)
  {
    free(arr);
    return (-1);
  }
  
  free(arr);
  fclose(newfptr);
  return (read);
}
#endif
 
#ifdef TEST_READVECTOR
bool readVector(char* filename, Vector * vecArr, int size)
{
  FILE * fptr = fopen(filename, "r");
  
  if(!fptr)
  {
    return (false);
  }
  
  int elem = fread(vecArr, sizeof(Vector), size, fptr);
  
  if(elem != size)
  {
    return (false);
  }
  
  fclose(fptr);
  return (true);
}
#endif
 
#ifdef TEST_COMPAREVECTOR
int compareVector(const void *p1, const void *p2)
{
  const Vector * val1 = (const Vector *) p1;
  const Vector * val2 = (const Vector *) p2;
  
  if(val1 -> x < val2 -> x)
  {
    return (-1);
  }
  else if(val1 -> x > val2 -> x)
  {
    return (1);
  }
  else
  {
    if(val1 -> y < val2 -> y)
    {
      return (-1);
    }
    else if(val1 -> y > val2 -> y)
    {
      return (1);
    }
    else
    {
      if(val1 -> z < val2 -> z)
      {
        return (-1);
      }
      else if(val1 -> z > val2 -> z)
      {
        return (1);
      }
      else
      {
        return (0);
      }
    }
  }
}
#endif
 
#ifdef TEST_WRITEVECTOR
bool writeVector(char* filename, Vector * vecArr, int size)
{
  FILE * fptr = fopen(filename, "w");
  
  if(!fptr)
  {
    return (false);
  }
  
  int write = fwrite(vecArr, sizeof(Vector), size, fptr);
  
  if(write != size)
  {
    return (false);
  }
  else
  {
    fclose(fptr);
    return (true);
  }
}
#endif
 
// This function is provided to you. No need to change
void printVector(Vector * vecArr, int size)
{
  int ind = 0;
  for (ind = 0; ind < size; ind ++)
  {
    printf("%6d %6d %6d\n",
    vecArr[ind].x, vecArr[ind].y, vecArr[ind].z);
  }
}