WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)

hw16: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw16

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw16
	./hw16 inputs/test1in inputs/test1post > output1
	diff -w output1 expected/expected1 > grade.txt

test2: hw16
	./hw16 inputs/test2in inputs/test2post > output2
	diff -w output2 expected/expected2 > grade.txt

test3: hw16
	./hw16 inputs/test3in inputs/test3post > output3
	diff -w output3 expected/expected3 > grade.txt

test4: hw16
	./hw16 inputs/test4in inputs/test4post > output4
	diff -w output4 expected/expected4 > grade.txt

test5: hw16
	./hw16 inputs/test5in inputs/test5post > output5
	diff -w output5 expected/expected5 > grade.txt

test6: hw16
	./hw16 inputs/test6in inputs/test6post > output6
	diff -w output6 expected/expected6 > grade.txt

clean: # remove all machine generated files
	rm -f hw16 *.o output?



