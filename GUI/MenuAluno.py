from GUI.TelaEdit import *

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

    def modificar(self):
        self.botaoModificar.pack_forget()

        self.botaoModificarLogin.pack(side=tkinter.LEFT)
        self.botaoModificarLogin["command"] = self.telaLogin

        self.botaoModificarSenha.pack(side=tkinter.LEFT)
        self.botaoModificarSenha["command"] = self.telaSenha

        self.botaoModificarNome.pack(side=tkinter.LEFT)
        self.botaoModificarNome["command"] = self.telaNome

    
    def telaLogin(self):
        janelaEdit = tkinter.Tk()
        janelaEdit.title("Modificar Login")
        janelaEdit.geometry('200x150')

        TelaEdit(self.aluno, 1, janelaEdit)
        janelaEdit.mainloop()


    def telaSenha(self):
        janelaEdit = tkinter.Tk()
        janelaEdit.title("Modificar Senha")
        janelaEdit.geometry('200x150')

        TelaEdit(self.aluno, 2, janelaEdit)
        janelaEdit.mainloop()


    def telaNome(self):
        janelaEdit = tkinter.Tk()
        janelaEdit.title("Modificar Nome")
        janelaEdit.geometry('200x150')

        TelaEdit(self.aluno, 3, janelaEdit)
        janelaEdit.mainloop()