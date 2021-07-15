from functions.createJSONFiles import getHomeworkList
from functions.createJSONFiles import isAValidHomework
import os

def argParse(args, profFiles):
    homeworkMasterList = getHomeworkList(os.path.join(os.getcwd() + profFiles))

    if args.grade_all == True:
        startIndex = 0
        endIndex = len(homeworkMasterList) - 1

    elif args.hw_range is not None:
        if isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[0]: 
            startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[1]
        else:
            print('Your start range homework name was not valid')
            raise Exception('Invalid Homework Name')
        if isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[0]: 
            startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[1]
        else:
            print('Your end range homework name was not valid')
            raise Exception('Invalid Homework Name')
    
    else:
        if isAValidHomework(os.getcwd() + profFiles, args.hw_name)[0]:
            startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_name)[1]
        else:
            print('Your homework name was not valid')
            raise Exception('Invalid Homework Name')
        endIndex = startIndex
    
    return startIndex, endIndex, homeworkMasterList