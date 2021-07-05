import subprocess
import json
import os
import re
import shutil
import calcHoursLate
import gitCurl

def cloneFromRepos(org, students, hwName, tagName, authName, authKey): #changed repository to students and added hwName
    hoursLateArr = []
    for student in students:
        repo = hwName + '-' + student
        tagList = gitCurl.fetchTags(org, repo, authName, authKey)
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
            subDate =info.split(' ')[0] + ' ' + info.split(' ')[1]
            #print(subDate)
            hoursLate = calcHoursLate.calcHoursLate(subDate, "2021-06-30 15:59:59") #still need to get the due date from somewhere
            hoursLateArr.append([repo, hoursLate]) #2d array with repository URL and number of hours late
            os.chdir(owd)
    print(hoursLateArr)

if __name__ == "__main__":
    #shutil.rmtree('clones') #this doesnt work
    [students, hws] = gitCurl.fetchLists(gitCurl.fetchRepos("cam2testclass", "myers395", "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")) #modified output since fetchLists outputs students and hws and not repository list
    cloneFromRepos("cam2testclass", students, 'hw02sort', "final_ver", "myers395", "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")