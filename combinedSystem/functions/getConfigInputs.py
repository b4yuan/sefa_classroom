import subprocess
import json
import os
import re
import shutil

def getConfigInputs(JSONFile):
	dictJSON = {} 
	with open(JSONFile, "r") as JFile:
		dictJSON = json.load(JFile)
	return dictJSON

