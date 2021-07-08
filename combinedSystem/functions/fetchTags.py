import requests

#inputs: organization name (ex: cam2testclass), repository name (ex: lvy15-hw02sort), authName (?), authKey (?)
#outputs: list of tags that exist in repo

def fetchTags(orgName, repoName, authName, authKey):

    #returns list of tags for specified organization and repo
    
    url = "https://api.github.com/repos/" + orgName + "/" + repoName + "/tags"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    tagList = []
    for entry in response.json():
        tagList.append(entry["name"])
    return tagList