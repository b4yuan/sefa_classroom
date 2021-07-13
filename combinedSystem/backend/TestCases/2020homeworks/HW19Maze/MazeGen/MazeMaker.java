// MazeMaker.java// Andrew Davison, April 2005, ad@fivedots.coe.psu.ac.th/* Generates a maze, consisting of corridors and rooms,   and a single entrance.   The maze is represented by a grid of 'b' letters,   which represent the walls of the maze.   The maze is saved to MAZE_FN, or the file specified   on the command line.   Changes from MazeMaker.java in /Maze:     * increased width and height to 40*40 (was 20*16)     * randomly change some blocks to cylinders 'b' --> 'c'     * mark an open point with the 's'   The difference from MazeGen is that the mazes here    have rooms, large areas of solid blocks, and spaces   that cannot be reached.*/import java.awt.*;import java.io.*;public class MazeMaker{  private final static int WIDTH = 21;   // grid dimensions   private final static int HEIGHT = 21;    // should be a multiple of 4 plus 1 so enough space for    // rooms across and down  private final static int MAX_POINTS = 100;  private final static int ROOM_LEN = 3;  // so don't overlap point sep  private final static int POINT_SEP = 4;  private final static double CYLINDER_PERCENT = 0.2;     // percentage of blocks to change to cylinders  private final static String MAZE_FN = "maze.txt";  private Point points[];  private int numPoints;  private boolean connected[];  private char grid[][];    // use 'x' for a corridor or room fill    // use 'b' for walls of corridors/rooms  private Point entrance;   // on the top edge of the grid  public MazeMaker()  {    points = new Point[MAX_POINTS];    connected = new boolean[MAX_POINTS];    grid = new char[HEIGHT][WIDTH];    initPoints();    connectPoints();    makeRooms();    buildWalls();    makeCylinders();    placeStart();  }  // end of MazeMaker()  private void initPoints()  // create grid interior points and one entrance point  {    numPoints = 0;    for (int i=0; i < MAX_POINTS; i++)       connected[i] = false;    // set grid to be empty    for(int j=0; j < HEIGHT; j++)      for(int i=0; i < WIDTH; i++)        grid[j][i] = ' ';    // regular pattern of points    for(int y=2; y < HEIGHT; y=y+POINT_SEP)      for(int x=2; x < WIDTH; x=x+POINT_SEP)        if ((numPoints < MAX_POINTS) && !onAnEdge(x,y)) {          points[numPoints] = new Point(x, y);          grid[y][x] = 'x';          numPoints++;        }    entrance = new Point( (int)(WIDTH/2), 0);   // middle of top edge    grid[0][(int)(WIDTH/2)] = ' ';  }  // end of initPoints()  private boolean onAnEdge(int x, int y)  {    if ((x == 0) || (x == WIDTH-1) ||        (y == 0) || (y == HEIGHT-1))      return true;    return false;  }  private void connectPoints()  // draw 'L' shape lines between the points  {    Point pt1, pt2;    int pointsLeft = (int)(0.7 * numPoints);   // connect fewer points    while (pointsLeft >= 2) {       pt1 = selectPoint();       pt2 = selectPoint();       // System.out.print("" + pt1 + ", " + pt2);       connectPair(pt1.x, pt1.y, pt2.x, pt2.y);       pointsLeft = pointsLeft - 2;    }    // connect entrance pt to (at most) two internal points    pt1 = points[ randomPoint() ];    connectEntrance( pt1.x, pt1.y);    pt2 = points[ randomPoint() ];    connectEntrance( pt2.x, pt2.y);  }  // end of connectPoints()  private Point selectPoint()  // Select a point which is not already connected to something  {    int posn = randomPoint();    while (connected[posn])    // an inefficient loop       posn = randomPoint();    connected[posn] = true;    return points[ posn ];  }  private void connectPair(int x1, int y1, int x2, int y2)  // connect (x1,y1) and (x2,y2) via a 'L' shape line  {    if (Math.random() < 0.5) {  // randomly pick shape of 'L'      makeYLine( x1, y1, y2);      makeXLine( y2, x1, x2);    }    else {      makeXLine( y1, x1, x2);      makeYLine( x2, y1, y2);    }  }  // end of connectPair()  private void connectEntrance(int x, int y)  // Connect entrance to (x,y) using a 'L' shape line.  // The coding assumes the entrance is on the top edge.  {    makeYLine( entrance.x, entrance.y, y);    makeXLine( y, entrance.x, x);  }  private void makeYLine(int x, int y1, int y2)  // make a line (x,y1) to (x,y2) in the grid  {    // System.out.println("makeYLine " + x + ", " + y1 + ", " + y2);    int start = (y1 < y2) ? y1 : y2;    int end = (y1 < y2) ? y2 : y1;    for(int i = start; i <= end; i++)      grid[i][x] = 'x';  }  // end of makeYLine()  private void makeXLine(int y, int x1, int x2)  // make a line (x1,y) to (x2,y) in the grid  {    // System.out.println("makeXLine " + y + ", " + x1 + ", " + x2);    int start = (x1 < x2) ? x1 : x2;    int end = (x1 < x2) ? x2 : x1;    for(int i = start; i <= end; i++)      grid[y][i] = 'x';  }  // end of makeXLine()  private void makeRooms()  /* Randomly select numPoints/2 internal points and      convert them into rooms (squares filled with 'x's).  */  { int numRooms = 0;    Point pt;    while (numRooms < numPoints/2) {      pt = points[ randomPoint() ];    // don't check for duplicates      if (!nearEdge(pt.x, pt.y)) {        makeRoom(pt.x, pt.y);        numRooms++;      }    }  }  // end of makeRooms()  private boolean nearEdge(int x, int y)  // is (x,y) + or - ROOM_LEN/2 on/beyond an edge?  {    int len = (int)(ROOM_LEN/2);    if ((x-len <= 0) || (x+len >= WIDTH-1))       return true;    if ((y-len <= 0) || (y+len >= HEIGHT-1))       return true;    return false;  }  // end of nearEdge()  private void makeRoom(int x, int y)  /* Create a filled box of 'x's with (x,y) as its     centre, with sides of length ROOM_LEN */  {    int len = (int)(ROOM_LEN/2);    for(int i = x-len; i <= x+len; i++)      for(int j = y-len; j <= y+len; j++)        grid[j][i] = 'x';  } // end of makeRoom()  private void buildWalls()  {    for(int y=0; y<HEIGHT; y++)      for(int x=0; x < WIDTH; x++) {        if (grid[y][x] == ' ')   // put 'b's in the spaces          grid[y][x] = 'b';        else if (grid[y][x] == 'x')   // remove the 'x's          grid[y][x] = ' ';      }  }  private void makeCylinders()  // convert roughly CYLINDER_PERCENT blocks to cylinders  {    for(int y=0; y<HEIGHT; y++)      for(int x=0; x < WIDTH; x++) {        if ((grid[y][x] == 'b') &&             (Math.random() <= CYLINDER_PERCENT))          grid[y][x] = 'c';      }  }  private void placeStart()  // place the 's' in a large open space in the lower half of the maze  {    boolean placed = false;  search:    for(int y=HEIGHT/2; y<HEIGHT; y++) {      for(int x=0; x < WIDTH; x++) {        if ((grid[y][x] == ' ' ) && openSpace(y,x)) {          grid[y][x] = 's';          placed = true;          break search;        }      }    }    if (!placed)      grid[entrance.y][entrance.x] = 's';  } // end of placeStart()             private boolean openSpace(int y, int x) {   if ((y-1 < 0) || (y+1 >= HEIGHT) || (x-1 < 0) || (x+1 >= WIDTH))     return false;   if ((grid[y-1][x-1] == ' ') && (grid[y-1][x] == ' ') && (grid[y-1][x+1] == ' ') &&       (grid[y][x-1] == ' ') && (grid[y][x] == ' ') && (grid[y][x+1] == ' ') &&       (grid[y+1][x-1] == ' ') && (grid[y+1][x] == ' ') && (grid[y+1][x+1] == ' '))     return true;   return false; }     public void print()  {    System.out.println("-----");    for(int y=0; y<HEIGHT; y++) {      for(int x=0; x<WIDTH; x++)        System.out.print( grid[y][x] );      System.out.println("|");    }    System.out.println("-----");  }  private int randomX()  {  return (int)(WIDTH * Math.random()); }  private int randomY()  {  return (int)(HEIGHT * Math.random()); }  private int randomPoint()  {  return (int)(numPoints * Math.random()); }  public void save(String fn)  {    try {      PrintWriter out = new PrintWriter(							new FileWriter(fn));      for(int i=0; i < HEIGHT; i++)        out.println(grid[i]);      out.close();      System.out.println("Saved to " + fn);    }    catch(IOException e)    { System.out.println("Error writing to " + fn); }  }  // end of save()  // ---------------------------------  public static void main(String args[])  {    MazeMaker mm = new MazeMaker();    mm.print();    if (args.length == 0)      mm.save( MAZE_FN );    else       mm.save( args[0] );  }  // end of main()} // end of MazeMaker class