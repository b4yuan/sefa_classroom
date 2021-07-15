import os

def splitRepo(repoURL=""):
    if (repoURL == ""):
        print("No Master Repo HTTPS provided.")
    owd = os.getcwd() #save working directory
    if os.path.isdir(os.getcwd() + "/clones") == False: #check for clones directory and make if doesn't exist
        os.mkdir(os.getcwd() + "/clones") 
    os.chdir(os.getcwd() + "/clones")

    os.chdir(owd)
    print(os.getcwd())


if __name__ == "__main__":
    splitRepo("https://github.com/PurdueECE264/2020FallProblems-Lu.git")