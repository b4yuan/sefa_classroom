WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_CONVERT 

SRCS = main.c list.c convert.c
OBJS = $(SRCS:%.c=%.o)

hw14: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw14

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw14
	./hw14 inputs/test1 > output1
	diff output1 expected/expected1 > grade.txt

test2: hw14
	./hw14 inputs/test2 > output2
	diff output2 expected/expected2 > grade.txt

test3: hw14
	./hw14 inputs/test3 > output3
	diff output3 expected/expected3 > grade.txt

test4: hw14
	./hw14 inputs/test4 > output4
	diff output4 expected/expected4 > grade.txt

test5: hw14
	./hw14 inputs/test5 > output5
	diff output5 expected/expected5 > grade.txt

clean: # remove all machine generated files
	rm -f hw14 *.o output?


