from Repositorios.RepositorioAluno import *
from Aluno import *


class Login:
    def __init__(self):
        pass

    @staticmethod
    def log(usuario, senha):
        aluno = RepositorioAluno.procurarAlunoLogin(usuario, senha)
        alunoLogado = Aluno(aluno[0][1], aluno[0][2], aluno[0][3], aluno[0][4], aluno[0][5], aluno[0][6], aluno[0][0])

        return alunoLogado

    @staticmethod
    def registrar(login, senha, nome, idade, email, contato):
        aluno = Aluno(login, senha, nome, idade, email, contato)
        RepositorioAluno.salvar(aluno)

        return aluno