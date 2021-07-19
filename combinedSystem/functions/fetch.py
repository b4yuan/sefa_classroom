import os, json, re, requests
from datetime import datetime, timedelta

#THIS FILE CONTAINS:
#fetchLists, fetchRepos, fetchTags, fetchDueDate, fetchHoursLate, fetchHWInfo

def fetchLists(jsonFile):
    #returns [list of students, list of homeworks] when given a json file of repo names

    repoList = []
    for entry in jsonFile:
        repoList.append(entry["name"])

    template = re.compile('^([a-zA-Z0-9]+)[-]([a-zA-Z0-9]+)$')
    studentSet = set()
    hwSet = set()
    repos = []

    for repo in repoList:
        match = re.fullmatch(template, repo)
        if match != None:
            repos.append(match[0])
            hwSet.add(match[1])
            studentSet.add(match[2])

    students = list(studentSet)
    hws = list(hwSet)
    students.sort()
    hws.sort()

    return students, hws, repos

def fetchRepos(orgName, authName, authKey):
    """Description: Obtains JSON file of repository names for specified organization using GitHub
    
    Parameters: 
    orgName (str): name of classroom
    authName (str): name of authorized user
    authKey(str): GPG key
    
    Returns:
    JSONfile: JSON file of repository names"""


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
    return tagList

def fetchDueDate(profFiles, hwNum):
    if os.path.exists(profFiles + "/assignmentData.json"):
        jsonFile = json.load(open(profFiles + "/assignmentData.json")) #open Json
        for entry in jsonFile: #look through each homework
            if fetchHWInfo(hwNum, entry["name"]): #check name
                date = entry["due"] #assign the due date
                break
    else:
        print("Professor files path does not exist:" + str(profFiles))
    return date

def fetchHoursLate(subDate, dueDate):
    #date format: year, month, day, hour, minute, second
    #24 hour clock, must be padded with zeroes
    #example: "2021-07-02 23:59:59"
    FMT = '%Y-%m-%d %H:%M:%S'
    timeDiff = datetime.strptime(dueDate, FMT) - datetime.strptime(subDate, FMT) #calculate time difference
    timeDiff = timedelta.total_seconds(timeDiff) #convert difference to seconds
    timeDiff = timeDiff / 3600 #convert difference to hours
    
    #timeDiff is positive if submitted before deadline and negative if after deadline
    if (timeDiff >= 0):
        #not late
        return 0
    else:
        return timeDiff * -1

def fetchHWInfo(num, hwName):
    # INPUTS:
    #   num: number of homework
    #   hwName: string of homework to match
    # RETURNS:
    #   Boolean: whether or not the number matches the homework

    template = re.compile('^([a-zA-Z]*)([0-9]+)(.*)')
    match = re.fullmatch(template, hwName)
    if match != None:
        if (num == None):
            return int(match[2])
        elif (num == int(match[2])):
            return True
        else:
            return False
    else:
        print("Invalid hw name format")
        return False