WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_DIVIDE -DTEST_INTERLEAVE -DTEST_SHUFFLE

SRCS = main.c shuffle.c
OBJS = $(SRCS:%.c=%.o)

hw12: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw12

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw12
	./hw12 3 1 | sort > output1
	diff -w output1 expected/expected31 > grade.txt

test2: hw12
	./hw12 3 2 | sort > output2
	diff -w output2 expected/expected32 > grade.txt

test3: hw12
	./hw12 4 2 | sort > output3
	diff -w output3 expected/expected42 > grade.txt

test4: hw12
	./hw12 6 2 | sort > output4
	diff -w output4 expected/expected62 > grade.txt

test5: hw12
	./hw12 4 3 | sort | uniq > output5
	diff -w output5 expected/expected_4_3 > grade.txt

test6: hw12
	./hw12 4 5 | sort | uniq > output6
	diff -w output6 expected/expected_4_5 > grade.txt

test7: hw12
	./hw12 5 2 | sort | uniq > output7
	diff -w output7 expected/expected_5_2 > grade.txt

test8: hw12
	./hw12 6 2 | sort | uniq > output8
	diff -w output8 expected/expected_6_2 > grade.txt

test9: hw12
	./hw12 7 3 | sort | uniq > output9
	diff -w output9 expected/expected_7_3 > grade.txt

test10: hw12
	./hw12 8 3 | sort | uniq > output10
	diff -w output10 expected/expected_8_2 > grade.txt

test11: hw12
	./hw12 11 2 | sort | uniq > output11
	diff -w output11 expected/expected_11_2 > grade.txt

clean: # remove all machine generated files
	rm -f hw12 *.o output?


