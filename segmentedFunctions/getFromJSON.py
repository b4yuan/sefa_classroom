import subprocess
import json
import os
import re
import shutil

def getFlagFromJSON(JSONFile, flag):
	flag = []
	with open(JSONFile, "r") as JFile:
		extractRawJSON = json.load(JFile)
		for dictionaries in extractRawJSON:
			for flags in dictionaries:
				if(flags == flag):
					flag.append(dictionaries[flags])
	return flag

def getRepoNamesFromJSON(JSONFile):
	usernames = getFlagFromJSON(JSONFile, "names")
	return usernames

def getRepoCloneURLSFromJSON(JSONFile):
	repositoryURLS = getFlagFromJSON(JSONFile, "clone_url")
	return repositoryURLS


