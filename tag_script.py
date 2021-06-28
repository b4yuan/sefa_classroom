import subprocess
import os

repo = 'git@github.com:cam2testclass/hw03cake-lvy15.git'
clonedRepo = 'clone'
tagName = 'ver_1'

subprocess.run('git clone -b ' + tagName + ' ' + repo + ' ' + clonedRepo)
os.chdir(clonedRepo) #need to navigate to cloned repo
tagStr = 'git log -1 --format=%ai ' + tagName
info = subprocess.check_output(tagStr.split()).decode() #must be in repo to work

split1 = info.split(' ')
dateSplit = split1[0].split('-')
timeSplit = split1[1].split(':')

dateArr = dateSplit + timeSplit
for x in range(6):
    dateArr[x] = int(dateArr[x])

print(dateArr) #order: year, month, day, hour, minute, second