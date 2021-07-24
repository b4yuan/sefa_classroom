#ifndef MAZE_H
#define MAZE_H
typedef struct maze
{
    int step;
    int pos;
}Que;

bool find_dimension(int* w, int* h, char* filename);
bool read_maze(int w, int h,int* maze, char* filename,int* start);
void bfs(int width,int height,int* maze,int start);
void fill_all(int* maze,int fill);
void print_maze(int* maze,int width,int height);
#endif
