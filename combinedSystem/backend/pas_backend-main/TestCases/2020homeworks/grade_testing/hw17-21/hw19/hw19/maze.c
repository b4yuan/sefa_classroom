#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "maze.h"
/*
    find the width and height of the maze
    for further reading
*/
bool find_dimension(int* w, int* h, char* filename)
{
    FILE *fptr;
    char c;
    fptr = fopen(filename,"r");
    if(fptr==NULL) return false; 
    while((c = fgetc(fptr)) != EOF)
    {
        if(c=='\n') (*h)++;
        else (*w)++;
    }
    fclose(fptr);
    if(!(*w) || !(*h)) return true;
    *w /= *h;
    return true;
}

/*
    read in maze 
    store wall as -1
    store starting point as 0
    store path as -2
*/
bool read_maze(int w, int h, int* maze, char* filename,int* start)
{
    FILE *fptr = fopen(filename,"r");
    if(fptr==NULL) return false;
    char c;
    int ind = 0;
    while((c = fgetc(fptr)) != EOF)
    {
        if(c=='b') maze[ind++]=-1; //wall
        else if(c==' ') maze[ind++]=-2;//path
        else if(c=='s') 
        {
            *start = ind;
            maze[ind++]=0;//start point
        }
        else continue;
    }
    fclose(fptr);
    return true;
}

void bfs(int width,int height,int* maze,int start)
{   
    Que * q;
    q = malloc(sizeof(Que)*1005);
    int head,tail;
    head=0;
    tail=1;
    q[head].pos=start;
    q[head].step=0;
    while(head<tail)
    {
        start = q[head].pos;
         //NOTE: find if it is feasible to go for four direction
        int top = (start < width) ? -1 : 
              maze[start-width]==-2 ? (start - width) : -1;
        int bottom = (start >= (height-1)*width) ? -1 :
                 maze[start+width]==-2 ? (start + width) : -1;
        int left = start%width==0  ? -1 :
               maze[start-1]==-2 ? (start-1) : -1;
        int right = (start+1)%width==0 ? -1 :
               maze[start+1]==-2 ? (start+1) : -1;
        if(top!=-1) {
            q[tail].pos=top;
            q[tail].step=q[head].step + 1;
            maze[top]=q[head].step+1;
            tail++;
        }
        if(bottom!=-1) {
            q[tail].pos=bottom;
            q[tail].step=q[head].step + 1;
            maze[bottom]=q[head].step+1;
            tail++;
        }
        if(left!=-1) {
            q[tail].pos=left;
            q[tail].step=q[head].step + 1;
            maze[left]=q[head].step+1;
            tail++;
        }
        if(right!=-1) {
            q[tail].pos=right;
            q[tail].step=q[head].step + 1;
            maze[right]=q[head].step+1;
            tail++;
        }
        head++;
    }
    free(q);
    return;
}

void fill_all(int* maze,int fill)
{
    for(int i=0;i<fill-1;i++)
        if(maze[i]==-2) maze[i]=fill;
    return;
}

void print_maze(int* maze,int width,int height)
{
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
            j==0 ? printf("%4d",maze[i*width+j]): printf("%5d",maze[i*width+j]);
        printf(" \n");
    }
    return;
}