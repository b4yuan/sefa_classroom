WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_DIVIDE -DTEST_INTERLEAVE -DTEST_SHUFFLE

SRCS = main.c shuffle.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw11: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw11

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw11
	./hw11 4 | sort > output1
	diff -w output1 expected/expected4 > grade.txt

test2: hw11
	./hw11 8 | sort > output2
	diff -w output2 expected/expected8 > grade.txt

test3: hw11
	./hw11 11 | sort > output3
	diff -w output3 expected/expected11 > grade.txt

clean: # remove all machine generated files
	rm -f hw11 *.o output?


