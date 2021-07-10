import subprocess
import os
import random #for testing purposes

def startGradingProcess(runFilePath):
	subprocess.run(["python3", runFilePath], check=True, stdout=subprocess.PIPE).stdout
	testFile = "testJSON.json"

def startGradingProcessModified(repos, hoursLate):
	#creates grade.txt as test
	for repo in repos:
		owd = os.getcwd()
		path = owd + "/grades/" + repo
		os.makedirs(path)
		path = path + '/grade.txt'
		file1 = open(path, "w")
		file1.write(str(random.randrange(0,100)/100.)) #random percentage for testing
		file1.close()
		print('grade.txt created at ' + path)