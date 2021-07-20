import os, json, re, requests
from datetime import datetime, timedelta

#THIS FILE CONTAINS:
#fetchLists, fetchRepos, fetchTags, fetchDueDate, fetchHoursLate, fetchHWInfo

def fetchLists(jsonFile):
    """Description: Obtains list of students and homeworks when given a JSON file of repositories
    
    Parameters: 
    jsonFile (file): JSON file of repository names
    
    Returns:
    students (list of str): list of students in organization
    hws (list of str): list of homeworks in organization
    repos (list of str): list of repository names in organization
    """

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
    """Description: Provides list of tags that exist for specified repository
    
    Parameters: 
    orgName (str): name of classroom
    repoName (str): name of repository
    authName (str): name of authorized user
    authKey(str): GPG key
    
    Returns:
    tagList (list of str): list of tag names for that repository
    """
    
    url = "https://api.github.com/repos/" + orgName + "/" + repoName + "/tags"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    tagList = []
    for entry in response.json():
        tagList.append(entry["name"])
    return tagList

def fetchDueDate(profDir, hwNum):
    """Description: Obtains JSON file of repository names for specified organization using GitHub
    
    Parameters: 
    profDir (str): path of root folder of professor files
    hwNum (int): number of homework that is being graded

    Returns:
    (str) or None: due date of homework
    """

    if os.path.exists(profDir):
        files = os.listdir(profDir)
        hws = [file for file in files if (os.path.isdir(profDir + "/" + file) and fetchHWInfo(None, file)[1] == hwNum)]
        if (len(hws) == 1):
            jsonFile = json.load(open(profDir + "/" + hws[0] + "/weights.json")) #open Json
            return(jsonFile["due"])
        else:
            return None
    else:
        print("HW not present or profFiles doesn't exist: " + str(profDir))
    return None

def fetchHoursLate(subDate, dueDate):
    """Description: Calculates the number of hours between the submission date and due date
    
    Parameters: 
    subDate (str): date associated with the final_ver tag
    dueDate (str): due date of homework from JSON file

    Returns:
    timeDiff: difference in hours between dates
    """

    #date format: year, month, day, hour, minute, second
    #24 hour clock, must be padded with zeroes. example: "2021-07-02 23:59:59"
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
    """Description: Confirms whether or not the submitted number matches the string provided, and returns number associated with provided string
    
    Parameters: 
    num (int): number of homework that is being graded
    hwName (str): string to check number against

    Returns:
    (boolean): whether or not the number and string provided match numbers
    (int): homework number found in string 
    """

    template = re.compile('^([a-zA-Z]*)([0-9]+)(.*)')
    match = re.fullmatch(template, hwName)
    if match != None:
        if (num == None):
            return True, int(match[2])
        elif (num == int(match[2])):
            return True, None
        else:
            return False, None
    else:
        print("Invalid hw name format")
        return False, None