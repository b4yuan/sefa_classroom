import requests

def fetchRepos(orgName, authName, authKey):
    """Description: Obtains JSON file of repository names for specified organization using GitHub
    
    Parameters: 
    orgName (str): name of classroom
    authName (str): name of authorized user
    authKey(str): GPG key
    
    Returns:
    JSONfile: JSON file of repository names"""


    url = "https://api.github.com/orgs/" + orgName + "/repos"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, auth=(authName, authKey))
    return response.json()