WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_BUILDTREE

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)

hw15: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw15

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw15
	./hw15 inputs/test1in inputs/test1post output1
	diff output1 expected/expected1 > grade.txt

test2: hw15
	./hw15 inputs/test2in inputs/test2post output2
	diff output2 expected/expected2 > grade.txt

test3: hw15
	./hw15 inputs/test3in inputs/test3post output3
	diff output3 expected/expected3 > grade.txt

test4: hw15
	./hw15 inputs/test4in inputs/test4post output4
	diff output4 expected/expected4 > grade.txt

test5: hw15
	./hw15 inputs/test5in inputs/test5post output5
	diff output5 expected/expected5 > grade.txt

test6: hw15
	./hw15 inputs/test6in inputs/test6post output6
	diff output6 expected/expected6 > grade.txt

clean: # remove all machine generated files
	rm -f hw15 *.o output?


