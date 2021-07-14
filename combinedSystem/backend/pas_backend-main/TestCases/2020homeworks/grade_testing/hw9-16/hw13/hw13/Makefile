WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_READLIST -DTEST_DELETELIST -DTEST_ADDNODE -DTEST_DELETENODE -DTEST_CALCULATE 

SRCS = main.c list.c calculate.c
OBJS = $(SRCS:%.c=%.o)

hw13: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw13

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw13
	./hw13 inputs/test1 > outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw13
	./hw13 inputs/test2 > outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw13
	./hw13 inputs/test3 > outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw13
	./hw13 inputs/test4 > outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw13
	./hw13 inputs/test5 > outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt

test6: hw13
	./hw13 inputs/test6 > outputs/output6
	diff outputs/output6 expected/expected6 > grade.txt

clean: # remove all machine generated files
	rm -f hw13 *.o output?


