#!!--------Imports-----------!!
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.fetchTags import fetchTags
from functions.cloneFromRepos import cloneFromRepos
from functions.putGradesInRepos import putGradesInRepos
from functions.pushChangeToRepos import pushChangeToRepos
from functions.startGradingProcess import startGradingProcess
from functions.putGradesInCSV import putGradesInCSV
from functions.getConfigInputs import getConfigInputs
from functions.argParse import argParse
from functions.rmtree import rmtree
from functions.hwNameHelper import stripHW
from functions.dataFrameHelper import *

import argparse
import os
import sys
from datetime import datetime

#!!--------Set Up Variables From JSON File-----------!! 
#Configname
configJSON = "/profFiles/config.json"
#get variables from JSON config file
configInputs = getConfigInputs(configJSON)

#variables
organization =  configInputs["organization"]  #json file
authName = configInputs["authName"] #json file
authKey = configInputs["authKey"] #json file

tagName = "final_ver"
gradeFileName = "gradeReport.txt"
profFiles = "/profFiles"
gradeRoot = "/grades"
clonesRoot = "/clones"

#!!----------Set Up File For Collecting Output------!!
outputFile = open('filteredOutput.txt', 'w')
outputFile.write("Ran on ")
outputFile.write(datetime.now().strftime("%m-%d %H:%M:%S") + "\n")

#!!----------Set Up Command Line Flag Input--------!!
parser = argparse.ArgumentParser("specify homework assignments to grade")
group = parser.add_mutually_exclusive_group()
group.add_argument("--hw_name", type = str, help= "specify the name of the homework to grade. example: python3 runSystem.py --hw_name hw02sort")
group.add_argument("--hw_range", type = str, nargs = 2, help = "specify a range of homeworks to grade. example: python3 runSystem.py --hw_range hw02sort hw04file")
group.add_argument("--grade_all", action="store_true", help = "specify this option to grade all homeworks. example: python3 runSystem.py --grade_all")
parser.add_argument("-d", "--delete", action ="store_false", help="specify this option if you would like to NOT delete clones and grades folders after running. default is true")
args = parser.parse_args()

[startIndex, endIndex, homeworkMasterList] = argParse(args, profFiles, outputFile)

#!!----------Run Actual System--------!!
for x in range(startIndex, endIndex + 1): #for each homework
    hwName = homeworkMasterList[x]
    hwNum = stripHW(hwName)
    outputFile.write('\n[[Currently grading : '+ hwName + ']]')

    #!!----------Collect List of Students, Homeworks, and Repositories--------!!
    [students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey))  #fetchRepos returns json file of repos, then fetchLists returns list of students in class and lists of homeworks that exist
    df = loadCSV(os.getcwd() + profFiles + "/masterGrades.csv")
    df = updateDF(hws, students, df) # adding rows and columns based on new students and hws in the class
    writeCSV(os.getcwd() + profFiles + "/masterGrades.csv", df)

    #!!----------Clone Appropriate Repositories--------!!
    for repo in repos: #for each repo
        [needsToBeGraded, hoursLateArr] = cloneFromRepos(organization, repo, hwNum, tagName, authName, authKey, profFiles, clonesRoot, outputFile)
        #[repos cloned to the server at this step, each repo and its hours late]
        #clones all repositories of students with the specified homework name and tag

        if (needsToBeGraded == True):
            #!!---------Run Grading Script--------!!
            startGradingProcess(repo, hoursLateArr, homeworkMasterList[x], outputFile)
            outputFile.write('\n\nSuccessfully ran startGradingProcess\n')

            #!!---------Put Grade Text File Into Cloned Repos--------!!
            putGradesInRepos(gradeRoot, gradeFileName, repo)
            outputFile.write('\nSuccessfully ran putGradesInRepos\n')

            #!!---------Add Grades to CSV For Prof Access--------!!
            putGradesInCSV(profFiles, gradeRoot, gradeFileName, repo)
                #adds new hws and students to a csv
                #uses the grade directory to modify data points
            outputFile.write('\nSuccessfully ran putGradesInCSV\n')

            #!!---------Push Grade File to Student Repos--------!!
            pushChangeToRepos(clonesRoot, gradeFileName, repo)
                #also adds graded_ver tag
            outputFile.write('\nSuccessfully ran pushChangeToRepos\n')

            #!!---------Remove Local Repository--------!!
            if args.delete != False:
                repoPath = os.getcwd() + clonesRoot + "/" + repo
                if os.path.exists(repoPath):
                    rmtree(repoPath)

#!!----------Delete Clones and Grades Folders--------!!
if args.delete != False: #it defaults to true
    if os.path.exists('clones'):
        rmtree('clones') 
        sys.stdout.write('\nRemoved clones')
            #removes all cloned folders
    if os.path.exists('grades'):
        rmtree('grades')
        sys.stdout.write('\nRemoved grades')
            #removes folder of grades

#!!----------Close Output File--------!!
outputFile.write('\n***Finished grading process***')
outputFile.close()