// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "list.h"
#include "convert.h"
/*
void printL(List * arithlist)
{
  if (arithlist == NULL)
    {
      return;
    }
  ListNode * ln = arithlist -> head;
  ListNode * p;
  printf("from head: \n");
  while (ln != NULL)
    {
      p = ln -> next;
      printf("%s", ln -> word); // no need to add '\n'
      ln = p;
    }
}
*/

bool insertNode(List * arithlist, ListNode *ln,char * word){
  if(arithlist == NULL) return false;
  if(arithlist->head == NULL) return false;
  ListNode *p = arithlist->head;
  while(p!=NULL && p!=ln){
     p = p->next;
  }
  if(p == NULL) return false;
  if(p ==arithlist->tail){
    ListNode *new;
    new = malloc(sizeof(ListNode));
    p->next = new;
    new->prev = p;
    new->next = NULL;
    memcpy(new->word,word,WORDLENGTH);
    arithlist->tail = new;
    return true;
  }
  ListNode *new;
  new = malloc(sizeof(ListNode));
  ListNode *q = p->next;
  p->next = new;
  new->prev = p;
  new->next = q;
  q->prev = new;
  memcpy(new->word,word,WORDLENGTH);
  return true;
}
// DO NOT MODIFY FROM HERE --->>>
const int Operations[] = {'+', '-', '*', '(', ')'};

// return -1 if the word is not an operator
// return 0 if the word contains '+'
//        1                      '-'
//        2                      '*'
//        3                      '('
//        4                      ')'
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
// *** You MUST modify the convert function
// ***
#ifdef TEST_CONVERT
//7+10*2 => 7 10 2 * +
void add_minus(List *oper,List *arithlist,ListNode **cur){
  ListNode *p = oper->tail;
  while(p->prev!=NULL && (isOperator(p->prev->word)==2 ||isOperator(p->prev->word)==1)){
    insertNode(arithlist,*cur,p->prev->word);
    *cur = (*cur)->next;
    deleteNode(oper,p->prev);
  }
}
void free_parent(List *oper,List *arithlist,ListNode **cur){
  ListNode *p = oper->tail;
  while(isOperator(p->word)!=3){
    insertNode(arithlist,*cur,p->word);
    *cur = (*cur)->next;
    ListNode *q = p;
    p = p->prev;
    deleteNode(oper,q);
  }
  deleteNode(oper,p);
}
bool convert(List * arithlist)
{
  if (arithlist == NULL)
    {
      return true;
    }
  if ((arithlist -> head) == NULL)
    {
      return true;
    }
  List *oper; //store operator
  oper = malloc(sizeof(List));
  oper -> head = NULL;
  oper -> tail = NULL;
  ListNode *p = arithlist->head;
  while(p!=NULL){
    while(p!=NULL && isOperator(p->word)==-1) p=p->next;
    if(p==NULL) break;
    int num = isOperator(p->word);
    ListNode *q = p;
    switch (num)
    {
    case 0: addNode(oper,p->word);
            add_minus(oper,arithlist,&p);
            break;//+
    case 1: addNode(oper,p->word);
            add_minus(oper,arithlist,&p);
            break;//-
    case 2: addNode(oper,p->word);
            break;//*             
    case 3: addNode(oper,p->word);
            break;//(
    case 4: free_parent(oper,arithlist,&p);
            break;//) 
    default:
      break;
    }
    //printf("%s\n",p->word);
    p= p->next;
    
    deleteNode(arithlist,q);
    /* testing
    printL(arithlist);
    printL(oper);
    printf("===================================\n");
    */
  }
  ListNode *cur=oper->tail;
  while(oper->head!=NULL){
    addNode(arithlist,cur->word);
    if(cur->prev == NULL) break;
    cur = cur->prev;
  }
  deleteList(oper);
  return true;
}
#endif
