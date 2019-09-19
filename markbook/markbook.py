#! /usr/bin/env python3

import sys


def args_parser(args: list):
    pass


class Student:

    accepted_types = {
        'first_name': str,
        'last_name': str,
        'gender': str,
        'image': str,
        'student_number': int,
        'grade': int,
        'email': str,
        'marks': tuple,
        'comments': str
    }

    __slots__ = ['first_name', 'last_name', 'gender', 'image', 'student_number', 'grade',
                 'email', 'marks', 'comments']

    def __init__(self, first_name=None, last_name=None, gender=None, image=None, student_number=None,
                 grade=None, email=None, marks=None, comments=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.image = image
        self.student_number = student_number
        self.grade = grade
        self.email = email
        self.marks = marks
        self.comments = comments

    def wipe(self):
        for attribute in self.__slots__:
            self.__setattr__(attribute, None)

    def tweak(self, attribute: str, value):
        self.__setattr__(attribute, value)

    def load(self, first_name: str, last_name: str):
        pass
        # class method of find

    def find(self):
        pass

    def __str__(self):
        return str(Student.__slots__)


class Classroom:

    accepted_types = {
        'course_code': str,
        'course_name': str,
        'period': int,
        'teacher_name': str,
        'student': str,
        'assignments': tuple
    }

    __slots__ = ['course_code', 'course_name', 'period', 'teacher_name', 'student', 'assignments']

    def __init__(self, course_code=None, course_name=None, period=None, teacher_name=None,
                 student=None, assignements=None):
        self.course_code = course_code
        self.course_name = course_name
        self.period = period
        self.teacher_name = teacher_name
        self.student = student
        self.assignments = assignements

    def __str__(self):
        return str(Classroom.__slots__)


class Assignment:

    accepted_types = {
        'mark': float,
        'due': str,
        'name': str,
        'points': int
    }

    __slots__ = ['id', 'mark', 'due', 'name', 'points']

    def __init__(self, assig_id=None, mark=None, due=None, name=None, points=None):
        self.id = assig_id
        self.mark = mark
        self.due = due
        self.name = name
        self.points = points

    def __str__(self):
        return str(Assignment.__slots__)


print(sys.argv)
