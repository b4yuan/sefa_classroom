

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 


TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw17: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw17

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 


test1: hw17
	./hw17 inputs/input1 | sort > output1
	diff output1 expected/expected1 > grade.txt

test2: hw17
	./hw17 inputs/input2 | sort > output2
	diff output2 expected/expected2 > grade.txt

test3: hw17
	./hw17 inputs/input3 | sort > output3
	diff output3 expected/expected3 > grade.txt

test4: hw17
	./hw17 inputs/input4 | sort > output4
	diff output4 expected/expected4 > grade.txt

test5: hw17
	./hw17 inputs/input5 | sort > output5
	diff output5 expected/expected5 > grade.txt


clean: # remove all machine generated files
	rm -f hw17 *.o output?

