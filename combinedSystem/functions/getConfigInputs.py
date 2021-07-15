import subprocess
import json
import os
import re
import shutil

def getConfigInputs(JSONFile):
	dictJSON = {} 
	with open(os.getcwd() + JSONFile, "r") as JFile:
		dictJSON = json.load(JFile)
	return dictJSON

