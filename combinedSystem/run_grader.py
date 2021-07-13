import os

def run_grader(students, hwName):
    #creates grade.txt as test
    for user in students:
        path = "combinedSystem/grades" + hwName + "-" + user + '/grade.txt'
        file1 = open(path, "w")
        file1.write("file information")
        file1.close()
    print("graded")

