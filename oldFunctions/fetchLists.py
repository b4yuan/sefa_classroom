import re

#inputs: json file
#outputs: list of students, list of homeworks, list of repos

def fetchLists(jsonFile):

    #returns [list of students, list of homeworks] when given a json file of repo names

    repoList = []
    for entry in jsonFile:
        repoList.append(entry["name"])
    template = re.compile('^([a-zA-Z0-9]+)[-]([a-zA-Z0-9]+)$')
    studentSet = set()
    hwSet = set()
    repos = []
    for repo in repoList:
        match = re.fullmatch(template, repo)
        if match != None:
            repos.append(match[0])
            hwSet.add(match[1])
            studentSet.add(match[2])
    students = list(studentSet)
    hws = list(hwSet)
    students.sort()
    hws.sort()
    return students, hws, repos
