import subprocess
import os
import random #for testing purposes

def startGradingProcess(runFilePath):
	graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort.zip'), os.path.join(path, '2020homeworks/HW02Sort'))
	obj = GradedSubmission()
	grade = obj.get_grade() #returns a float that is rounded to two decimals
	feedback = obj.get_error_list() #returns a list
	#need to write it to a file - grade and feedback in one file

def startGradingProcessModified(repos, hoursLate):
	#creates grade.txt as test
	for repo in repos:
		owd = os.getcwd()
		path = owd + "/grades/" + repo
		os.makedirs(path)
		path = path + '/grade.txt' #gradeReport.txt
		file1 = open(path, "w")
		file1.write(str(random.randrange(0,100)/100.)) #random percentage for testing
		file1.close()
		print('grade.txt created at ' + path)