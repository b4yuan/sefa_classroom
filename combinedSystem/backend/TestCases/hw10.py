import unittest
from GradingInterface import interface
import os

path = os.getcwd()

#print(path)

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw10/hw10.zip'),
                                            os.path.join(path, '2020homeworks/hw10Cake2'))
        print('Correct code')
        print(graded.get_error_list())
        print(graded.get_grade())

    def test_grade_submission2(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw10/hw10_simple_wrong_code.zip'),
                                            os.path.join(path, '2020homeworks/hw10Cake2'))
        print('Simple wrong code')
        print(graded.get_error_list())
        print(graded.get_grade())

if __name__ == '__main__':
    unittest.main() # run the unit test again ...
