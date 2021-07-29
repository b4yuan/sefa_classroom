WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_CREATELIST -DTEST_ELIMINATE -DTEST_DELETENODE -DDEBUG

SRCS = main.c hw10.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw10: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw10

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw10
	./hw10 6 3 > output1
	diff output1 expected/expected1 > grade.txt

test2: hw10
	./hw10 6 4 > output2
	diff output2 expected/expected2 > grade.txt

test3: hw10
	./hw10 25 7 > output3
	diff output3 expected/expected3 > grade.txt

clean: # remove all machine generated files
	rm -f hw10 *.o output?


