import shutil
import os

def putGradesInRepos(rootDirGrades, fileName, repos):
	for repo in repos:
		owd = os.getcwd()
		srcPath = str(owd + rootDirGrades + "/" + repo + "/" + fileName)
		dstPath = str(owd + "/clones/" + repo)
		if os.path.exists(str(srcPath)) and os.path.exists(str(dstPath)):
			shutil.copy(srcPath, dstPath)
		else:
			print("One of these directories does not exist: " +  str(srcPath) + " or " + str(dstPath))