import subprocess
import json
import os
import re
import shutil
import calcHoursLate
import gitCurl

def cloneFromRepos(org, repositories, tagName, authName, authKey):
    hoursLateArr = []
    for repo in repositories:
        tagList = gitCurl.fetchTags(org, repo, authName, authKey)
        if (tagName in tagList) and ('graded_ver' not in tagList):
            reposURL = "https://" + authKey + "@github.com/" + org + "/" + repo + ".git"
            if os.path.isdir(os.getcwd() + "/clones") == False:
                os.mkdir(os.getcwd() + "/clones")
            os.chdir(os.getcwd() + "/clones")
            subprocess.run(["git", "clone", "-b", tagName, str(reposURL)], check=True, stdout=subprocess.PIPE).stdout
            os.chdir(os.getcwd() + "/" + repo) #navigate to cloned repo
            tagStr = 'git log -1 --format=%ai ' + tagName
            info = subprocess.check_output(tagStr.split()).decode()
            subDate =info.split(' ')[0] + ' ' + info.split(' ')[1]
            print(subDate)
            hoursLate = calcHoursLate.calcHoursLate(subDate, "2021-06-30 15:59:59") #still need to get the due date from somewhere
            hoursLateArr.append([repo, hoursLate]) #2d array with repository URL and number of hours late
    print(hoursLateArr)

if __name__ == "__main__":
    [repos, students, hws] = gitCurl.fetchLists(gitCurl.fetchRepos("cam2testclass", "myers395", "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"))
    cloneFromRepos("cam2testclass", repos, "final_ver", "myers395", "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")
