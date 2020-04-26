import tkinter
from ModificarPerfil import *

class MenuAluno:
    def __init__(self, aluno, master=None):
        self.aluno = aluno
        self.widgetPrincipal = tkinter.Frame(master)
        self.widgetPrincipal.pack()

        self.LabelTitulo = tkinter.Label(self.widgetPrincipal, text="Menu Principal do Aluno")
        self.LabelTitulo["font"] = ("Arial", "15", "bold")
        self.LabelTitulo.pack()



        self.widgetInfoPerfil = tkinter.Frame(master)
        self.widgetInfoPerfil.pack()

        self.labelNome = tkinter.Label(self.widgetInfoPerfil)
        self.labelNome["text"] = ("Nome: {}".format(aluno.nome))
        self.labelNome.pack(side=tkinter.LEFT)

        self.labelIdade = tkinter.Label(self.widgetInfoPerfil)
        self.labelIdade["text"] = ("Idade: {}".format(aluno.idade))
        self.labelIdade.pack(side=tkinter.LEFT)

        self.labelEmail = tkinter.Label(self.widgetInfoPerfil)
        self.labelEmail["text"] = ("Email: {}".format(aluno.email))
        self.labelEmail.pack(side=tkinter.LEFT)

        self.labelContato = tkinter.Label(self.widgetInfoPerfil)
        self.labelContato["text"] = ("Contato: {}".format(aluno.contato))
        self.labelContato.pack(side=tkinter.LEFT)



        self.widgetOpcoes = tkinter.Frame(master)
        self.widgetOpcoes.pack()

        self.botaoModificar = tkinter.Button(self.widgetOpcoes, text='Modificar Perfil')
        self.botaoModificar.pack(side=tkinter.LEFT)
        self.botaoModificar["command"] = self.modificar


        #Itens sem pack
        self.botaoModificarNome = tkinter.Button(self.widgetOpcoes, text='Atualizar Nome')
        self.botaoModificarLogin = tkinter.Button(self.widgetOpcoes, text='Atualizar Login')
        self.botaoModificarSenha = tkinter.Button(self.widgetOpcoes, text='Atualizar Senha')

        self.widgetCamposModificar = tkinter.Frame(master)

        self.labelLoginConfir = tkinter.Label(self.widgetCamposModificar, text='Confirme seu Login: ')
        self.entryLoginConfir = tkinter.Entry(self.widgetCamposModificar)

        self.labelSenhaConfir = tkinter.Label(self.widgetCamposModificar, text='Confirme sua senha')
        self.entrySenhaConfir = tkinter.Entry(self.widgetCamposModificar)

        self.labelLoginNovo = tkinter.Label(self.widgetCamposModificar, text='Login Novo: ')
        self.entryLoginNovo = tkinter.Entry(self.widgetCamposModificar)

        self.labelSenhaNova = tkinter.Label(self.widgetCamposModificar, text='Senha Nova: ')
        self.entrySenhaNova = tkinter.Entry(self.widgetCamposModificar)

        self.botaoSalvar = tkinter.Button(self.widgetCamposModificar, text='Salvar')

    def modificar(self):
        self.botaoModificar.pack_forget()

        self.botaoModificarLogin.pack(side=tkinter.LEFT)
        self.botaoModificarLogin["command"] = self.camposLogin

        self.botaoModificarSenha.pack(side=tkinter.LEFT)
        self.botaoModificarSenha["command"] = self.modificarSenha

        self.botaoModificarNome.pack(side=tkinter.LEFT)

    
    def camposLogin(self):
        self.labelSenhaNova.pack_forget()
        self.entrySenhaNova.pack_forget()
        self.botaoSalvar.pack_forget()

        self.widgetCamposModificar.pack()

        self.labelLoginConfir.pack()
        self.entryLoginConfir.pack()

        self.labelSenhaConfir.pack()
        self.entrySenhaConfir.pack()

        self.labelLoginNovo.pack()
        self.entryLoginNovo.pack()

        self.botaoSalvar.pack()
        self.botaoSalvar["command"] = self.modificarLogin

    def modificarLogin(self):
        login = self.entryLoginConfir.get()
        senha = self.entrySenhaConfir.get()
        novoLogin = self.entryLoginNovo.get()

        log = ModificarPerfil.modificarLoginAluno(self.aluno, login, senha, novoLogin)
        self.aluno.login = log

    def modificarSenha(self):
        self.labelLoginNovo.pack_forget()
        self.entryLoginNovo.pack_forget()
        self.botaoSalvar.pack_forget()

        self.widgetCamposModificar.pack()

        self.labelLoginConfir.pack()
        self.entryLoginConfir.pack()

        self.labelSenhaConfir.pack()
        self.entrySenhaConfir.pack()

        self.labelSenhaNova.pack()
        self.entrySenhaNova.pack()

        self.botaoSalvar.pack()




        



