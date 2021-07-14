#!/usr/bin/env python3

from TestCases.GradingInterface.interface import *
import sys
import os
import argparse

GRADE_FILE = 'grade.txt'
FEEDBACK_FILE = 'feedback.txt'

def parse_args(args):

    def force_absolute(path):
        return path if path[0] == '/' else os.path.join(os.getcwd(), path)

    # Checks if the argument is a path to a directory
    def dir_path(path):
        path = force_absolute(path)
        if not os.path.isdir(path):
            raise ValueError
        return path

    # Checks if the argument is a path to a zip file
    def zipfile_path(path):
        path = force_absolute(path)
        if not path.endswith('.zip') or not os.path.isfile(path):
            raise ValueError
        return path

    # define the arguments to be used with argparse
    parser = argparse.ArgumentParser(description='CMD line interface for grading a homework submission')
    parser.add_argument('submission_zip', help='HW submission ZIP file', type=zipfile_path)
    parser.add_argument('test_cases_dir', help='Folder with test cases to grade against', type=dir_path)
    parser.add_argument('hw_tag', help='Homework tag')
    parser.add_argument('user_id', help='Student\'s user id')
    parser.add_argument('out_dir', help=f'Directory to place {GRADE_FILE} and {FEEDBACK_FILE}', type=dir_path,
        default=os.getcwd())

    args = parser.parse_args(args)
    return args

def grade_hw(zip_file_path, test_cases_dir_path):
    graded_obj = grade_submission(zip_file_path, test_cases_dir_path)
    grade = graded_obj.get_grade()
    feedback = graded_obj.get_error_list()

    return grade, feedback

def write_grade(grade: float, hw_tag: str, user_id: str, out_dir: str) -> None:
     with open(os.path.join(out_dir, GRADE_FILE), 'w') as f:
        f.write(f'{hw_tag}\n')
        f.write(f'{user_id}\n')
        f.write(f'{grade:.2f}%\n')

def write_feedback(feedback: list, hw_tag: str, user_id: str, out_dir: str) -> None:
    feedback = '\n'.join(feedback)
    with open(os.path.join(out_dir, FEEDBACK_FILE), 'w') as f:
        f.write(f'{hw_tag}\n')
        f.write(f'{user_id}\n')
        f.write(f'{feedback}\n')

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    grade, feedback = grade_hw(args.submission_zip, args.test_cases_dir)

    write_grade(grade, args.hw_tag, args.user_id, args.out_dir)
    write_feedback(feedback, args.hw_tag, args.user_id, args.out_dir)

 # ./grade_submission.py TestCases/2020homeworks/grade_testing/hw9-16/hw15/hw15.zip TestCases/2020homeworks/HW15BinaryTree1 fake_tag fake_id .

