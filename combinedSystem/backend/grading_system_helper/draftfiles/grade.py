import os
from distutils.ccompiler import new_compiler
import filecmp
import re


# input: a string which is student file pass
# output: a tuple that has <grade, a list about feedback(each element is a string)>
def grade(path, pathin, pathout, makefile):
    """
    :param path: path to the project. ex) /users/alex/myfiles/project
    :type path: str
    :param pathin: path to the expected input files. ex) /users/alex/myfiles/project/inputs
    :type pathin str
    :param pathout: path to the expected output files. ex) /users/alex/myfiles/project/outputs
    :type pathout str
    :param makefile: path to the expected makefile. ex) /users/alex/makefiles/project1
    :type makefile str
    :return: grade, feedback
    """
    list_final = []
    grade_final = 100

    # if a makefile is not specified, then it is assumed that the student has made one
    # if a make file is specified, then it writes the makefile into the folder
    if makefile != 0:
        with open(makefile, 'r') as make:
            makefiletext = make.read()

        os.chdir(path)
        with open('makefile', 'w+') as make:
            make.write(makefiletext)

    print('starting compile')
    # check that everything can compile
    compiler = new_compiler()
    for filename in os.listdir(path):
        if filename.endswith(".c"):  # suppose c file
            try:
                compiler.compile([filename])
                list_final.append(f'{filename} compiled correctly!')

            except:
                list_final.append(f'{filename} did not compile correctly...')
                return 0, list_final
        else:
            continue
    print('compile finished\nstarting diff')

    # Check diff
    inputfiles = os.listdir(pathin)
    inputfiles.sort()
    outputfiles = os.listdir(pathout)
    outputfiles.sort()

    with open("makefile", 'r') as f:  # open the makefile
        text = f.read()
        ex = re.compile(r'-o (\w+)')  # use regex to get the name of the executable made from the makefile
        match = ex.search(text)
        if match is not None:
            executable = match.group(1)  # set the name of the executable as long as it is able to find it
        else:
            list_final.append('name of executable could not be found')
            return 0, list_final

    passed = 0
    for i in range(len(inputfiles)):
        os.chdir(path)
        os.system('make clean >/dev/null 2>&1')
        os.system('make >/dev/null 2>&1')
        os.system(f'./{executable} {pathin}/{inputfiles[i]} > temp.txt')
        comp = filecmp.cmp('temp.txt', f'{pathout}/{outputfiles[i]}', shallow=False)
        if comp is True:
            list_final.append("Test case " + str(i + 1) + " is correct!")
            passed += 1
        else:
            list_final.append("Test case " + str(i + 1) + " is wrong...")

    grade_final -= 100/len(inputfiles) * (len(inputfiles) - passed)
    list_final.append(f'{passed}/{len(inputfiles)} test cases passed!')

    print('diff finished\nstarting memcheck')

    # Check memory
    for inputfile in inputfiles:
        os.system('make clean >/dev/null 2>&1')
        bytesLeaked, blocksLeaked = memcheck(path, f'{pathin}/{inputfile}')

        if bytesLeaked < 0:
            list_final.append('error when executing makefile...')
            return 0, list_final
        else:
            list_final.append('makefile executed correctly!')

    if bytesLeaked > 0:
        list_final.append(f'{bytesLeaked} byte(s) of memory leak was present in the program')
        grade_final -= bytesLeaked
    if bytesLeaked == 0:
        list_final.append('No memory leak!')

    print('memcheck finished')

    if grade_final < 0:
        grade_final = 0

    os.system('make clean >/dev/null 2>&1')
    os.remove('temp.txt')

    return grade_final, list_final


def memcheck(makefile_dir, path_of_testcase):
    """
    :param makefile_dir: full directory to the makefile (doarts with a '/' and does not include the makfile)
    :type makefile_dir: str
        example: /users/alex/desktop/project14
    :param path_of_testcase: the full path of the testcase (starts with a '/' and includes the file)
    :type path_of_testcase: str
        example: users/alex/desktop/project14/inputs/test1.txt
    :return bytes: bytes of code leaked in the program
    :return blocks: blocks of code that leaked memory

    if the output is -1, -1: the name of the executable cannot be found
    if the output is -2, -2: valgrind was not run correctly (make sure it's installed and working on your computer first)
    """

    if path_of_testcase != 0:
        with open(path_of_testcase) as f:  # open the specified test case
            testcase = f.read()  # read the test case and store the data for later

    os.chdir(makefile_dir)  # go to the folder where the makefile and other files are (essentially the project folder)

    with open("makefile", 'r') as f:  # open the makefile
        text = f.read()
        ex = re.compile(r'-o (\w+)')  # use regex to get the name of the executable made from the makefile
        match = ex.search(text)
        if match is not None:
            executable = match.group(1)  # set the name of the executable as long as it is able to find it
        else:
            return -1, -1  # happens when the name of the executable cannot be found from the makefile

    os.system("make >/dev/null 2>&1")  # compiles the code according to the makefile

    tempfile = "tempfile.txt"  # name of the tempfile which will store the valgrind output
    testfile = "testcase.txt"

    if path_of_testcase != 0:
        with open(testfile, 'w') as f:
            f.write(testcase)  # writes the testcase into a file in the current directory

        os.system("valgrind ./" + executable + " " + testfile + " > " + tempfile + " 2>&1")
        # previous statement executes valgrind on the executable and writes the output to the tempfile
    else:
        os.system("valgrind ./" + executable + " > " + tempfile + " 2>&1")

    p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')  # regex for getting values from valgrind output

    with open(tempfile, 'r') as f:
        text = f.read()
        match = p.search(text)  # use regex to get number of bytes leaked and in how many blocks
        if match is None:
            return -2, -2  # return this if the valgrind is not called properly (might happen bc i wrote this on mac)
        bytesInUse = int(match.group(1))  # put regex groups from the match into variables and cast to integers
        blocks = int(match.group(2))

    os.remove(tempfile)  # remove the files we created as they only pertain to this function
    os.remove(testfile)

    return bytesInUse, blocks
