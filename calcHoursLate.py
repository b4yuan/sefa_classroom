from datetime import datetime
from datetime import timedelta

def calcHoursLate(subDate, dueDate):
    #date format: year, month, day, hour, minute, second
    #24 hour clock, must be padded with zeroes
    #example: "2021-07-02 23:59:59"
    FMT = '%Y-%m-%d %H:%M:%S'
    timeDiff = datetime.strptime(dueDate, FMT) - datetime.strptime(subDate, FMT) #calculate time difference
    timeDiff = timedelta.total_seconds(timeDiff) #convert difference to seconds
    timeDiff = timeDiff / 3600 #convert difference to hours
    
    #timeDiff is positive if submitted before deadline and negative if after deadline
    if (timeDiff >= 0):
        #not late
        return 0
    else:
        return timeDiff * -1
