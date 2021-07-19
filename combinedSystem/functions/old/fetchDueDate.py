import os
import json 
from functions.hwNameHelper import fetchHWInfo

def fetchDueDate(profFiles, hwNum):
    if os.path.exists(profFiles + "/assignmentData.json"):
        jsonFile = json.load(open(profFiles + "/assignmentData.json")) #open Json
        for entry in jsonFile: #look through each homework
            if fetchHWInfo(hwNum, entry["name"]): #check name
                date = entry["due"] #assign the due date
                break
    else:
        print("Professor files path does not exist:" + str(profFiles))
    return date