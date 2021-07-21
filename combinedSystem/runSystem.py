#!!--------Imports-----------!!
from functions.setup import getConfigInputs, argParse
from functions.fetch import fetchLists, fetchRepos, fetchHWInfo, fetchLimit
from functions.dataFrameHelper import updateDF, loadCSV, writeCSV
from functions.gradeProcess import cloneFromRepos, startGradingProcess, putGradesInRepos, putGradesInCSV, pushChangeToRepos
from functions.rmtree import rmtree

import argparse, os
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
profDir = "/profFiles"
gradesDir = "/grades"
clonesDir = "/clones"

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

[startIndex, endIndex, homeworkMasterList] = argParse(args, profDir, outputFile)

#!!----------Run Actual System--------!!
[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey))  #fetchRepos returns json file of repos, then fetchLists returns list of students in class and lists of homeworks that exist
[usedStart, remaining] = fetchLimit(authName, authKey) #Used for tracking requests, can be deleted

for x in range(startIndex, endIndex + 1): #for each homework
    hwName = homeworkMasterList[x]
    hwNum = fetchHWInfo(None, hwName)[1]
    outputFile.write('\n[[Currently grading : '+ hwName + ']]')

    #!!----------Collect List of Students, Homeworks, and Repositories--------!!
    df = loadCSV(os.getcwd() + profDir + "/masterGrades.csv")
    df = updateDF(hws, students, df) # adding rows and columns based on new students and hws in the class
    writeCSV(os.getcwd() + profDir + "/masterGrades.csv", df)

    #!!----------Clone Appropriate Repositories--------!!
    for repo in repos: #for each repo
        [needsToBeGraded, hoursLate] = cloneFromRepos(organization, repo, hwNum, tagName, authName, authKey, profDir, clonesDir, outputFile)
        #[repos cloned to the server at this step, each repo and its hours late]
        #clones all repositories of students with the specified homework name and tag

        if (needsToBeGraded == True):
            #!!---------Run Grading Script--------!!
            startGradingProcess(repo, hoursLate, homeworkMasterList[x], outputFile, gradesDir, clonesDir, profDir)
            outputFile.write('\n\nSuccessfully ran startGradingProcess\n')

            #!!---------Put Grade Text File Into Cloned Repos--------!!
            putGradesInRepos(gradesDir, clonesDir, gradeFileName, repo)
            outputFile.write('\nSuccessfully ran putGradesInRepos\n')

            #!!---------Add Grades to CSV For Prof Access--------!!
            putGradesInCSV(profDir, gradesDir, gradeFileName, repo)
                #adds new hws and students to a csv
                #uses the grade directory to modify data points
            outputFile.write('\nSuccessfully ran putGradesInCSV\n')

            #!!---------Push Grade File to Student Repos--------!!
            pushChangeToRepos(clonesDir, gradeFileName, repo)
                #also adds graded_ver tag
            outputFile.write('\nSuccessfully ran pushChangeToRepos\n')

            #!!---------Remove Local Repository--------!!
            if args.delete != False:
                repoPath = os.getcwd() + clonesDir + '/' + repo
                if os.path.exists(repoPath):
                    rmtree(repoPath)

#!!----------Delete Clones and Grades Folders--------!!
if args.delete != False: #it defaults to true
    if os.path.exists(os.getcwd() + clonesDir):
        rmtree('clones') 
        outputFile.write('\nRemoved clones')
            #removes all cloned folders
    if os.path.exists(os.getcwd() + gradesDir):
        rmtree('grades')
        outputFile.write('\nRemoved grades')
            #removes folder of grades

#!!----------Print Request Limit Info--------!!
[usedFinal, remaining] = fetchLimit(authName, authKey)
outputFile.write('\n\nRequests Used this Runtime: ' + str(usedFinal - usedStart) + '\nHourly Requests Left: ' + str(remaining) + '\n')

#!!----------Close Output File--------!!
outputFile.write('\n***Finished grading process***')
outputFile.close()