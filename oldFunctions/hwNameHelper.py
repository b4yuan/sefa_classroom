import re

def fetchHWInfo(num, hwName):

    # INPUTS:
    #   num: number of homework
    #   hwName: string of homework to match
    # RETURNS:
    #   Boolean: whether or not the number matches the homework

    template = re.compile('^([a-zA-Z]*)([0-9]+)(.*)')
    match = re.fullmatch(template, hwName)
    if match != None:
        if (num == None):
            return True, int(match[2])
        elif (num == int(match[2])):
            return True, None
        else:
            return False, None
    else:
        print("Invalid hw name format")
        return False, None