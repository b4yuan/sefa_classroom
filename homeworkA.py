import subprocess
import json
import os
import re
import shutil

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
	usernames = []
	with open(JSONFile, "r") as JFile:
		extractRawJSON = json.load(JFile)
		for dictionaries in extractRawJSON:
			for flags in dictionaries:
				if(flags == "names"):
					usernames.append(dictionaries[flags])
	return usernames

def getRepoCloneURLSFromJSON(JSONFile):
	repositoryURLS = []
	with open(JSONFile, "r") as JFile:
		extractRawJSON = json.load(JFile)
		for dictionaries in extractRawJSON:
			for flags in dictionaries:
				if(flags == "clone_url"):
					repositoryURLS.append(dictionaries[flags])
	return repositoryURLS

def pullFileFromAllRepos(repositories, fileToPull):
	for reposURL in repositories:
		splitURL = reposURL.split("/")
		reposFileWithGit = splitURL[len(splitURL) - 1].split(".")
		reposFile = reposFileWithGit[0]
		reposLinkWithGit = reposURL.split(".git")
		reposLink = reposLinkWithGit[0]
		if os.path.exists(reposFile):
			rootDir = os.getcwd()
			os.chdir(str(rootDir + "/" + reposFile))
			subprocess.run(["git", "fetch"], check=True, stdout=subprocess.PIPE).stdout
 
			process = subprocess.run(["git", "checkout", fileToPull], check=True, stdout=subprocess.PIPE).stdout
			os.chdir(rootDir)
		else:
			process = subprocess.run(["git", "clone", str(reposURL)], check=True, stdout=subprocess.PIPE).stdout

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
		else:
			print("The directory " + srcPath + " does not exist.")

def startGradingProcess(runFilePath):
	subprocess.run(["python3", "pas_backend/run_grader.py"], check=True, stdout=subprocess.PIPE).stdout
	
#pullFileFromAllRepos(getRepoCloneURLSFromJSON(example.json), "HW01Linux")
