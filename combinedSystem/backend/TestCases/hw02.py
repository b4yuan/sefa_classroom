import unittest
from GradingInterface import interface
import os

path = os.getcwd()

def testhw02():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()

def testhw02_nocompile():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort_nocompile.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()

def testhw02_incorrect():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort_wrong.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()

def testhw02_mem():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort_mem.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()


    
    # ...

if __name__ == '__main__':
    print('Start Testing...')

    print('start correct homework ----------------------------------')
    print(testhw02())
    print('end correct homework ----------------------------------\n\n')
'''
    print('start nocompile homework ----------------------------------')
    print(testhw02_nocompile())
    print('end nocompile homework ----------------------------------\n\n')

    print('start incorrect homework ----------------------------------')
    print(testhw02_incorrect())
    print('end incorrect homework ----------------------------------\n\n')

    print('start mem leak homework ----------------------------------')
    print(testhw02_mem())
    print('end mem leak homework ----------------------------------\n\n')

'''
    # ......
