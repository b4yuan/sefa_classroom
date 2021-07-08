import subprocess
import os

def startGradingProcess(runFilePath):
	subprocess.run(["python3", runFilePath], check=True, stdout=subprocess.PIPE).stdout
	testFile = "testJSON.json"

def startGradingProcessModified(students, hwName):
	#creates grade.txt as test
	for user in students:
		owd = os.getcwd()
		path = owd + "/grades/" + hwName + "-" + user
		os.makedirs(path)
		path = path + '/grade.txt'
		file1 = open(path, "w")
		file1.close()
		print('grade.txt created at ' + path)