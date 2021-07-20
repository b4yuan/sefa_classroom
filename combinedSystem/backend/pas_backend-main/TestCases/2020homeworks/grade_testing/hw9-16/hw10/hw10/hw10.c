// ***
// *** You MUST modify this file
// ***

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <string.h>
#include "hw10.h"

// DO NOT MODIFY this function --->>>
void printListNode(ListNode * head)
{
  ListNode * p = head;
  printf("printListNode: ");
  while (p != NULL)
    {
      printf("%7d ", p -> value);
      p = p -> next;
    }
  printf("\n");
}
// <<<--- until here

// You MUST modify the following functions

#ifdef TEST_CREATELIST
// create a linked list storing values 0, 1, 2, ... valn - 1
// The first node (head) stores 0, the next node stores 1,
// ..., the last node stores valn - 1
// return the head of the linked listn
ListNode * createList(int valn)
{
  ListNode *head = malloc(sizeof(ListNode));
  ListNode *tail = NULL;
  
  head -> value = 0;
  head -> next = NULL;
  tail = head;
  for(int i = 1;i<valn;i++){
    ListNode *new;
    new = malloc(sizeof(ListNode));
    new -> value = i;
    new -> next = NULL;
    tail -> next = new;
    tail = new;
  }
  return head;
}
#endif

#ifdef TEST_ELIMINATE
// eliminate the nodes in the linked list
// starting from the head, move one node at a time and count to valk.
// eliminate that node, keep counting
//
// when reaching the end of the list, continue from the beginning of
// the list
//
// print the values of the nodes to be deleted
void eliminate(ListNode * head, int valk)
{

  // this #ifdef ... #endif should be inside the condition *BEFORE* a
  // node' value is printed and it is deleted
  ListNode * p = head;
  do{
  for(int i=1;i<valk;i++){
    if(p->next == NULL) p = head;
    else p = p->next;
  }
  ListNode * todelete = p;
  #ifdef DEBUG
  if(head->next != NULL) printListNode (todelete); 
  printf("%d\n",p->value);
  #endif
  p= p-> next != NULL ? p->next : head;
  head = deleteNode(head,todelete);
  }while(head!= NULL);

}
#endif

#ifdef TEST_DELETENODE
// head points to the first node in the linked list
// todelete points  to the node to be deleted
//
// delete the node and return the head of the linked list
// release the memory of the deleted node
//
// should check several conditions:
// 1. If head is NULL, the list is empty and this function returns
//    NULL
// 2. If todelete is NULL, nothing can be deleted, return head
// 3. If todelete is not in the list, keep the list unchanged and
//    return head
// It is possible that todelete is the first node in the list (i.e.,
// the head). If this occurs, return the second node of the list.
ListNode * deleteNode(ListNode * head, ListNode * todelete)
{
  if(head == NULL) return NULL;
  if(todelete == NULL) return head;
  ListNode *p = head;
  if(head == todelete){
    p = p->next;
    free(head);
    return p;
  }
  while(p->next != NULL){
    if(p->next == todelete){
      ListNode *q = p -> next;
      p->next = q->next;
      free(todelete);
      return head;
    }
    p = p->next;
  }
  return head;
}
#endif


