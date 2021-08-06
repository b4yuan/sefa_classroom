import os
import json
import re
from crontab import CronTab
from datetime import datetime

#getDueDateDict - Gets the JSON File, inserts the due dates for each homework into a dictionary, returns that dictionary
def getDueDateDict(jsonFile):
	dueDict = {}
	with open(jsonFile, 'r') as jF:
		jsonF = jF.read()
		dueDict = json.loads(jsonF)
	return dueDict
	
#updateCronFile - Updates the cronfile with the necessary due dates
def updateCronFile(cronDict, userName):
	for key, value in cronDict.items():
		cronSess = CronTab(user=userName)
		cronJob = cronSess.new(command=str('python3 ../combinedSystem/runSystem.py --hw_name ' + key),comment=key )
		cronJob.minute.on(value[4])
		print(value)
		cronJob.hour.on(value[3])
		cronJob.day.on(value[1])
		cronJob.month.on(value[0])
		cronSess.write()

#processDueDate - Updates the dictionary with a processed version and returns that processed version
def processDueDate(cronDict):
	formattedDates = re.compile(r'([0-9])-([0-9])-([0-9]*),([0-9]*]):([0-9]*)')
	for key, value in cronDict.items():
		valBuffer = value
		value = []
		value.append(int(valBuffer.split("-")[0]))  
		value.append(int(valBuffer.split("-")[1]))   
		value.append(int(valBuffer.split(",")[0].split("-")[2]))   
		value.append(int(valBuffer.split(",")[1].split(":")[0]))   
		value.append(int(valBuffer.split(":")[1]))
		cronDict[key] = value
	return cronDict
	 
#deleteDatesPassed - Deletes old due dates, so that they do not reoccur again
def deleteDatesPassed(cronDict, userName):
	for key, value in cronDict.items():
		print(value)
		print(datetime.now().month)
		print(key)
		
		cronSess = CronTab(user=userName)
		if(int(datetime.now().year) > value[2]):
			cronSess.remove_all(comment=key)
		if(int(datetime.now().year) == value[2] and int(datetime.now().month) > value[0]):
			cronSess.remove_all(comment=key)
		if(int(datetime.now().year) == value[2] and int(datetime.now().month) == value[0]):
			if(int(datetime.now().month) > value[0]):
				cronSess.remove_all(comment=key)
			if(int(datetime.now().month) == value[0] and int(datetime.now().day) > value[1]):
				cronSess.remove_all(comment=key)
			if(int(datetime.now().month) == value[0] and int(datetime.now().day) == value[1]):
				if((int(datetime.now().hour) > value[3])):
					cronSess.remove_all(comment=key)
				if((int(datetime.now().hour) == value[3]) and int(datetime.now().minute) > value[4]):
					cronSess.remove_all(comment=key)
			

		cronSess.write()
	
if __name__ == "__main__":
	updateCronFile(processDueDate(getDueDateDict('duedates.json')), 'merrill8')
	deleteDatesPassed(processDueDate(getDueDateDict('duedates.json')), 'merrill8')
