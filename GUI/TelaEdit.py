import tkinter
from Facade.FcdAluno import *

class TelaEdit:
    def __init__(self, aluno, tipoTela, master=None):
        self.aluno = aluno

        self.widgetPrincipal = tkinter.Frame(master)
        self.widgetPrincipal.pack()


        self.labelLoginConfir = tkinter.Label(self.widgetPrincipal, text='Confirme seu Login: ')
        self.labelLoginConfir.pack()

        self.entryLoginConfir = tkinter.Entry(self.widgetPrincipal)
        self.entryLoginConfir.pack()

        self.labelSenhaConfir = tkinter.Label(self.widgetPrincipal, text='Confirme sua senha')
        self.labelSenhaConfir.pack()

        self.entrySenhaConfir = tkinter.Entry(self.widgetPrincipal)
        self.entrySenhaConfir.pack()


        self.labelLoginNovo = tkinter.Label(self.widgetPrincipal, text='Login Novo: ')
        self.entryLoginNovo = tkinter.Entry(self.widgetPrincipal)

        self.labelSenhaNova = tkinter.Label(self.widgetPrincipal, text='Senha Nova: ')
        self.entrySenhaNova = tkinter.Entry(self.widgetPrincipal)

        self.labelNomeNovo = tkinter.Label(self.widgetPrincipal, text='Novo nome: ')
        self.entryNomeNovo = tkinter.Entry(self.widgetPrincipal)

        self.botaoSalvar = tkinter.Button(self.widgetPrincipal, text='Salvar')

        if(tipoTela == 1):
            self.labelLoginNovo.pack()
            self.entryLoginNovo.pack()
            self.botaoSalvar.pack()
            self.botaoSalvar["command"] = self.modificarLogin

        elif(tipoTela == 2):
            self.labelSenhaNova.pack()
            self.entrySenhaNova.pack()
            self.botaoSalvar.pack()
            self.botaoSalvar["command"] = self.modificarSenha

        else:
            self.labelNomeNovo.pack()
            self.entryNomeNovo.pack()
            self.botaoSalvar.pack()
            self.botaoSalvar["command"] = self.modificarNome


    def modificarLogin(self):
        login = self.entryLoginConfir.get()
        senha = self.entrySenhaConfir.get()
        novoLogin = self.entryLoginNovo.get()

        FcdAluno.modificarLogin(self.aluno, login, senha, novoLogin)

    def modificarSenha(self):
        login = self.entryLoginConfir.get()
        senha = self.entrySenhaConfir.get()
        novaSenha = self.entrySenhaNova.get()

        FcdAluno.modificarSenha(self.aluno, login, senha, novaSenha)

    def modificarNome(self):
        login = self.entryLoginConfir.get()
        senha = self.entrySenhaConfir.get()
        novoNome = self.entryNomeNovo.get()

        FcdAluno.modificarNome(self.aluno, login, senha, novoNome)