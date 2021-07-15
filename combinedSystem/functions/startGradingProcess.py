import subprocess
import os
from datetime import datetime
import functions.GradingInterface.interface as interface

def startGradingProcess(repos, hoursLateArr, hwName):
	index = 0
	for repo in repos:
		owd = os.getcwd()
		print("owd: ", owd)
		path = owd + "/grades/" + repo

		clonePath = owd + '/clones/' + repo #path to student directory
		profPath = owd + '/profFiles' + hwName #path to professor directory

		os.makedirs(path) #creates repository folder in grades folder
		path = path + '/gradeReport.txt'
		print("calling grade_submission")
		obj = interface.grade_submission(clonePath, profPath, int(hoursLateArr[index][1]))
		#obj = graded.GradedSubmission()
		grade = obj.get_grade() #returns a float that is rounded to two decimals
		print("grade for ", repo, 'is ', str(grade))
		feedback = obj.get_error_list() #returns a list

		os.chdir(owd)
		print("in directory: ", owd)
		file = open(path, "w") #creates grade report file

		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		file.write("Current Time is ")
		file.write(current_time)

		file.write("\nSubmission was ")
		file.write(str(hoursLateArr[index][1]))
		file.write(' hours late.')

		file.write("\nGrade: ")
		file.write(str(grade))

		file.write('%\nFeedback: ')
		for line in feedback:
			file.write(line)
			file.write(". ")
		file.close()

		print('gradeReport.txt created at ' + path)
		index = index + 1
		#need to write it to a file - grade and feedback in one file