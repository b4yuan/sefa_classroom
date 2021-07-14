// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "calculate.h"
#include "list.h"

// DO NOT MODIFY FROM HERE --->>>
const int Operations[] = {'+', '-', '*'};

// return -1 if the word is not an operator
// return 0 if the word contains '+'
// return 1 if the word contains '-'
// ...
int isOperator(char * word)
{
  int ind;
  int numop = sizeof(Operations) / sizeof(int);
  for (ind = 0; ind < numop; ind ++)
    {
    char *loc = strchr(word, Operations[ind]);  
    if (loc != NULL && !isdigit(loc[1]))
	{
	  return ind;
	}
    }
  return -1;
}
// <<<--- UNTIL HERE

// ***
// *** You MUST modify the calculate function
// ***
#ifdef TEST_CALCULATE
// if arithlist is NULL, return true
// if arithlist -> head is NULL, return true
// if the input list is invalid, return false
bool calculate(List * arithlist)
{
  if (arithlist == NULL)
    {
      return true;
    }
  if ((arithlist -> head) == NULL)
    {
      return true;
    }
  // go through the list until there is only node in the list
  // find the next operator
  // If no operator can be found, return false
  // If an operator is found, find the two previous nodes as operands
  // If cannot find previous two operands, return false
  // If two operands can be found, perform the arithmetic operation
  // Be careful, subtraction is no commutative: 4 2 - means 4 - 2,
  //    not 2 - 4
  // After the operation,
  //     put the result back to the list
  //     remove the two nodes used to store the two operands
  // After going through the entire list and performing the operations,
  //     the list should have exactly one node left. If this is not
  //     true, return false
  // If the input is valud, return true
  // 7 10 2 + -
  //atoi
  ListNode *p = arithlist->head;
  while (p->next!= NULL)
  {
    while(isOperator(p->word)==-1 && p -> next != NULL){
      p = p->next;
    }
    if(p->next==NULL && isOperator(p->word)==-1) return false;
    if(p->prev == NULL || p->prev->prev == NULL) return false;
    int num;

    switch (isOperator(p->word))
    {
    case 0: num = atoi(p->prev->prev->word) + atoi(p->prev->word);
            break;
    case 1: num = atoi(p->prev->prev->word) - atoi(p->prev->word);
            break;
    case 2: num = atoi(p->prev->prev->word) * atoi(p->prev->word);
            break;
    default:
      break;
    }
    deleteNode(arithlist,p->prev);
    deleteNode(arithlist,p->prev);
    char *buff;
    buff = malloc(sizeof(char)*WORDLENGTH);
    sprintf(buff,"%d\n",num);
    memcpy(p->word,buff,WORDLENGTH);
    free(buff);
  }
  // if more than one node left, return false
  if(arithlist->head!=arithlist->tail) return false;
  // if the remaining node is an operator, return false
  if(isOperator(arithlist->head->word)!=-1) return false;
  // if everything is OK, return true
  return true;
}
#endif
