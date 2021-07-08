import os
import subprocess
from functions.calcHoursLate import calcHoursLate
from functions.fetchTags import fetchTags
#inputs: 

def cloneFromRepos(org, repos, hwName, tagName, authName, authKey): #changed repository to students and added hwName
    hoursLateArr = []
    for repo in repos:
        if repo.startswith(hwName):
            tagList = fetchTags(org, repo, authName, authKey)
            print(tagList)
            if (tagName in tagList) and ('graded_ver' not in tagList):
                reposURL = "https://" + authKey + "@github.com/" + org + "/" + repo + ".git"
                owd = os.getcwd()
                if os.path.isdir(os.getcwd() + "/clones") == False:
                    os.mkdir(os.getcwd() + "/clones")
                os.chdir(os.getcwd() + "/clones")
                subprocess.run(["git", "clone", "-b", tagName, str(reposURL)], check=True, stdout=subprocess.PIPE).stdout
                os.chdir(os.getcwd() + "/" + repo) #navigate to cloned repo
                tagStr = 'git log -1 --format=%ai ' + tagName
                info = subprocess.check_output(tagStr.split()).decode()
                subDate = info.split(' ')[0] + ' ' + info.split(' ')[1]
                #print(subDate)
                hoursLate = calcHoursLate(subDate, "2021-06-30 15:59:59") #still need to get the due date from somewhere
                hoursLateArr.append([repo, hoursLate]) #2d array with repository URL and number of hours late
                os.chdir(owd)
    return hoursLateArr