import argparse

homeworkMasterList = ["hw02sort", "hw03cake", "hw04file", "hw05sum"]

parser = argparse.ArgumentParser("specify homework assignments to grade")
group = parser.add_mutually_exclusive_group()
group.add_argument("--hw_name", type = str, help= "specify the name of the homework to grade. example: python3 runSystem.py --hw_name hw02sort")
group.add_argument("--hw_range", type = str, nargs = 2, help = "specify a range of homeworks to grade. example: python3 runSystem.py --hw_range hw02sort hw04file")
group.add_argument("--grade_all", action="store_true", help = "specify this option to grade all homeworks. example: python3 runSystem.py --grade_all")
args = parser.parse_args()

if args.hw_range is not None or args.grade_all == True:
    print('Grading a range of hws')
    if args.grade_all == True:
        startIndex = 0
        endIndex = len(homeworkMasterList) - 1
    else:
        startIndex = homeworkMasterList.index(args.hw_range[0])
        endIndex = homeworkMasterList.index(args.hw_range[1])
    for x in range(startIndex, endIndex+1):
        hwName = homeworkMasterList[x]
        print('Grading :', hwName)
else:
    print('Grading only one hw')
    print('Grading :', args.hw_name)