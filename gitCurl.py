import json
import os
import requests
import re
#import pandas as pd

def fetchRepos(orgName, authName, authKey):

    #returns json file of repos for specified organization

    url = "https://api.github.com/orgs/" + orgName + "/repos"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    return response.json()

def fetchTags(orgName, repoName, authName, authKey):

    #returns list of tags for specified organization and repo
    
    url = "https://api.github.com/repos/" + orgName + "/" + repoName + "/tags"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    tagList = []
    for entry in response.json():
        tagList.append(entry["name"])
    print(tagList)

def fetchLists(jsonFile):

    #returns [list of students, list of homeworks] when given a json file of repo names

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
    [students, hws] = fetchLists(fetchRepos("cam2testclass", "myers395", "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"))
    fetchTags("cam2testclass", "hw02sort-lvy15", "myers395", "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")