import os
import subprocess
from fetch import fetchHWInfo
import requests
from distutils.dir_util import copy_tree
from rmtree import rmtree
import time
from setup import getConfigInputs

def splitRepo(cloneRoot, repoURL):

    parentDir = os.path.dirname(os.getcwd())
    os.chdir(parentDir)

    #Configname
    configJSON = "/profFiles/config.json"
    #get variables from JSON config file
    configInputs = getConfigInputs(configJSON)

    #variables
    orgName =  configInputs["organization"]  #json file
    authName = configInputs["authName"] #json file
    authKey = configInputs["authKey"] #json file

    # variable check
    if (repoURL == "") or (repoURL == None): 
        print("No Master Repo HTTPS provided.")
        return

    owd = os.getcwd() # save working directory
    if os.path.isdir(os.getcwd() + cloneRoot) == False: # check for clone directory and make if doesn't exist
        os.mkdir(os.getcwd() + cloneRoot) 
    os.chdir(os.getcwd() + cloneRoot)

    # Clone master repo and change into it
    print("\nCloning master repo:\n")
    subprocess.run(["git", "clone", str(repoURL)])
    masterClone = os.getcwd() + "/" + os.listdir()[0]
    os.chdir(masterClone)

    # Find all homework folders in repo
    contents = os.listdir()
    hws = []
    for file in contents:
        if ((fetchHWInfo(None, str(file))[1]) != None):
            hws.append(file)
    hws.sort()
    os.chdir(owd + cloneRoot)

    # Create stageing dir
    if os.path.isdir(os.getcwd() + "/staging") == False: # check for clone directory and make if doesn't exist
        os.mkdir(os.getcwd() + "/staging") 
    os.chdir(os.getcwd() + "/staging")
    stagingDir = os.getcwd()

    # Create template repos and fill with homewor files from master repo
    print("\nCreating template repositories")
    for hw in hws:
        createTemplateRepo(orgName, hw, authKey, authName)
    time.sleep(1) # not sure if this is necessary
    print("Done.")

    for hw in hws:
        reposURL = "https://" + authKey + "@github.com/" + orgName + "/" + hw + ".git"
        print("\nCloning " + hw + " Template Repo:\n")
        subprocess.run(["git", "clone", reposURL])
        print("\nFilling " + hw + " with Files:")
        copy_tree(masterClone + "/" + hw, stagingDir + "/" + hw)
        print("Done.")
        os.chdir(stagingDir + "/" + hw)
        print("\nPushing " + hw + " Files:\n")
        subprocess.run(["git", "add", "."], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "commit", "-m", "Automatic population"], stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "push", "origin", "HEAD:refs/heads/master", "--force"], check=True, stdout=subprocess.PIPE).stdout
        os.chdir(stagingDir)
    os.chdir(owd + cloneRoot)

    os.chdir(owd)
    if os.path.exists(owd + cloneRoot):
        rmtree(owd + cloneRoot)
        print('\nCleaned clone directories')

def createTemplateRepo(orgName, repoName, authKey, authName):

    # Creates empty template repo with name (repoName) in org (orgName) specified

    headers = {
        'Accept': 'application/vnd.github.baptiste-preview+json',
    }

    data = '{"name":\"'+ repoName + '\", "is_template": true, "private": true, "description":"Auto generated template"}'

    response = requests.post('https://api.github.com/orgs/' + orgName + '/repos', headers=headers, data=data, auth=(authName, authKey))

if __name__ == "__main__":
    https = input("Please Enter HTTPS for Master Repo (Press Enter for Default):")
    if (https == ""):
        print("Using https://github.com/PurdueECE264/2020FallProblems-Lu")
        splitRepo("/masterClone", "https://github.com/PurdueECE264/2020FallProblems-Lu.git")
    else:
        splitRepo("/masterClone", https)