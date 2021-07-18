from functions.rmtree import rmtree
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.fetchTags import fetchTags
from functions.getConfigInputs import getConfigInputs
from functions.createJSONFiles import getHomeworkList, isAValidHomework
from functions.hwNameHelper import stripHW, matchHW

import argparse
import os
import subprocess

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

#!!----------Set Up Command Line Flag Input--------!!
parser = argparse.ArgumentParser("specify homework assignments to grade")
group = parser.add_mutually_exclusive_group()
group.add_argument("--hw_name", type = str, help= "specify the name of the homework to grade. example: python3 runSystem.py --hw_name hw02sort")
group.add_argument("--hw_range", type = str, nargs = 2, help = "specify a range of homeworks to grade. example: python3 runSystem.py --hw_range hw02sort hw04file")
args = parser.parse_args()

homeworkMasterList = getHomeworkList(os.path.join(os.getcwd() + '/profFiles'))

#!!------Checking argument inputs-----!!
if args.hw_range is not None:
    if isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[0]: 
        startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[1]
    else:
        print('Your start range homework name was not valid')
        raise Exception('Invalid Homework Name')

    if isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[0]: 
        endIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[1]
    else:
        print('Your end range homework name was not valid')
        raise Exception('Invalid Homework Name')
else: 
    if isAValidHomework(os.getcwd() + profFiles, args.hw_name)[0]:
        startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_name)[1]
    else:
        print('Your homework name was not valid')
        raise Exception('Invalid Homework Name')
    endIndex = startIndex

#!!----Get lists----!!
[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 

for x in range(startIndex, endIndex + 1): #for each homework
    hwName = homeworkMasterList[x]
    hwNum = stripHW(hwName)
    print('\nResetting hw ', hwName, '\n')

    for repo in repos: #for each repository
        if matchHW(hwNum, repo):
            #!!----Check for local repository and clone if does not exist----!!
            owd = os.getcwd()

            print('Resetting repo', repo)
            
            dirPath = "/clones/" + repo
            repoURL = "https://" + authKey + '@github.com/' + organization + '/' + repo + '.git'

            if not os.path.exists(owd + '/' + clonesRoot): #if cloned repo doesn't exist, clone
                os.mkdir(owd + '/clones')
            
            os.chdir(owd + '/clones')

            tagList = fetchTags(organization, repo, authName, authKey)

            if not os.path.exists(owd + dirPath) and 'final_ver' in tagList:
                subprocess.run(["git", "clone", "-b", tagName, str(repoURL)]) #clone repo
                os.chdir(owd + dirPath)

            #!!----Delete graded tag-----!!
            tagList = fetchTags(organization, repo, authName, authKey)
            if 'graded_ver' in tagList:
                subprocess.run(["git", "push", "-d", repoURL, "graded_ver"], check=True, stdout=subprocess.PIPE).stdout
            else:
                print('\nNo tag to delete\n')
                
            #!!-----Remove grade report----!!
            if os.path.exists(owd + dirPath + '/' + gradeFileName):
                os.remove(owd + dirPath + '/' + gradeFileName)
                subprocess.run(["git", "add", gradeFileName], check=True, stdout=subprocess.PIPE).stdout
                subprocess.run(["git", "commit", "-m", "deleted gradeReport.txt"], stdout=subprocess.PIPE).stdout
                subprocess.run(["git", "push", "origin", "HEAD:refs/heads/master", "--force"], check=True, stdout=subprocess.PIPE).stdout
                print('\nDeleted grade file for', repo, '\n')
            
            os.chdir(owd)


if os.path.exists('clones'):
    rmtree('clones') 
    print('Deleted clones')
        #removes all cloned folders
if os.path.exists('grades'):
    rmtree('grades')
    print('Deleted grades')
        #removes folder of grades
if os.path.exists('filteredOutput.txt'):
    os.remove('filteredOutput.txt')
    print('Deleted output file')
