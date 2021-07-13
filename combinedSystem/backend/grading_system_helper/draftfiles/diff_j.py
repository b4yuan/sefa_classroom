import os
#input:
    #mkf_path: This is the path of Makefile file
    #num_of_case: This is the number of test case to be compared by Makefile
#output:    
    #return: return a list containing three element
    #  First element: the list of passed test case
    #  Second element: the list of failed test case
    #  Third element: passed precent
def diff(mkf_path,num_of_case):
    failed = []
    passed = []
    for k in range (num_of_case):
        i = k+1
        result = os.system("make -C " + mkf_path + " testcase" + str(i))
        if (result != 0):
            failed.append(i)
        else:
            passed.append(i)
    
    precent = len(passed) / num_of_case
    return [passed,failed,precent]

#just for test
if __name__ == "__main__":
# "/home/cai282/pas_backend/Grading\ system/ttt/" 
# Path above is just the path of temporary test folder
    result = diff("/home/cai282/pas_backend/Grading\ system/ttt/",2)
    print(result)
