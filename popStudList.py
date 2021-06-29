import json
import os
import requests
import re
#import pandas as pd

def fetchJson():
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get('https://api.github.com/orgs/cam2testclass/repos', auth=('myers395', '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'))
    return response.json()

def fetchLists(jsonFile):
    repoList = []
    for entry in jsonFile:
        repoList.append(entry["name"])
    template = re.compile('^([a-zA-Z0-9]+)[-]([a-zA-Z0-9]+)$')
    studentSet = set()
    hwSet = set()
    for repo in repoList:
        match = re.fullmatch(template, repo)
        if match != None:
            hwSet.add(match[1])
            studentSet.add(match[2])
    students = list(studentSet)
    hws = list(hwSet)
    return students.sort(), hws.sort()

#def updateDF(hws, students, df):
    #if (df == None):
    #    df = pd.DataFrame(columns = students, index = hws)
    #print(df)


if __name__ == "__main__":
    [students, hws] = fetchLists(fetchJson())