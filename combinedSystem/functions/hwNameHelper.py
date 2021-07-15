import re

def stripHW(hwName):

    # INPUTS:
    #   hwName: string of homework to match
    # RETURNS:
    #   int: number associated with homework

    template = re.compile('^([a-zA-Z]*)([0-9]+)(.*)')
    match = re.fullmatch(template, hwName)
    if match != None:
        return int(match[2])
    else:
        print("Invalid hw name format")

def matchHW(num, hwName):

    # INPUTS:
    #   num: number of homework
    #   hwName: string of homework to match
    # RETURNS:
    #   Boolean: whether or not the number matches the homework

    template = re.compile('^([a-zA-Z]*)([0-9]+)(.*)')
    match = re.fullmatch(template, hwName)
    if match != None:
        if (num == int(match[2])):
            return True
        else:
            return False
    else:
        print("Invalid hw name format")
        return False


if __name__ == "__main__":
    #stripHW("HW15BinaryTree1")
    #stripHW("15")
    #stripHW("hw15binarytree1")
    #stripHW("HW05Sum")
    #stripHW("5")
    print(matchHW(5, "HW05Sum"))