import tkinter

class MenuAluno:
    def __init__(self, aluno, master=None):
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


