from functions.createJSONFiles import getHomeworkList
from functions.createJSONFiles import isAValidHomework
import os

def argParse(args, profFiles, f):
    homeworkMasterList = getHomeworkList(os.path.join(os.getcwd() + profFiles))

    if args.grade_all == True:
        startIndex = 0
        endIndex = len(homeworkMasterList) - 1
        f.write('\nGrading all homeworks!')

    elif args.hw_range is not None:
        f.write('\nGrading a range of homeworks: ')

        if isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[0]: 
            startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[0])[1]
            f.write(homeworkMasterList[startIndex] + ' to ')
        else:
            print('Your start range homework name was not valid')
            raise Exception('Invalid Homework Name')

        if isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[0]: 
            endIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_range[1])[1]
            f.write(homeworkMasterList[endIndex])
        else:
            print('Your end range homework name was not valid')
            raise Exception('Invalid Homework Name')
    
    else:
        if isAValidHomework(os.getcwd() + profFiles, args.hw_name)[0]:
            startIndex = isAValidHomework(os.getcwd() + profFiles, args.hw_name)[1]
            f.write('Grading ' + homeworkMasterList[startIndex])
        else:
            print('Your homework name was not valid')
            raise Exception('Invalid Homework Name')
        endIndex = startIndex
    
    return startIndex, endIndex, homeworkMasterList