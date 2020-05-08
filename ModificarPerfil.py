from Repositorios.RepositorioAluno import *

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

    @staticmethod
    def modificarSenhaAluno(aluno, login, senha, novaSenha):
        if(aluno.login == login and aluno.senha == senha):
            RepositorioAluno.modificarPerfil(aluno.id, 'senha', novaSenha)
            aluno.senha = novaSenha
        else:
            print(aluno.login)
            print(aluno.senha)
            print("Senha ou login errado")

        return aluno.senha

    @staticmethod
    def modificarNomeAluno(aluno, login, senha, novoNome):
        if (aluno.login == login and aluno.senha == senha):
            RepositorioAluno.modificarPerfil(aluno.id, 'nome', novoNome)
            aluno.nome = novoNome
        else:
            print(aluno.login)
            print(aluno.senha)
            print("Senha ou login errado")

        return aluno.nome