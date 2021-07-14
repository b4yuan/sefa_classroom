#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "tree.h"
int main(int argc, char * * argv)
{
  if (argc < 4) return EXIT_FAILURE;
  // NOTE: rtv: judge whether successful in reading file
  //       List1: Store the input character as integers
  //       num1: Size of List1
  //       List2: Store the chaacter needed to convert
  //       num2: Size of List2
  bool rtv;
  int *List1;
  int num1 = 0;
  int *List2;
  int num2 = 0;

  List1 = malloc(sizeof(int) * 1000);
  List2 = malloc(sizeof(int) * 1000);
  rtv = readfile(argv[1], List1, &num1);
  if (rtv == false) return EXIT_FAILURE;
  rtv = readfile(argv[2], List2, &num2);
  if (rtv == false) return EXIT_FAILURE;


  // NOTE: tr: the huffman tree
  //       path: a string to store path 
  Tree * tr = NULL;
  char * path=malloc(sizeof(char)*1000);
  tr = buildTree(List1,num1);

  // NOTE: fptr: read the file
  //       path: a string to store path 
  //       result: to store total path
  FILE *fptr = fopen(argv[3],"wb");
  if(fptr == NULL) return EXIT_FAILURE;
  char* result;
  result = malloc(sizeof(char)*1000);
  // NOTE: count: total length of the result
  //       numm: number of length return each term
  int count=0;
  int numm=0;
  for(int i=0;i<num2;i++)
  {
    printPath(tr->root,path,0,count,List2[i],result,&numm);
    count+=numm;
  }

  // if not have more 0 
  while(count%8!=0)
  {
    result[count] = '0';
    count++;
  }

  // NOTE: final_result: after compressed result
  unsigned char *final_result;
  final_result = malloc(sizeof(char)*(count/8));
  for(int j=0;j<count;j+=8)
  {
    char *t;
    t = malloc(sizeof(char)*9);
    memcpy(&t[0],&result[j],8);
    t[8] = '\0';
    // change to int in decimal
    unsigned char temp = (int) strtol(t,NULL,2);
    free(t);
    // assign to final result
    final_result[j/8] = temp;
  }
  // write to the file
  fwrite(&final_result[0],sizeof(char),count/8,fptr);

  // free all the stuff
  //free(result);
  //free(List2);
  //freeTree (tr);
  //free(path);
  //free(final_result);
  fclose(fptr);
  return EXIT_SUCCESS;
}
