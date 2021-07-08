#this file will run all the functions
from functions.rmtree import rmtree
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
rmtree('clones') 
    #removes all cloned folders
rmtree('grades')
    #removes folder of grades

[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 
print(students)
    #fetchRepos returns ?, then fetchLists returns list of students in class and lists of homeworks that exist
hoursLateArr = cloneFromRepos(organization, repos, hwName, tagName, authName, authKey)
    #clones all repositories of students with the specified homework name and tag


startGradingProcessModified(students, hwName)
print('\nran startGradingProcessModified\n')
putGradesInRepos(gradeRoot, gradeName, students, hwName)
print('\nran putGradesInRepos\n')
pushChangeToRepos("repos", "grade.txt", students, hwName)
print('\nran pushChangeToRepos\n')
