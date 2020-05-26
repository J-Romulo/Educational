from Exceptions.NotFindError import NotFindError
from Exceptions.BlankFieldError import BlankFieldError
from Repositories.StudentRepository import *


class EditProfile:
    def __init__(self):
        pass

    @staticmethod
    def editStudentLogin(student, login, password, newLogin):
        try:
            if login and password and newLogin:

                if student.login == login and student.password == password:
                    StudentRepository.editProfile(student.id, 'login', newLogin)
                    student.login = newLogin

                else:
                    raise NotFindError()

            else:
                raise BlankFieldError()

        except NotFindError as editError:
            editError.throwGUI()

        except BlankFieldError as editError:
            editError.throwGUI()

    @staticmethod
    def editStudentPassword(student, login, password, newPassword):
        try:
            if login and password and newPassword:

                if student.login == login and student.password == password:
                    StudentRepository.editProfile(student.id, 'senha', newPassword)
                    student.password = newPassword
                else:
                    raise NotFindError()

            else:
                raise BlankFieldError()

        except NotFindError as editError:
            editError.throwGUI()

        except BlankFieldError as editError:
            editError.throwGUI()

    @staticmethod
    def editStudentName(student, login, password, newName):
        try:
            if login and password and newName:

                if student.login == login and student.password == password:
                    StudentRepository.editProfile(student.id, 'nome', newName)
                    student.name = newName

                else:
                    raise NotFindError()

            else:
                raise BlankFieldError()

        except NotFindError as editError:
            editError.throwGUI()

        except BlankFieldError as editError:
            editError.throwGUI()