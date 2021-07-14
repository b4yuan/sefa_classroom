from functions.rmtree import rmtree
from functions.fetchLists import fetchLists
from functions.fetchRepos import fetchRepos
from functions.fetchTags import fetchTags
import os
import subprocess

testFile = "testJSON.json"
hwName = "hw02sort"
graderFile = "run_grader.py" #file name of grading function
gradeName = "grade.txt"
gradeRoot = "/grades"
organization = "cam2testclass"
tagName = "final_ver"
authName = "myers395"
authKey = "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"

[students, hws, repos] = fetchLists(fetchRepos(organization, authName, authKey)) 

for student in students:
    #removes graded tag if it exists on remote repository 
    srcPath = "clones/" + hwName + "-" + student
    originalDir = os.getcwd()
    if os.path.exists(originalDir + "/" + srcPath):
        print('in directory: ', originalDir + "/" + srcPath)
        os.chdir(str(originalDir + "/" + srcPath))
        repoName = hwName + '-' + student
        tagList = fetchTags(organization, repoName, authName, authKey)
        print("user: ", student, "taglist:", tagList)
        repoName = 'git@github.com:' + organization + '/' + repoName + '.git'
        if 'graded_ver' in tagList:
            subprocess.run(["git", "push", "-d", repoName, "graded_ver"], check=True, stdout=subprocess.PIPE).stdout
        #removes grade.txt if it exists on remote repository
        deletePath = originalDir + '/' + srcPath + '/grade.txt'
        if os.path.exists(deletePath):
            os.remove(deletePath)
            subprocess.run(["git", "add", "gradeReport.txt"], check=True, stdout=subprocess.PIPE).stdout
            subprocess.run(["git", "commit", "-m", "deleted gradeReport.txt"], stdout=subprocess.PIPE).stdout
            subprocess.run(["git", "push", "origin", "HEAD:refs/heads/master", "--force"], check=True, stdout=subprocess.PIPE).stdout
        os.chdir(originalDir)
        
if os.path.exists('clones'):
    rmtree('clones') 
        #removes all cloned folders
if os.path.exists('grades'):
    rmtree('grades')
        #removes folder of grades