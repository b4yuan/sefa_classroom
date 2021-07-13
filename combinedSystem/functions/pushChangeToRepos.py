import os
import subprocess

def pushChangeToRepos(rootPath, fileName, repos, hwName):
	for repo in repos:
		srcPath = os.getcwd() + rootPath + "/" + repo #rootPath + "/" + user + "/" + fileName

		if os.path.exists(srcPath):
			originalDir = os.getcwd()
			os.chdir(str(srcPath))	
			subprocess.run(["git", "add", fileName], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "commit", "-m", str("Grades updated for " + hwName + ".")], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "push", "origin", "HEAD:refs/heads/master", "--force"], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "tag", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #adds graded version tag
			subprocess.run(["git", "push", "origin", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #need to push the tag specifically, will not update tag with just a general push command
			os.chdir(originalDir)
	
		else:
			print("The directory " + srcPath + " does not exist.")