import os
from functions.fetchDueDate import fetchDueDate
import subprocess
from functions.calcHoursLate import calcHoursLate
from functions.fetchTags import fetchTags
#inputs: 

def cloneFromRepos(org, repos, hwName, tagName, authName, authKey, profPath): #changed repository to students and added hwName
    hoursLateArr = [] #Cloned repos and their time late
    clonedRepos = [] #Array of repositories that will be cloned after function
    newProfPath = os.getcwd() + profPath #must set before looping through repos
    owd = os.getcwd()
    for repo in repos:
        if repo.startswith(hwName):
            clonedRepos.append(repo)
            tagList = fetchTags(org, repo, authName, authKey)
            print(tagList)
            if (tagName in tagList) and ('graded_ver' not in tagList):
                reposURL = "https://" + authKey + "@github.com/" + org + "/" + repo + ".git"
                if os.path.isdir(os.getcwd() + "/clones") == False:
                    os.mkdir(os.getcwd() + "/clones")
                os.chdir(os.getcwd() + "/clones")
                subprocess.run(["git", "clone", "-b", tagName, str(reposURL)], check=True, stdout=subprocess.PIPE).stdout
                os.chdir(os.getcwd() + "/" + repo) #navigate to cloned repo
                tagStr = 'git log -1 --format=%ai ' + tagName
                info = subprocess.check_output(tagStr.split()).decode()
                subDate = info.split(' ')[0] + ' ' + info.split(' ')[1]
                #print(subDate)
                hoursLate = calcHoursLate(subDate, fetchDueDate(newProfPath, hwName))
                hoursLateArr.append([repo, hoursLate]) #2d array with repository name and number of hours late
                os.chdir(owd)
    return clonedRepos, hoursLateArr