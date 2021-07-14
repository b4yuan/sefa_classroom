import unittest
from GradingInterface import interface
import os

path = os.getcwd()

#print(path)

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw9-16/hw11/hw11.zip'),
                                            os.path.join(path, '2020homeworks/HW11Shuffle1'))
        print('Correct code')
        print(graded.get_error_list())
        print(graded.get_grade())

if __name__ == '__main__':
    unittest.main() # run the unit test again ...
