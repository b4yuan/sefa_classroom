import os
import json

def fetchDueDate(profFiles, hwName):
    if os.path.exists(profFiles + "/assignmentData.json"):
        jsonFile = json.load(open(profFiles + "/assignmentData.json")) #open Json
        for entry in jsonFile: #look through each homework
            if(entry["name"] == hwName): #check name
                date = entry["due"] #assign the due date
                break
    else:
        print("Professor files path does not exist:" + str(profFiles))
    return date