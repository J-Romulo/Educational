from Login import *
from ModificarPerfil import *

class FcdAluno:
    def __init__(self):
        pass

    @staticmethod
    def logar(usuario, senha):
        aluno = Login.log(usuario, senha)

        return aluno


    @staticmethod
    def registrar(usuario, senha, nome, idade, email, contato):
        aluno = Login.registrar(usuario, senha, nome, idade, email, contato)

        return aluno

    @staticmethod
    def modificarSenha(aluno, login, senha, novaSenha):
        ModificarPerfil.modificarSenhaAluno(aluno, login, senha, novaSenha)

    @staticmethod
    def modificarLogin(aluno, login, senha, novoLogin):
        ModificarPerfil.modificarLoginAluno(aluno, login, senha, novoLogin)

    @staticmethod
    def modificarNome(aluno, login, senha, novoNome):
        ModificarPerfil.modificarNomeAluno(aluno, login, senha, novoNome)

