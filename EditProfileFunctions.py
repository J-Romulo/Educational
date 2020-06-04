from Exceptions.NotFindError import NotFindError
from Exceptions.BlankFieldError import BlankFieldError
from Repositories.StudentRepository import *


class EditProfile:
    def __init__(self):
        pass

    @staticmethod
    def editStudentLogin(student, passedLogin, passedPassword, newLogin):
        try:
            if passedLogin and passedPassword and newLogin:

                if student.login == passedLogin and student.password == passedPassword:
                    StudentRepository.editProfileField(student.login, 'login', newLogin)
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
    def editStudentPassword(student, passedLogin, passedPassword, newPassword):
        try:
            if passedLogin and passedPassword and newPassword:

                if student.login == passedLogin and student.password == passedPassword:
                    StudentRepository.editProfileField(student.login, 'senha', newPassword)
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
                    StudentRepository.editProfileField(student.login, 'nome', newName)
                    student.name = newName

                else:
                    raise NotFindError()

            else:
                raise BlankFieldError()

        except NotFindError as editError:
            editError.throwGUI()

        except BlankFieldError as editError:
            editError.throwGUI()