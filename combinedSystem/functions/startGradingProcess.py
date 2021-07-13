import subprocess
import os
import random #for testing purposes

def startGradingProcess(repos):
	for repo in repos:
		owd = os.getcwd()
		path = owd + "/grades/" + repo
		os.makedirs(path) #creates repository folder in grades folder
		path = path + '/gradeReport.txt'

		#graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort.zip'), os.path.join(path, '2020homeworks/HW02Sort'))
		#obj = GradedSubmission()
		grade = 34.34; # obj.get_grade() #returns a float that is rounded to two decimals
		feedback = ["error on line 2", "something else is wrong"] #obj.get_error_list() #returns a list

		file = open(path, "w") #creates grade report file
		file.write("Grade: ")
		file.write(str(grade))
		file.write('%\nFeedback: ')
		for line in feedback:
			file.write(line)
			file.write(". ")
		file.close()

		print('gradeReport.txt created at ' + path)
		#need to write it to a file - grade and feedback in one file