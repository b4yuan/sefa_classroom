

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 


TESTFALGS = 

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw18: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw18

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 


test1: hw18
	./hw18 inputs/input1 inputs/test1 output1
	diff -w output1 expected/expected1 > grade.txt

test2: hw18
	./hw18 inputs/input2 inputs/test2 output2
	diff -w output2 expected/expected2 > grade.txt

test3: hw18
	./hw18 inputs/input3 inputs/test3 output3
	diff -w output3 expected/expected3 > grade.txt

test4: hw18
	./hw18 inputs/input4 inputs/test4 output4
	diff -w output4 expected/expected4 > grade.txt

test5: hw18
	./hw18 inputs/input5 inputs/test5 output5
	diff -w output5 expected/expected5 > grade.txt

memcheck: hw18
	$(VAL) ./hw18 inputs/input1 inputs/test1 output1

clean: # remove all machine generated files
	rm -f hw18 *.o output?

