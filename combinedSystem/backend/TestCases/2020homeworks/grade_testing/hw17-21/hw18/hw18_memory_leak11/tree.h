#ifndef TREE_H
#define TREE_H

typedef struct tnode
{
  int value;
  struct tnode * left;
  struct tnode * right;
} TreeNode;

typedef struct trnode
{
  TreeNode * root;
} Tree;

void freeTree(Tree * tr);
TreeNode* conbineTreeNode(TreeNode* leftT, TreeNode* rightT);
bool readfile(char* filename, int* list,int* num);
Tree * buildTree(int * list, int size);
void printPath(TreeNode * tr, char* path,int num,int count,int target,char *result,int* numm);
#endif
