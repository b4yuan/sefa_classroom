import os
import subprocess

def splitRepo(cloneRoot, repoURL):
    if (repoURL == "") or (repoURL == None): # variable check
        print("No Master Repo HTTPS provided.")
    owd = os.getcwd() # save working directory
    if os.path.isdir(os.getcwd() + cloneRoot) == False: # check for clone directory and make if doesn't exist
        os.mkdir(os.getcwd() + cloneRoot) 
    os.chdir(os.getcwd() + cloneRoot)
    subprocess.run(["git", "clone", str(repoURL)])



    os.chdir(owd)
    print(os.getcwd())

if __name__ == "__main__":
    splitRepo("/home/jack/Documents/pas/pas_githubclassroom/combinedSystem/masterClone","https://github.com/PurdueECE264/2020FallProblems-Lu.git")