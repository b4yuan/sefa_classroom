import numpy as np
import pandas as pd
import os
import re
from functions.dataFrameHelper import *

def putGradesInCSV(profFiles, rootDirGrades, fileName, repos, hws, students):
    owd = os.getcwd() # get working directory
    if (os.path.exists(owd + profFiles) and os.path.exists(owd + rootDirGrades)):
        df = loadCSV(owd + profFiles + "/masterGrades.csv") 
        template = re.compile('^([a-zA-Z0-9]+)[-]([a-zA-Z0-9]+)$') # regex template for getting hw and student from repo name
        df = updateDF(hws, students, df) # adding rows and columns based on new students and hws in the class
        for repo in repos:
            srcPath = str(owd + rootDirGrades + "/" + repo + "/" + fileName)
            # srcPath = str(rootDirGrades + "/" + repo + "/" + fileName) for testing
            match = re.fullmatch(template, repo) # match template with repository name
            if os.path.exists(str(srcPath)):
                grade = open(srcPath, "r").read() # open grade file
                df = editEntry(float(grade), match[2], match[1], df) # add grade to respective hw and student
            else:
                print("Grade does not exist: " +  str(srcPath))
        writeCSV(owd + profFiles + "/masterGrades.csv", df)
    else:
        print("Path Missing: " + str(rootDirGrades) + " or " + str(profFiles))


# if __name__ == "__main__": for testing
#     repos = ['hw02sort-kmerrill16', 'hw02sort-lvy15']
#     hws = ['hw02sort', 'hw03cake']
#     students = ['kmerrill16', 'lvy15']
#     putGradesInCSV("/mnt/c/Users/Jack/Documents/pas_githubclassroom/combinedSystem/profFiles", "/mnt/c/Users/Jack/Documents/pas_githubclassroom/combinedSystem/grades", "grade.txt", repos, hws, students)