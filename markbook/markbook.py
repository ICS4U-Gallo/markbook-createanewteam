#! /usr/bin/env python3
import pickle


class Assignment:

    accepted_types = {
        'mark': float,
        'due': str,
        'name': str,
        'points': int
    }

    def __init__(self, mark=None, due=None, name=None, points=None):
        self.mark = mark
        self.due = due
        self.name = name
        self.points = points

    def tweak(self, attribute: str, value):
        self.__setattr__(attribute, value)

    def __str__(self):
        return str(list(Assignment.accepted_types.keys()))


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
        for attribute in Student.accepted_types.keys():
            self.__setattr__(attribute, None)

    def tweak(self, attribute: str, value):
        self.__setattr__(attribute, value)

    def __str__(self):
        return str(list(Student.accepted_types.keys()))  # Temporary


class Classroom:
    accepted_types = {
        'course_code': str,
        'course_name': str,
        'period': int,
        'teacher_name': str,
        'students': list,
        'assignments': tuple
    }

    def __init__(self, class_name=None, course_code=None, course_name=None, period=None, teacher_name=None,
                 students=None, assignements=None):
        self.class_name = class_name
        self.course_code = course_code
        self.course_name = course_name
        self.period = period
        self.teacher_name = teacher_name
        self.students = {}
        self.assignments = assignements

        if students is not None:
            for student in students:
                self.students.update({'{} {}'.format(student.last_name, student.first_name): student})
        else:
            pass

    def tweak(self, attribute: str, value):
        self.__setattr__(attribute, value)

    def add_student(self, student: Student):
        self.students.update({'{} {}'.format(student.last_name, student.first_name): student})

    def remove_student(self, first_name: str, last_name: str):
        self.students.pop('{} {}'.format(last_name, first_name))

    def wipe(self):
        self.students.update({})

    def __str__(self):
        return str(list(Classroom.accepted_types.keys()))  # Temporary

    def __len__(self):
        return len(self.students.items())


class Book:

    def __init__(self):
        self.classrooms = {}

    def add_class(self, classroom: Classroom):
        self.classrooms.update({classroom.class_name: classroom})

    def remove_class(self, class_name: str):
        self.classrooms.pop(class_name)

    def save(self, save_name: str, protocol=0):
        file = open(save_name, 'wb')
        pickle.dump(self, file, protocol=protocol)
        file.close()

    @staticmethod
    def load(file_path: str):
        file = open(file_path, 'rb')
        session = pickle.load(file)
        file.close()

        return session

    def __str__(self):
        return str(Book.__slots__)

    def __len__(self):
        return len(self.classrooms.items())
