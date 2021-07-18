import numpy as np
import pandas as pd
import os
import re
from functions.dataFrameHelper import *

def putGradesInCSV(profFiles, rootDirGrades, fileName, repo):
    owd = os.getcwd() # get working directory
    if (os.path.exists(owd + profFiles) and os.path.exists(owd + rootDirGrades)):
        df = loadCSV(owd + profFiles + "/masterGrades.csv") 
        template = re.compile('^([a-zA-Z0-9]+)[-]([a-zA-Z0-9]+)$') # regex template for getting hw and student from repo name
        srcPath = str(owd + rootDirGrades + "/" + repo + "/" + fileName)
        match = re.fullmatch(template, repo) # match template with repository name
        if os.path.exists(str(srcPath)):
            grade = open(srcPath, "r").readlines()[2] # open grade file, get the first line
            grade = grade.split(" ")[1].split("%")[0] #retrives just the number from the text file
            df = editEntry(float(grade), match[2], match[1], df) # add grade to respective hw and student
        else:
            print("Grade does not exist: " +  str(srcPath))
        writeCSV(owd + profFiles + "/masterGrades.csv", df)
    else:
        print("Path Missing: " + str(rootDirGrades) + " or " + str(profFiles))
