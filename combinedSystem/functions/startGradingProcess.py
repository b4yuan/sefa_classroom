import os
import sys
from datetime import datetime
import functions.GradingInterface.interface as interface

def startGradingProcess(repos, hoursLateArr, hwName, f):
	index = 0
	for repo in repos:
		owd = os.getcwd()
		path = owd + "/grades/" + repo

		clonePath = owd + '/clones/' + repo #path to student directory
		profPath = owd + '/profFiles/' + hwName #path to professor directory

		os.makedirs(path) #creates repository folder in grades folder
		path = path + '/gradeReport.txt'
		f.write('\n\nFor repo: ' + repo)
		f.write("\n--Calling grade_submission.py")
		obj = interface.grade_submission(clonePath, profPath, int(hoursLateArr[index][1]))
		#obj = graded.GradedSubmission()
		grade = obj.get_grade() #returns a float that is rounded to two decimals
		f.write("\n--Grade is " + str(grade))
		feedback = obj.get_error_list() #returns a list

		os.chdir(owd)
		gradefile = open(path, "w") #creates grade report file

		gradefile.write("Graded on " + datetime.now().strftime("%m-%d %H:%M:%S"))

		gradefile.write("\nSubmission was " + str(hoursLateArr[index][1]) + ' hours late.')

		gradefile.write("\nGrade: " + str(grade))

		gradefile.write('%\nFeedback: ')
		for line in feedback:
			gradefile.write(line)
			gradefile.write(". ")
		gradefile.close()

		f.write('\n--gradeReport.txt created')
		index = index + 1
		#need to write it to a file - grade and feedback in one file