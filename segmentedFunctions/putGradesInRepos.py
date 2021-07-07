import subprocess
import json
import os
import re
import shutil
import calcHoursLate

def putGradesInRepos(rootDirGrades, fileName, userList, rootDirRepos, hwName):
	for user in userlist:
		srcPath = rootDirGrades + "/" + user + "/" + hwName + "/" + fileName
		dstPath = rootDirRepos + "/" + user + "/" + hwName + "/" + fileName
		if os.path.exists(srcPath) and os.path.exists(dstPath):
			shutil.copy(srcPath, dstPath)
		else:
			print("One of these directories does not exist: " +  str(srcPath) + " or " + str(dstPath))


