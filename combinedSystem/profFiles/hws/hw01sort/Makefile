# ***
# *** You can modify this file. You do not (should not) submit this file
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_SWAP -DTEST_SORT

SRCS = main.c sort.c
OBJS = $(SRCS:%.c=%.o)

sort: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o sort

ascsort:
	$(GCC) $(TESTFALGS) -DASCENDING $(SRCS) -o ascsort

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2 test3 test4 test5 test6 test7 test8 test9 test10

test1: ascsort
	./ascsort inputs/test1 > output1
	diff output1 expected/expected1 > grade.txt

test2: ascsort
	./ascsort inputs/test2 > output2
	diff output2 expected/expected2 > grade.txt

test3: ascsort
	./ascsort inputs/test3 > output3
	diff output3 expected/expected3 > grade.txt

test4: ascsort
	./ascsort inputs/test4 > output4
	diff output4 expected/expected4 > grade.txt

test5: ascsort
	./ascsort inputs/test5 > output5
	diff output5 expected/expected5 > grade.txt

test6: sort
	./sort inputs/test1 > output6
	diff output6 expected/expected6 > grade.txt

test7: sort
	./sort inputs/test2 > output7
	diff output7 expected/expected7 > grade.txt

test8: sort
	./sort inputs/test3 > output8
	diff output8 expected/expected8 > grade.txt

test9: sort
	./sort inputs/test4 > output9
	diff output9 expected/expected9 > grade.txt

test10: sort
	./sort inputs/test5 > output10
	diff output10 expected/expected10 > grade.txt

testfor: ascsort  # same as testall
	for case in 1 2 3; do \
	echo $$case; \
	./ascsort inputs/test$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done

clean: # remove all machine generated files
	rm -f sort ascsort *.o output?


