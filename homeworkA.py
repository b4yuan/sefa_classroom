import subprocess
import json
import os
import re
import shutil
import calcHoursLate.py

def getFlagFromJSON(JSONFile, flag):
	flag = []
	with open(JSONFile, "r") as JFile:
		extractRawJSON = json.load(JFile)
		for dictionaries in extractRawJSON:
			for flags in dictionaries:
				if(flags == flag):
					flag.append(dictionaries[flags])
	return flag

def getRepoNamesFromJSON(JSONFile):
	usernames = getFlagFromJSON(JSONFile, "names")
	return usernames

def getRepoCloneURLSFromJSON(JSONFile):
	repositoryURLS = getFlagFromJSON(JSONFile, "clone_url")
	return repositoryURLS

def pullFileFromAllRepos(repositories, fileToPull):
    hoursLateArr = []
	for reposURL in repositories:
		splitURL = reposURL.split("/")
		reposFileWithGit = splitURL[len(splitURL) - 1].split(".")
		reposFile = reposFileWithGit[0]
		reposLinkWithGit = reposURL.split(".git")
		reposLink = reposLinkWithGit[0]
		tagList = fetchTagList(reposURL) #uses URL for a function that analyzes json file to get list of tags that exist for repo
		if os.path.exists(reposFile):
			rootDir = os.getcwd()
			os.chdir(str(rootDir + "/" + reposFile))
			subprocess.run(["git", "fetch"], check=True, stdout=subprocess.PIPE).stdout
 
			process = subprocess.run(["git", "checkout", fileToPull], check=True, stdout=subprocess.PIPE).stdout
			os.chdir(rootDir)
		else:
			if 'final_ver' in tagList and 'graded_ver' not in tagList:
				#clones the directory only if final tag exists and it hasn't been graded yet
				process = subprocess.run(["git", "clone", str(reposURL)], check=True, stdout=subprocess.PIPE).stdout
                
                os.chdir(reposURL) #navigate to cloned repo
                info = subprocess.check_output('git log -1 --format=%ai ver_1').decode()
                subDate =info.split(' ')[0] + ' ' + info.split(' ')[1]
                hoursLate = calcHoursLate(subDate, dueDate) #still need to get the due date from somewhere
                hoursLateArr.append([reposURL, hoursLate]) #2d array with repository URL and number of hours late

    return hoursLateArr

def putGradesInRepos(rootDirGrades, fileName, userList, rootDirRepos, hwName):
	for user in userlist:
		srcPath = rootDirGrades + "/" + user + "/" + hwName + "/" + fileName
		dstPath = rootDirRepos + "/" + user + "/" + hwName + "/" + fileName
		if os.path.exists(srcPath) and os.path.exists(dstPath):
			shutil.copy(srcPath, dstPath)
		else:
			print("One of these directories does not exist: " +  str(srcPath) + " or " + str(dstPath))

def pushChangeToRepos(rootPath, fileName, userList, hwName):
	for user in userList:
		srcPath = rootPath + "/" + user + "/" + fileName
		if os.path.exists(srcPath):
			subprocess.run(["git", "add", srcPath], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "commit", "-m", str("Grades updated for " + hwName + ".")], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "push"], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "tag", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #adds graded version tag
			subprocess.run(["git", "push", "origin", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #need to push the tag specifically, will not update tag with just a general push command
		else:
			print("The directory " + srcPath + " does not exist.")
def getTimesLateFromFile(JSONFile, dueDate):
	tags = getFlagFromJSON(JSONFile, "tag")
	timesLate = []
	for tag in tags:
		timesLate.append(calcHoursLate(tag, dueDate))
        return timesLate
def deleteAllRepos(repoFileNames):
	for repos in repoFileNames:
			subprocess.run(["rm", repos], check=True, stdout=subprocess.PIPE).stdout 
def startGradingProcess(runFilePath):
	subprocess.run(["python3", "pas_backend/run_grader.py"], check=True, stdout=subprocess.PIPE).stdout
	
#pullFileFromAllRepos(getRepoCloneURLSFromJSON(example.json), "HW01Linux")
