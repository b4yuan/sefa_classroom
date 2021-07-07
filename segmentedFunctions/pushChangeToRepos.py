import subprocess
import json
import os
import re
import shutil
import calcHoursLate


def pushChangeToRepos(rootPath, fileName, userList, hwName):
	for user in userList:
		srcPath = fileName #rootPath + "/" + user + "/" + fileName

		if os.path.exists(srcPath):
			subprocess.run(["git", "add", srcPath], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "commit", "-m", str("Grades updated for " + hwName + ".")], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "push"], check=True, stdout=subprocess.PIPE).stdout
			subprocess.run(["git", "tag", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #adds graded version tag
			subprocess.run(["git", "push", "origin", "graded_ver"], check=True, stdout=subprocess.PIPE).stdout #need to push the tag specifically, will not update tag with just a general push command
		else:
			print("The directory " + srcPath + " does not exist.")

