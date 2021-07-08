import requests

#inputs: organization name (ex: cam2testclass), authName (?), authKey (?)
#outputs: json file of repos

def fetchRepos(orgName, authName, authKey):

    #returns json file of repos for specified organization

    url = "https://api.github.com/orgs/" + orgName + "/repos"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    return response.json()