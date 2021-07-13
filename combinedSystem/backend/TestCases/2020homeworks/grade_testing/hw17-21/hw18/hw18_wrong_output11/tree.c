#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "tree.h"

void deleteTreeNode(TreeNode * tr)
{
  if (tr == NULL)
    {
      return;
    }
  deleteTreeNode (tr -> left);
  deleteTreeNode (tr -> right);
  free (tr);
}

void freeTree(Tree * tr)
{
  if (tr == NULL)
    {
      // nothing to delete
      return;
    }
  deleteTreeNode (tr -> root);
  free (tr);
}
/*
  NOTE: This function conbine two TreeNode as a new TreeNode
*/
TreeNode* conbineTreeNode(TreeNode* leftT, TreeNode* rightT)
{
  TreeNode* new;
  new = malloc(sizeof(TreeNode));
  new -> left = leftT;
  new -> right = rightT;
  new -> value = -1;
  return new;
}

/*
  NOTE: This function read from input file and store each charater as integer
*/
bool readfile(char* filename, int* list,int* num)
{
  FILE *fptr = fopen(filename,"r");
  int c=0;
  if(fptr == NULL) return false;
  while((c = fgetc(fptr)) != EOF){
    list[(*num)] = c;
    ++(*num);
  }
  return true;
}

/*
  NOTE: This function create the tree
        ASCII: 0:48 1:49
        list: the integer array read from file
        size: size of the list
*/
Tree * buildTree(int * list, int size)
{
  // NOTE: HTree: Tree will return
  //       NodeList: A list to store different TreeNode
  //       Node_size: size of NodeList
  //       flag: judge whether meet 1
  Tree * HTree;
  HTree= malloc(sizeof(Tree));
  TreeNode** NodeList;
  NodeList = malloc(sizeof(TreeNode*)*1000);
  int Node_size=0;
  int flag=0;

  for(int i=0;i<size;i++)
  {
    if(flag) // last time read 1, this time should create new node
    {
      TreeNode *new;
      new = malloc(sizeof(TreeNode));
      new -> value = list[i];
      new -> left = NULL;
      new -> right = NULL;

      NodeList[Node_size] = new;
      Node_size++;
      flag=0;
    }
    else if(list[i]==49) flag = 1; // for next time 
    else if(list[i]==48 && Node_size>=2){ // not last 0, combine the lastest node
      TreeNode *new;
      new = conbineTreeNode(NodeList[Node_size-2], NodeList[Node_size-1]);
      Node_size --;
      NodeList[Node_size -1] = new;
    }
    else if(list[i]==48 && Node_size==1) continue; // last 0 is read
  }
  // NOTE: the only remain Node must be Root
  HTree -> root = NodeList[0]; 

  // Free all of them after use
  free(NodeList);
  free(list);
  return HTree;
}
/*
  NOTE: This function print the path based on the target value, store the path in result and return number of it 
*/
void printPath(TreeNode * tr, char* path,int num,int count,int target,char * result,int* numm)
{
  if(tr->value == target) // find it
  { 
    memcpy(&result[count],&path[0],num);
    *numm=num;
    return;
  }

  // recursion 
  if(tr ->left != NULL){
    path[num] = '0';
    printPath(tr->left,path,(num)+1,count,target,result,numm);
  }

  if(tr ->left != NULL){
    path[num] = '1';
    printPath(tr->right,path,(num)+1,count,target,result,numm);
  }
  return;
}
