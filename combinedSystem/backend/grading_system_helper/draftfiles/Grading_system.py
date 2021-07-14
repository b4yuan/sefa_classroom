import os
from distutils.ccompiler import new_compiler
import filecmp
import re

# 5. we need to set timeout for any os or make !!!!!!!!!
# pathin and pathout are not being used at all, so we need to look into whether we really need them or not.

# input: a string which is student file pass
# output: a tuple that has <grade, a list about feedback(each element is a string)>
def grade(path):
    """
    :param path: path to the project. ex) /users/alex/myfiles/project
    :type path: str
    :return: grade, feedback
    """

    list_final = []
    grade_final = 100

    debugging = False  # enable debugging print statements

    os.chdir(path)
    os.system('make clean >/dev/null 2>&1')

    if debugging:
        print('starting compile')

    # ---------------------------------
    # check that everything can compile
    # compiler = new_compiler()

    if len(os.listdir(path)) == 0:
        list_final.append('no files submitted')
        return 0, list_final

    compiler = new_compiler()

    for filename in os.listdir(path):  # for all files in the directory
        if filename.endswith(".c"):  # that end with .c
            try:
                compiler.compile([filename])  # check to see that it compiled
                list_final.append(f'{filename} compiled correctly!')

            except:
                list_final.append(f'{filename} did not compile correctly...')
                return 0, list_final

        else:
            continue

    if debugging:
        print('compile finished\nstarting diff')

    # this is the setup for the next few parts

    numberoftestcases = 0

    with open("Makefile", 'r') as f:  # open the Makefile
        text = f.read()

        # -----------------------
        # get the name of the executable

        ex = re.compile(r'-o (\w+)')  # use regex to get the name of the executable made from the Makefile
        match = ex.search(text)
        if match is not None:
            executable = match.group(1)  # set the name of the executable as long as it is able to find it
        else:
            list_final.append(
                'error when executing Makefile... contact your professor about this issue (name of executable can not be found)')
            return 0, list_final

        # ------------------------
        # get the number of test cases to run

        num = re.compile(r'test(\d+):')
        match = num.findall(text)
        if len(match) != 0:
            numberoftestcases = int(match[-1])
        else:
            list_final.append(
                'error when executing Makefile... contact your professor about this issue (number of test cases could not be found)')
            return 0, list_final

        if numberoftestcases == 0:
            list_final.append(
                'error when executing Makefile... contact your professor about this issue (number of test cases is not correct)')
            return 0, list_final

        # ------------------------
        # get the valgrind statements to run

        valgrindstatements = []
        val = re.compile(r'(\./.+)')
        reglist = val.findall(text)
        for elem in reglist:
            valgrindstatements.append(elem.split('>')[0])

    # -------------------------
    # Check diff

    passed = 0
    os.chdir(path)
    with open('empty.txt', 'w+') as f:
        f.write('')

    with open('grade.txt', 'w+') as f:
        f.write('')

    for i in range(1, numberoftestcases + 1):
        # print(f'i is {i}')
        os.system('make clean >/dev/null 2>&1')
        os.system('make >/dev/null 2>&1')
        os.system(
            f'make testcase{i} >/dev/null 2>&1')  # PROF MUST SEND THE OUTPUT OF THE DIFF COMMAND TO grade.txt !!!!!!
        # i can't route the output of the diff command, only the output of the testcase command
        # this must be done by the professor
        # ex) diff output1.txt expected1.txt > grade.txt

        comp = filecmp.cmp('grade.txt', 'empty.txt', shallow=False)
        if comp is True:
            list_final.append("Test case " + str(i) + " is correct!")
            passed += 1
        else:
            list_final.append("Test case " + str(i) + " is wrong...")

    grade_final -= 100 / numberoftestcases * (numberoftestcases - passed)
    list_final.append(f'{passed}/{numberoftestcases} test cases passed!')

    if debugging:
        print('diff finished\nstarting memcheck')

    # ----------------------------
    # Check memory

    bytesLeaked, blocksLeaked = memcheck(path, valgrindstatements)
    # print(bytesLeaked)
    if bytesLeaked < 0:
        list_final.append('error when executing Makefile... contact your professor about this issue')
        return 0, list_final
    # else:
    #     list_final.append('makefile executed correctly!')

    if bytesLeaked > 0:
        list_final.append(f'{bytesLeaked} byte(s) of memory leak present in the program')
        grade_final -= bytesLeaked
    if bytesLeaked == 0:
        list_final.append('No memory leak!')

    if debugging:
        print('memcheck finished')

    if grade_final < 0:
        grade_final = 0

    os.system('make clean >/dev/null 2>&1')
    os.remove('grade.txt')
    os.remove('empty.txt')

    return grade_final, list_final


def memcheck(makefile_dir, valgrindstatements):
    """
    :param makefile_dir: full directory to the makefile (doarts with a '/' and does not include the makfile)
    :type makefile_dir: str
        example: /users/alex/desktop/project14
    :param path_of_testcase: list containing the statements to run valgrind on
    :type path_of_testcase: list
        example: ['./hw14 inputs/input1', ./hw14 inputs/input2]
    :return bytes: bytes of code leaked in the program
    :return blocks: blocks of code that leaked memory
    if the output is -1, -1: the name of the executable cannot be found
    if the output is -2, -2: valgrind was not run correctly (make sure it's installed and working on your computer first)
    """

    os.chdir(makefile_dir)  # go to the folder where the makefile and other files are (essentially the project folder)

    os.system("make >/dev/null 2>&1")  # compiles the code according to the makefile

    tempfile = "tempfile.txt"  # name of the tempfile which will store the valgrind output

    bytesInUse = 0
    blocks = 0

    for statement in valgrindstatements:
        os.system(f'valgrind {statement} > {tempfile} 2>&1')
        # previous statement executes valgrind on the executable and writes the output to the tempfile

        p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')  # regex for getting values from valgrind output

        with open(tempfile, 'r') as f:
            text = f.read()
            match = p.search(text)  # use regex to get number of bytes leaked and in how many blocks
            if match is None:
                return -2, -2  # return this if the valgrind is not called properly (might happen bc i wrote this on mac)
            bytesInUse += int(match.group(1))  # put regex groups from the match into variables and cast to integers
            blocks += int(match.group(2))

        os.remove(tempfile)  # remove the files we created as they only pertain to this function

    return bytesInUse, blocks
