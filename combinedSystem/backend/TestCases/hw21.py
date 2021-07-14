import unittest
from GradingInterface import interface
import os

path = os.getcwd()

print(path)

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw17-21/hw21/hw21.zip'), 
                                            os.path.join(path, '2020homeworks/HW21Sudoku'))
        print(graded.get_error_list())
        print(graded.get_grade())

    def test_grade_submission1(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw17-21/hw21/hw21_compile_error.zip'), 
                                            os.path.join(path, '2020homeworks/HW21Sudoku'))
        print(graded.get_error_list())
        print(graded.get_grade())
    '''        
    def test_grade_submission2(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw17-21/hw21/hw21_memory_leak.zip'), 
                                            os.path.join(path, '2020homeworks/HW21Sudoku'))
        print(graded.get_error_list())
        print(graded.get_grade())
    '''        
    def test_grade_submission3(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw17-21/hw21/hw21_wrong_output.zip'), 
                                            os.path.join(path, '2020homeworks/HW21Sudoku'))
        print(graded.get_error_list())
        print(graded.get_grade())

if __name__ == '__main__':
    unittest.main() # run the unit test again ...
