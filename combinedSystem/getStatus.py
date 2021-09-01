from functions.setup import getConfigInputs, isAValidHomework, getHomeworkList
from functions.fetch import fetchLists, fetchRepos, fetchHWInfo, fetchTags
from functions.rmtree import rmtree

import argparse, os, subprocess, pandas as pd

parentDir = os.getcwd()

#!!--------Set Up Variables From JSON File-----------!! 
#Configname
configJSON = parentDir + "/profFiles/config.json"
#get variables from JSON config file
configInputs = getConfigInputs(configJSON)

#variables
organization =  configInputs["organization"]  #json file
authName = configInputs["authName"] #json file
authKey = configInputs["authKey"] #json file

tagName = "final_ver"
gradeFileName = "gradeReport.txt"
profFiles = "/profFiles"
gradeRoot = "/grades"
clonesRoot = "/clones"

[s, h, repos] = fetchLists(fetchRepos(organization, authName, authKey))

submitted = []
graded = []
hwnames = []
students = []

for repo in repos:
    tagList = fetchTags(organization, repo, authName, authKey)
    if 'final_ver' in tagList:
        submitted.append('Y')
    else:
        submitted.append(' ')

    if 'graded_ver' in tagList:
        graded.append('Y')
    else:
        graded.append(' ')
    list = repo.split("-")
    hwnames.append(list[0])
    students.append(list[1])


df = pd.DataFrame(
    {
    "hw name": hwnames,
    "student": students,
    "submitted?":submitted,
    "graded?":graded
    }
)

df = df.sort_values(by=["hw name"])

print(df)