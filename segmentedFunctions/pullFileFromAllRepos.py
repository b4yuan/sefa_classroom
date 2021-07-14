import subprocess
import json
import os
import re
import shutil
import calcHoursLate

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


