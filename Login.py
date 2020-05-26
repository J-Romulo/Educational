from Exceptions.BlankFieldError import BlankFieldError
from Exceptions.NotFindError import NotFindError
from Repositories.StudentRepository import *
from Entities.Student import *


class Login:
    def __init__(self):
        pass

    @staticmethod
    def log(login, password):
        try:
            if login and password:
                student = StudentRepository.searchStudentLogin(login, password)
                loggedStudent = Student(student[0][1], student[0][2], student[0][3], student[0][4], student[0][5], student[0][6],
                                    student[0][0])
            else:
                raise BlankFieldError()

        except IndexError:
            try:
                raise NotFindError()
            except NotFindError as logError:
                logError.throwGUI()

        except BlankFieldError as logError:
            logError.throwGUI()

        else:
            return loggedStudent

    @staticmethod
    def register(login, password, name, age, email, contact):
        try:
            if login and password and name and age and email and contact:
                student = Student(login, password, name, age, email, contact)
                StudentRepository.save(student)
            else:
                raise BlankFieldError()

        except BlankFieldError as logError:
            logError.throwGUI()

        else:
            return student
