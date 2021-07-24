// ***
// *** You MUST modify this file
// ***
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tree.h"

// DO NOT MODIFY FROM HERE --->>>
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

static void preOrderNode(TreeNode * tn, FILE * fptr)
{
  if (tn == NULL)
    {
      return;
    }
  fprintf(fptr, "%d\n", tn -> value);
  preOrderNode(tn -> left, fptr);
  preOrderNode(tn -> right, fptr);
}

void preOrder(Tree * tr, char * filename)
{
  if (tr == NULL)
    {
      return;
    }
  FILE * fptr = fopen(filename, "w");
  preOrderNode(tr -> root, fptr);
  fclose (fptr);
}
// <<<--- UNTIL HERE

// ***
// *** You MUST modify the follow function
// ***

#ifdef TEST_BUILDTREE
// Consider the algorithm posted on
// https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/

//search value whether is in inArray
int searchRoot(int * inArray,int start,int end, int value)
{
  for(int i=end;i>=start;i--){
    if(inArray[i] == value) return i;
  }
  return -1;
}
//search value of right/left
int searchValue(int * inArray,int start,int end,int size,int *postArray)
{
  int ind=-1;
  int value=0;
  for(int i=end;i>=start;i--){
    int indx = searchRoot(postArray,0,size-1,inArray[i]);
    if(indx > ind){
       ind = indx;
       value = inArray[i];
    }
  }
  return value;
}

void buildNode(int * inArray,int * postArray,int start,int end,TreeNode *Root,int size)
{
  //Root has not left or right
  if(start >= end) {
    Root->left = NULL;
    Root->right = NULL;
    return;
  }
  //Root has left or right

  // find left and right root value
  int Root_in_index = searchRoot(inArray,start,end,Root->value); 
  Root->left = NULL;
  Root->right = NULL;
  if(Root_in_index > start){
    Root->left = malloc(sizeof(TreeNode));
    Root->left->value = searchValue(inArray,start,Root_in_index-1,size,postArray);
    buildNode(inArray,postArray,start,Root_in_index-1,Root->left,size);
  }
  if(Root_in_index < end){
    Root->right = malloc(sizeof(TreeNode));
    Root->right->value = searchValue(inArray,Root_in_index+1,end,size,postArray);
    buildNode(inArray,postArray,Root_in_index+1,end,Root->right,size);
  }
  return;
}

Tree * buildTree(int * inArray, int * postArray, int size)
{
  Tree *PreTree;
  TreeNode *Root;
  PreTree = malloc(sizeof(Tree));
  Root = malloc(sizeof(TreeNode));
  Root->value = postArray[size-1];
  PreTree->root = Root;
  buildNode(inArray,postArray,0,size-1,Root,size);
  return PreTree;
}
#endif
