# ***
# *** You can modify this file. You do not (should not) submit this file
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
EXEC = # executable here

TESTFALGS = -DTEST_SWAP -DTEST_SORT

SRCS = # sources here
OBJS = $(SRCS:%.c=%.o)

all: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o $(EXEC)

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2# ... more targets for more testcases

test1: all
	./($EXEC) inputs/test1 > output1
	diff output1 expected/expected1 > grade.txt

test2: all
	./($EXEC) inputs/test2 > output2
	diff output2 expected/expected2 > grade.txt

clean: # remove all machine generated files
	rm -f sort ascsort *.o output?


