import filecmp
import os


def diff(hw, sub_path):  # input variables: number of test cases(int), submission file path(str), #hw(int)

    listR = []  # Correct file
    listS = []  # Submission file
    # hw = 1
    filepath = 'hw' + str(hw)
    directory = r'/Users/liang/PycharmProjects/pythonProject/research/' + filepath  # our test case results
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # suppose txt file
            #  print(os.path.join(directory, filename))
            listR.append(os.path.join(directory, filename))  # file path add to list
        else:
            continue

    directory = r'/Users/liang/PycharmProjects/pythonProject/research/diffs/'  # should be student test case path
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            #  print(os.path.join(directory, filename))
            listS.append(os.path.join(directory, filename))  # file path add to list
        else:
            continue

    score = 0
    n = len(listR)
    # Path of first file
    a = 'abc'
    for x in range(len(listS)):
        file1 = listR[x]
        # Path of second file
        file2 = listS[x]

        # Compare the contents of both files
        comp = filecmp.cmp(file1, file2, shallow=False)
        if comp == True:
            print("Test case " + str(x + 1) + " is right!")
            score = score + 100 / n
        else:
            print("Test case " + str(x + 1) + " is wrong...")
    print('Your score is: ' + str(score))  # Print the score
