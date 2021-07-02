import numpy as np
import pandas as pd
import os
import gitCurl

def updateDF(hws, students, df):

    #Takes in existing dataframe and returns the same dataframe with empty columns added
    #for each new entry in the student or homework list provided

    if (df.empty):
        df= pd.DataFrame(np.zeros((len(students), len(hws))), columns= hws, dtype= float)
        df.insert(0, "GitHub Username", students)

    else:
        for student1 in students:
            for student2 in list(df["GitHub Username"]):
                if (student1 == student2):
                    students.remove(student1)

        oldHws = list(df.columns)
        oldHws.remove("GitHub Username")
        for hw1 in hws:
            for hw2 in oldHws:
                if (hw1 == hw2):
                    hws.remove(hw1)

        for student in students:
            newStudent= [{"GitHub Username":student}]
            for i in range(1, len(df.columns)):
                newStudent[0][df.columns[i]]= 0
            df= df.append(newStudent, ignore_index= True, sort= True)

        for hw in hws:
            newHw= [0.0] * len(df.index)
            df[hw]= newHw
    return df

def loadCSV(path):

    #Takes in the file location of a csv and returns a the data in a dataframe 

    if (os.path.exists(path)):
        df= pd.read_csv(path, delimiter= ",", engine= "python").drop(labels= "Unnamed: 0", axis= 1)
    else:
        df= pd.DataFrame({"GitHub Username":[]})
    return df

def writeCSV(path, df):

    #Takes in a dataframe and writes data to an csv

    df.to_csv(path)
    return

if __name__ == "__main__":
    [students, hws] = gitCurl.fetchLists(gitCurl.fetchRepos("cam2testclass", "myers395", "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"))

    #Example call:

    writeCSV(os.getcwd() + "/grades.csv", updateDF(hws, students, loadCSV(os.getcwd() + "/grades.csv")))
