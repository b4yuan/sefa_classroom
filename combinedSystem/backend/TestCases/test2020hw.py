import unittest
from GradingInterface import interface
import os

path = os.path.join(os.getcwd(), 'TestCases')

def testhw02():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/sort.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()

def testhw03():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/eliminate.zip'),
                                        os.path.join(path, '2020homeworks/HW03Cake'))
    print(f'grade for hw03 is {graded.get_grade()}')

    return graded.get_error_list()
    
def testhw04():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/filechar.zip'),
                                        os.path.join(path, '2020homeworks/HW04File'))
    print(f'grade for hw04 is {graded.get_grade()}')

    return graded.get_error_list()
    
def testhw05():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/fileint.zip'),
                                        os.path.join(path, '2020homeworks/HW05Sum'))
    print(f'grade for hw05 is {graded.get_grade()}')

    return graded.get_error_list()
    
def testhw06():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/filestr.zip'),
                                        os.path.join(path, '2020homeworks/HW06Word'))
    print(f'grade for hw06 is {graded.get_grade()}')

    return graded.get_error_list()
    
def testhw07():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/hw07.zip'),
                                        os.path.join(path, '2020homeworks/HW07QSort'))
    print(f'grade for hw07 is {graded.get_grade()}')

    return graded.get_error_list()
    
def testhw08():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/hw08.zip'),
                                        os.path.join(path, '2020homeworks/HW08Struct'))
    print(f'grade for hw08 is {graded.get_grade()}')

    return graded.get_error_list()
    
    # ...

if __name__ == '__main__':
    print('Start Testing...')
    print(testhw02())
    print(testhw03())
    print(testhw04())
    print(testhw05())
    print(testhw06())
    print(testhw07())
    print(testhw08())

    # ......
