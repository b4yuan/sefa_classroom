// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#ifdef TEST_READLIST
// read line by line from the input file
// each line shorter than WORDLENGTH (including '\n' and '\0')
// arithlist should have memory to store head and tail
// If arithlist is NULL, return false
// If fopen fails, return false
// If a line is too long,
//    free memory of the list
//    fclose
//    return false
// If everything is fine
//    fclose
//    arithlist points to the head and tail of the list
//    return true
bool readList(char * filename, List * arithlist)
{
  FILE *fptr = fopen(filename,"r");
  if(fptr == NULL) return false;
  char *buff;
  buff = malloc(sizeof(char)*WORDLENGTH);
  while(fgets(buff,WORDLENGTH,fptr)!=NULL){
    if(strchr(buff,'\n')==NULL){
      deleteList(arithlist);
      fclose(fptr);
      return false;
    }
    addNode(arithlist,buff);
  }
  if(arithlist == NULL){
    free(buff);
    fclose(fptr);
    return false;
  }
  free(buff);
  fclose(fptr);
  return true;
}
#endif

#ifdef TEST_DELETELIST
// If arithlist is NULL, do nothing
// release the memory of every node in the list
// release the memory of the list 
void deleteList(List * arithlist)
{
  if(arithlist == NULL||arithlist->head==NULL) return;
  ListNode *p = arithlist->head;
  while(p->next != NULL){
    ListNode *q = p;
    if(p->next!=NULL) {
      p = p-> next;
      free(q);
      }
  }
  free(p);
  free(arithlist);
  return;
}
#endif

#ifdef TEST_ADDNODE
// Input: 
// arithlist stores the addresses of head and tail
// If arithlist is NULL, do nothing
// word is the word to be added
//
// Output:
// a ListNode is added to the end (become tail)
//
// allocate memory for a new ListNode
// copy word to the word attribute of the new ListNode
// insert the ListNode to the list
void addNode(List * arithlist, char * word)
{
  if(arithlist==NULL) return;
  if(arithlist->tail == NULL){
    ListNode *h = malloc(sizeof(ListNode));
    memcpy(h->word,word,WORDLENGTH);
    arithlist->head = h;
    arithlist->tail = h;
    h->prev = NULL;
    h->next = NULL;
    return;
  }
  ListNode *p = arithlist->tail;
  ListNode *new;
  new = malloc(sizeof(ListNode));
  p->next = new;
  new->prev = p;
  new->next = NULL;
  memcpy(new->word,word,WORDLENGTH);
  arithlist->tail = new;
  return;
}

#endif

#ifdef TEST_DELETENODE
//  Input:
// arithlist stores the addresses of head and tail
// If arithlist is NULL, return false
// If the list is empty (head and tail are NULL), return false
// ln is the node to be deleted
// If ln is not in the list, return false
// 
// Output:
// arithlist stores the addresses of head and tail
//   after ln is deleted
// return true.
//
// Be careful about delete the first or the last node
bool deleteNode(List * arithlist, ListNode * ln)
{
  if(arithlist == NULL) return false;
  if(arithlist->head == NULL) return false;
  ListNode *p = arithlist->head;
  while(p!=NULL && p!=ln){
     p = p->next;
  }
  if(p == NULL) return false;
  if(p == arithlist->head && p == arithlist->tail) {
    arithlist->head = NULL;
    arithlist->tail = NULL;
    free(ln);
    return true;
  }
  if(p == arithlist->head){
    arithlist->head = p-> next;
    p->next->prev = NULL;
    free(ln);
    return true;
  }
  if(p ==arithlist->tail){
    ListNode *q = arithlist->tail->prev;
    arithlist->tail = q;
    q->next = NULL;
    free(ln);
    return true;
  }
  ListNode *q = p->prev;
  ListNode *t = p->next;
  q->next = t;
  t->prev = q;
  free(p);

  return true;
}
#endif

