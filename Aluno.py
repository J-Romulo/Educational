class Aluno:

    def __init__(self, login, senha, nome, idade, email, contato, id=None):
        self.__nome = nome
        self.__idade = idade
        self.__contato = contato
        self.__login = login
        self.__senha = senha
        self.__email = email
        self.__id = id


    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def email(self):
        return self.__email

    @property
    def contato(self):
        return self.__contato

    @property
    def id(self):
        return self.__id


    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @email.setter
    def email(self, email):
        self.__email = email

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

    @id.setter
    def id(self, id):
        self.__id = id
