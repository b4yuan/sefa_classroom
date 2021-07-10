#this file will run all the functions
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.cloneFromRepos import cloneFromRepos
from functions.startGradingProcess import startGradingProcess
from functions.putGradesInRepos import putGradesInRepos
from functions.pushChangeToRepos import pushChangeToRepos
from functions.startGradingProcess import startGradingProcessModified
from functions.putGradesInCSV import putGradesInCSV

import os

#variables
testFile = "testJSON.json"
hwName = "hw02sort"
graderFile = "run_grader.py" #file name of grading function
gradeName = "grade.txt"
organization = "cam2testclass"
tagName = "final_ver"
authName = "myers395"
authKey = "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"
profFiles = "/profFiles"
gradeRoot = "/grades"
clonesRoot = "/clones"

#running functions
[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 
    #fetchRepos returns json file of repos, then fetchLists returns list of students in class and lists of homeworks that exist
[clonedRepos, hoursLateArr] = cloneFromRepos(organization, repos, hwName, tagName, authName, authKey, profFiles)
    #[repos cloned to the server at this step, each repo and it's hours late]
    #clones all repositories of students with the specified homework name and tag
startGradingProcessModified(clonedRepos, hoursLateArr)
    #fake grading function that just creates grade.txt file in the a grades folder
print('\nran startGradingProcessModified\n')
putGradesInRepos(gradeRoot, gradeName, clonedRepos)
    #puts grade.txt file into the cloned repositories
print('\nran putGradesInRepos\n')

putGradesInCSV(profFiles, gradeRoot, gradeName, clonedRepos, hws, students)
    #adds new hws and students to a csv
    #uses the grade directory to modify data points
print('\nran putGradesInCSV\n')

pushChangeToRepos(clonesRoot, "grade.txt", clonedRepos, hwName)
    #pushes the grade.txt file to remote repositories
print('\nran pushChangeToRepos\n')
