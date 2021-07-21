import subprocess, os

org = "cam2testclass"
authName = "myers395"
authKey = "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"

repo = "hw02-saulevans12"
repoURL = "https://" + authKey + "@github.com/" + org + "/" + repo + ".git"
#print(repoURL)

#cloneDir = os.getcwd() + "/clones/hw02sort-lvy15"
#subprocess.run(["git", "clone", str(repoURL), cloneDir])
#os.chdir(cloneDir)
command = "git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' " + repoURL
tags = os.popen("git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' https://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@github.com/cam3testclass/hw02-saulevans12.git").read()
#subprocess.run("git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' https://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@github.com/cam3testclass/hw02-saulevans12.git".split(" "))
print('Tags:', tags)