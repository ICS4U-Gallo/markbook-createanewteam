#! /usr/bin/env python3
import pickle
import tabulate  # External library to simplify tabular printing


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

    def tweak(self, attribute: str, value) -> None:

        """
        :param attribute: name of classroom attribute to be modified. if attribute
        does not exist it is created
        :param value: value associated to attribute being modified. overwrites any
        existing value associated to that attribute
        :return: no returns, modifies existing and/or creates attributes
        """

        self.__setattr__(attribute, value)

    def __str__(self):
        return str(list(Assignment.accepted_types.keys()))

    def __getitem__(self, item):
        return getattr(self, item)


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

    def wipe(self) -> None:

        """
        :return: no returns, clears all information
        """

        for attribute in Student.accepted_types.keys():
            self.__setattr__(attribute, None)

    def tweak(self, attribute: str, value) -> None:

        """
        :param attribute: name of classroom attribute to be modified. if attribute
        does not exist it is created
        :param value: value associated to attribute being modified. overwrites any
        existing value associated to that attribute
        :return: no returns, modifies existing and/or creates attributes
        """

        self.__setattr__(attribute, value)

    def print_info(self) -> None:
        data = self.__dict__
        for key in data.keys():
            data[key] = [data[key]]
        print(tabulate.tabulate(data, data.keys(), tablefmt='fancy_grid'))

    def __str__(self):
        return str(self.__dict__)

    def __getitem__(self, item):
        return getattr(self, item)


class Classroom:
    accepted_types = {
        'class_name': str,
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
        self.students = {}  # dict containing Student instances of all students in the classroom
        self.assignments = assignements

        if students is not None:
            for student in students:
                self.students.update({'{} {}'.format(student.last_name, student.first_name): student})
        else:
            pass

    def tweak(self, attribute: str, value) -> None:

        """
        :param attribute: name of classroom attribute to be modified. if attribute
        does not exist it is created
        :param value: value associated to attribute being modified. overwrites any
        existing value associated to that attribute
        :return: no returns, modifies existing and/or creates attributes
        """

        self.__setattr__(attribute, value)

    def add_student(self, student: Student) -> None:

        """
        :param student: student to be added, must be instance of Student class
        :return: no returns, adds given student to classroom instance
        """

        self.students.update({'{} {}'.format(student.last_name, student.first_name): student})

    def remove_student(self, first_name: str, last_name: str) -> None:

        """
        :param first_name: first name of student to be removed
        :param last_name: last name of student to be removed
        :return: no returns, removes student from classroom instance
        """

        self.students.pop('{} {}'.format(last_name, first_name))

    def wipe(self) -> None:

        """
        :return: no returns, clears all students and information
        """

        self.students.update({})
        for attribute in self.accepted_types.keys():
            self.__setattr__(attribute, None)

    def print_students(self) -> None:
        header = Student.accepted_types.keys()
        data = []
        for student in self.students.values():
            data.append([info for info in student.__dict__.values()])  # prints student dict needs fixing

        print(tabulate.tabulate(data, header, tablefmt='fancy_grid'))

    def inspect(self, student_fullname: str) -> None:

        """
        :param student_fullname: full first and last name of student to be inspected. last name, first name
        :return: no returns, prints out all info of inspected student
        """

        print(self.students[student_fullname])

    def __str__(self):
        return str(list(Classroom.accepted_types.keys()))  # temporary

    def __len__(self):
        return len(self.students.items())

    def __getitem__(self, item):
        return getattr(self, item)


class Book:

    def __init__(self):
        self.classrooms = {}  # dict containing Classroom instances of all the classrooms

    def add_class(self, classroom: Classroom) -> None:

        """
        :param classroom: classroom to be added, must be instance of Classroom class
        :return: no returns, adds given Classroom instance to dict of classrooms
        """

        self.classrooms.update({classroom.class_name: classroom})

    def remove_class(self, class_name: str) -> None:

        """
        :param class_name: name of the classroom to be removed
        :return: no returns, removes classroom of user's choosing
        """

        self.classrooms.pop(class_name)

    def save(self, save_name: str, protocol=0):

        """
        :param save_name: name of the file to be saved
        :param protocol: tells the pickler to use a given protocol
        :return: no returns, saves as pickled file of the Book instance to hard disk
        """

        file = open(save_name, 'wb')
        pickle.dump(self, file, protocol=protocol)
        file.close()

    @staticmethod
    def load(file_path: str):

        """
        :param file_path: file path of the file containing the Book instance to be loaded
        :return: returns Book instance of previously saved session
        """

        file = open(file_path, 'rb')
        session = pickle.load(file)
        file.close()

        return session

    def wipe(self) -> None:

        """
        :return: no returns, clears all classrooms
        """

        self.classrooms.update({})

    def print_classrooms(self, return_str=False):
        header = Classroom().__dict__
        # header.pop('students')

        data = []
        for room in self.classrooms.values():
            data.append([info for info in room.__dict__.values()])

        to_print = tabulate.tabulate(data, header, tablefmt='fancy_grid')
        if return_str:
            return to_print
        else:
            print(to_print)

    def tweak(self, class_name: str, attribute: str, value) -> None:
        self.classrooms[class_name].tweak(attribute, value)

    def inspect(self, class_name: str) -> None:
        self.classrooms[class_name].print_students()

    def find(self, first_name: str, last_name: str):

        """
        :param first_name: first name of student to be returned
        :param last_name: last name of student to be returned
        :return: searches all classrooms for specific student, returns instance to according student if found.
        returns False if student does not exist
        """

        pass  # Not Finished

    def __str__(self):
        return str(self.classrooms)

    def __len__(self):
        return len(self.classrooms.items())

    def __getitem__(self, item):
        return getattr(self, item)


book = Book()

stud = Student(first_name='John', last_name='Smith', gender='M')
stud2 = Student(first_name='Maria', last_name='Dick', gender='F')
stud3 = Student(first_name='Robert', last_name='DiNero', gender='M')
stud4 = Student(first_name='James', last_name='Harris', gender='M')

classroom = Classroom(students=[stud, stud2, stud3, stud4])
classroom.tweak('class_name', '12 Gallo')

book.add_class(classroom)
book.tweak('12 Gallo', 'course_code', 'ICS4U1')

# book.print_classrooms() book classroom printing needs fixing

classroom.print_students()


room = book.classrooms['12 Gallo']
room.print_students()

room.students['DiNero Robert'].tweak('student_number', 5386492)

room.print_students()


