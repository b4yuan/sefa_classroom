# variables to change (marked inside <>):
#   NNN = name of the excutable.  ex) hw01
#	Input arguments = Name of all the input arguments, seperate by space. Do not include any pass, just put in the file name.   ex) -b input1 input2
#	Name of Outputfiles = Name of all the output files, seperate by space. Do not include any pass, just put in the file name.	ex) output1 output2
#   Name of one of the outputfiles = Name of one of the outputfiles. Do not include any pass, just put in the file name.		ex) output1
#	Name of one of the expected outputfiles = Name of one of the expected outputfiles. Do not include any pass, just put in the file name.  ex) expected1
# 
# Replace any <...> with the correct code. Follow the instruction specified above and at the end of this makefile


WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = <need input!!!>   							                             # Need modification  ex) -DTEST_COUNTWORD -DDEBUG

SRCS = <need input!!!>        														 # Need modification  ex) main.c list.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

<NNN>: $(OBJS) 																	     # Need modification
	$(GCC) $(TESTFALGS) $(OBJS) -o <NNN>

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: <NNN>																	# Need modification
	./ <NNN> <Input arguments> <Name of Outputfiles>
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> > grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles>	>> grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> >> grade.txt

test2: <NNN>																	# Need modification
	./ <NNN> <Input arguments> <Name of Outputfiles>
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> > grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> >> grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> >> grade.txt

test3: <NNN>																	# Need modification
	./ <NNN> <Input arguments> <Name of Outputfiles>
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> > grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> >> grade.txt
	diff <Name of one of the outputfiles> <Name of one of the expected outputfiles> >> grade.txt

clean: # remove all machine generated files											# Need modification
	rm -f <NNN> *.o output?



# If you need more test cases, create more test cases below with the same format as above. 
# You can have as many diff statement as you want. 

# If the program output its output to the sdtout, use the template for testcases below. 
#
# test5: <NNN>																	# Need modification
#	./ <NNN> <Input arguments> > out.txt
#	diff out.txt <Name of one of the expected outputfiles> > grade.txt
#
#
#
