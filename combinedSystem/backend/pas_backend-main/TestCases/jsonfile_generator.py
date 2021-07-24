import json
import argparse
import os

'''
To use this program, enter command like:
python3 jsonfile_generator.py --HW_name ECE264-HW2 --case_num 5 --mem_coef 1 --late-coef 10
'''


def get_args():
    parser = argparse.ArgumentParser("please add weights here")
    parser.add_argument("--HW_name", type=str, default="weights",
                        help="name of the homework")  # Get name of the homework from terminal
    parser.add_argument("--case_num", type=int, default=10,
                        help="total number of testcases")  # Get total number of testcases from terminal
    parser.add_argument("--mem_coef", type=float, default=1,
                        help="the weight for memory leak")  # Get weight of memory leak per byte from terminal
    parser.add_argument("--late-coef", type=float, default=5,
                        help="the weight for late penalty")  # Get penalty weight of late submission per hour
    parser.add_argument("--grade_late_work", type=bool, default=False,
                        help="grade work and give feedback even if the late penalty is greater than 100 points")  # Get if very late work should be graded for feedback or not, even though they will get a 0 no matter what
    parser.add_argument("--destination", type=str, default=os.getcwd(),
                        help="the FULL path of where the file should be saved")  # Get where the file should be saved. default is the current directory. ideally they go to the directory they want it to be, and then call this file
    
    # add more arguments here with similar format

    args = parser.parse_args()
    return args


def generate_json_file(params):
    name = params.HW_name
    test_params = {}  # Write the inner keys
    json_text = {'weights': []}  # Write the outer key
    case_num = params.case_num

    # if not given specific weight for each testcase, the weights will be equally distributed
    for i in range(case_num):
        test_params['test%d' % (i + 1)] = 1

    '''
    to indicate weight for each testcase, write code like:
        test_params['test1'] = 0.1
        test_params['test2'] = 0.2
        ...
    '''

    test_params["mem_coef"] = params.mem_coef
    test_params["late_coef"] = params.late_coef
    test_params["grade_late_work"] = params.grade_late_work
    for item in test_params:
        value = test_params[item]
        json_text['weights'].append({item: value}, )
    json_data = json.dumps(json_text, indent=4, separators=(',', ': '))  # Make Json file looks better
    filename = name + '.json'
    os.chdir(params.destination)
    f = open(filename, 'w+')
    f.write(json_data)
    f.close()


if __name__ == '__main__':
    params = get_args()
    generate_json_file(params)
