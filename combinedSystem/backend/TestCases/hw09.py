import unittest
from GradingInterface import interface
import os

path = os.getcwd()

#print(path)

# test_weights = {'test1': 1, 'test2': 1, 'test3': 1, 'test4': 1, 'test5': 1000, 'mem_coef': 1}

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw9/hw09.zip'),
                                            os.path.join(path, '2020homeworks/hw09MergeSort'))
        print('Correct code')
        print(graded.get_error_list())
        print(graded.get_grade())
    
    def test_grade_submission2(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw9/hw09_memory_leak.zip'),
                                            os.path.join(path, '2020homeworks/hw09MergeSort'))
        print('Memory leak')
        print(graded.get_error_list())
        print(graded.get_grade())
    
    def test_grade_submission3(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw9/hw09_not_compile.zip'),
                                            os.path.join(path, '2020homeworks/hw09MergeSort'))
        print('Not compile')
        print(graded.get_error_list())
        print(graded.get_grade())

    def test_grade_submission4(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw9/hw09_simple_wrong_code.zip'),
                                            os.path.join(path, '2020homeworks/hw09MergeSort'))
        print('Simple wrong code')
        print(graded.get_error_list())
        print(graded.get_grade())
    
if __name__ == '__main__':
    unittest.main() # run the unit test again ...
