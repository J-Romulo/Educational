from InitialScreenFunctions import *
from EditProfileFunctions import *

class FcdStudent:
    def __init__(self):
        pass

    @staticmethod
    def log(usuario, senha):
        return InitialScreenFunctions.log(usuario, senha)


    @staticmethod
    def register(usuario, senha, nome, idade, email, contato):
        return InitialScreenFunctions.register(usuario, senha, nome, idade, email, contato)

    @staticmethod
    def editPassword(student, login, senha, novaSenha):
        return EditProfileFunctions.editStudentPassword(student, login, senha, novaSenha)


    @staticmethod
    def editLogin(student, login, senha, novoLogin):
        return EditProfileFunctions.editStudentLogin(student, login, senha, novoLogin)


    @staticmethod
    def editName(student, login, senha, novoNome):
        return EditProfileFunctions.editStudentName(student, login, senha, novoNome)
