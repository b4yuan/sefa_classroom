import subprocess
import json
import os
import re
import shutil
import calcHoursLate


def getTimesLateFromFile(JSONFile, dueDate):
	tags = getFlagFromJSON(JSONFile, "tag")
	timesLate = []
	for tag in tags:
		timesLate.append(calcHoursLate(tag, dueDate))
	return timesLate

