// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <string.h> 

#ifdef TEST_ELIMINATE
// 100% of the score
void eliminate(int n, int k)
{

  int i; 
  int j;
  // allocate an arry of n elements
  int * arr = malloc(sizeof(* arr) * n);
  // check whether memory allocation succeeds.
  // if allocation fails, stop
  if (arr == NULL)
    {
      fprintf(stderr, "malloc fail\n");
      return;
    }
  // initialize all elements

  for (i = 0; i < n; i++) {
    arr[i] = i; //array of integers going from 1 to k
  }

  int index = k - 1;

  // counting to k,
  // mark the eliminated element
  // print the index of the marked element
  // repeat until only one element is unmarked

for (i = n - 1; i > 0; i--) {
    while (index > i) {
      index -= i;
      index -= 1;
    }

    for (j = index; j < i; j++) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
    }

    printf("%d\n", arr[i]);
    
    while (index > i - 1) {
      index -= i;
    }
    
    index += k - 1;
  }

  // print the last one

  printf("%d\n", arr[0]);

  // release the memory of the array
  free (arr);
}
#endif