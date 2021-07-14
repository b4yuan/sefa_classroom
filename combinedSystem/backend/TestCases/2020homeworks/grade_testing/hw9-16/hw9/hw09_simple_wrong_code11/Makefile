WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)

TESTFALGS = -DTEST_MAIN -DDEBUG -DTEST_READDATA -DTEST_WRITEDATA -DTEST_MERGE -DTEST_MERGESSORT -DDEBUG

SRCS = main.c hw09.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw09: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw09

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c

test1: hw09
	./hw09 inputs/input1 output1
	diff output1 expected/expected1 > grade.txt

test2: hw09
	./hw09 inputs/input2 output2
	diff output2 expected/expected2 > grade.txt

test3: hw09
	./hw09 inputs/input3 output3
	diff output3 expected/expected3 > grade.txt

test4: hw09
	./hw09 inputs/input4 output4
	diff output4 expected/expected4 > grade.txt

test5: hw09
	./hw09 inputs/input5 output5
	diff output5 expected/expected5 > grade.txt
	
clean: # remove all machine generated files
	rm -f hw09 *.o output?
