from RepositorioAluno import *

class ModificarPerfil:
    def __init__(self):
        pass


    @staticmethod
    def modificarLoginAluno(aluno, login, senha, novoLogin):
        if(aluno.login == login and aluno.senha == senha):
            RepositorioAluno.modificarPerfil(aluno.id, 'login', novoLogin)
            aluno.login = novoLogin
        else:
            print(aluno.login)
            print(aluno.senha)
            print("Senha ou login errado")

        return aluno.login