#this file will run all the functions
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.cloneFromRepos import cloneFromRepos
from functions.startGradingProcess import startGradingProcess
from functions.putGradesInRepos import putGradesInRepos
from functions.pushChangeToRepos import pushChangeToRepos
from functions.startGradingProcess import startGradingProcessModified

#variables
testFile = "testJSON.json"
hwName = "hw02sort"
graderFile = "run_grader.py" #file name of grading function
gradeName = "grade.txt"
gradeRoot = "/grades"
organization = "cam2testclass"
tagName = "final_ver"
authName = "myers395"
authKey = "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"

#running functions
[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 
    #fetchRepos returns ?, then fetchLists returns list of students in class and lists of homeworks that exist
hoursLateArr = cloneFromRepos(organization, repos, hwName, tagName, authName, authKey)
    #clones all repositories of students with the specified homework name and tag

startGradingProcessModified(students, hwName)
    #fake grading function that just creates grade.txt file in the a grades folder
print('\nran startGradingProcessModified\n')
putGradesInRepos(gradeRoot, gradeName, students, hwName)
    #puts grade.txt file into the cloned repositories
print('\nran putGradesInRepos\n')
pushChangeToRepos("repos", "grade.txt", students, hwName)
    #pushes the grade.txt file to remote repositories
print('\nran pushChangeToRepos\n')
