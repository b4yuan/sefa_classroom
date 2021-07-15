#this file will run all the functions
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.cloneFromRepos import cloneFromRepos
from functions.putGradesInRepos import putGradesInRepos
from functions.pushChangeToRepos import pushChangeToRepos
from functions.startGradingProcess import startGradingProcess
from functions.putGradesInCSV import putGradesInCSV
from functions.getConfigInputs import getConfigInputs
from functions.createJSONFiles import findDirs

import argparse
import os

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

<<<<<<< HEAD
#!!----------Set Up Command Line Flag Input--------!!

homeworkMasterList = findDirs(os.path.join(os.getcwd() + profFiles), 'HWDirNames')

parser = argparse.ArgumentParser("specify homework assignments to grade")
group = parser.add_mutually_exclusive_group()
group.add_argument("--hw_name", type = str, help= "specify the name of the homework to grade. example: python3 runSystem.py --hw_name hw02sort")
group.add_argument("--hw_range", type = str, nargs = 2, help = "specify a range of homeworks to grade. example: python3 runSystem.py --hw_range hw02sort hw04file")
group.add_argument("--grade_all", action="store_true", help = "specify this option to grade all homeworks. example: python3 runSystem.py --grade_all")
args = parser.parse_args()

if args.grade_all == True:
    print('Grading a range of hws')
    startIndex = 0
    endIndex = len(homeworkMasterList) - 1
elif args.hw_range is not None:
    print('Grading a range of hws')
    startIndex = homeworkMasterList.index(args.hw_range[0])
    endIndex = homeworkMasterList.index(args.hw_range[1])
else:
    startIndex = homeworkMasterList.index(args.hw_name)
    endIndex = startIndex

#!!----------Run Actual System--------!!

for x in range(startIndex, endIndex+1):
    hwName = homeworkMasterList[x]
    print('Currently grading :', hwName)

    #!!----------Collect List of Students, Homeworks, and Repositories--------!!
    [students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey))  #fetchRepos returns json file of repos, then fetchLists returns list of students in class and lists of homeworks that exist
    
    #!!----------Clone Appropriate Repositories--------!!
    [clonedRepos, hoursLateArr] = cloneFromRepos(organization, repos, hwName, tagName, authName, authKey, profFiles, clonesRoot)
        #[repos cloned to the server at this step, each repo and its hours late]
        #clones all repositories of students with the specified homework name and tag

    #!!---------Run Grading Script--------!!
    startGradingProcess(clonedRepos, hoursLateArr, homeworkMasterList[x])
    print('\nran startGradingProcess\n')

    #!!---------Put Grade Text File Into Cloned Repos--------!!
    putGradesInRepos(gradeRoot, gradeFileName, clonedRepos)
    print('\nran putGradesInRepos\n')

    #!!---------Add Grades to CSV For Prof Access--------!!
    putGradesInCSV(profFiles, gradeRoot, gradeFileName, clonedRepos, hws, students)
        #adds new hws and students to a csv
        #uses the grade directory to modify data points
    print('\nran putGradesInCSV\n')

    #!!---------Push Grade File to Student Repos--------!!
    pushChangeToRepos(clonesRoot, gradeFileName, clonedRepos, hwName, organization)
        #also adds graded_ver tag
    print('\nran pushChangeToRepos\n')

=======
#running functions
[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 
print(students)
    #fetchRepos returns json file of repos, then fetchLists returns list of students in class and lists of homeworks that exist
[clonedRepos, hoursLateArr] = cloneFromRepos(organization, repos, hwName, tagName, authName, authKey, profFiles, clonesRoot)
    #[repos cloned to the server at this step, each repo and its hours late]
    #clones all repositories of students with the specified homework name and tag
startGradingProcess(clonedRepos, hoursLateArr, hwName)
    #fake grading function that just creates grade.txt file in the a grades folder
print('\nran startGradingProcess\n')

putGradesInRepos(gradeRoot, gradeFileName, clonedRepos)
    #puts grade.txt file into the cloned repositories
print('\nran putGradesInRepos\n')

putGradesInCSV(profFiles, gradeRoot, gradeFileName, clonedRepos, hws, students)
    #adds new hws and students to a csv
    #uses the grade directory to modify data points
print('\nran putGradesInCSV\n')

pushChangeToRepos(clonesRoot, gradeFileName, clonedRepos, hwName, organization)
    #pushes the grade.txt file to remote repositories
print('\nran pushChangeToRepos\n')
>>>>>>> 89d3b256709ffb6ecd56e9c477b1c04065413065
