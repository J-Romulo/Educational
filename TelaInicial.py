import tkinter
from Login import *
#from RepositorioAluno import *
from MenuAluno import *
#from Aluno import *

janelaPrincipal= tkinter.Tk()
janelaPrincipal.title("Tela Inicial")


class TelaInicial:
    def __init__(self, master=None):
        self.widgetPrincipal = tkinter.Frame(master)
        self.widgetPrincipal.pack()

        self.titulo = tkinter.Label(self.widgetPrincipal, text="SistemaBD de gestão")
        self.titulo.pack()
        self.titulo["font"] = ("Arial", "20", "bold")



        self.widgetLogin = tkinter.Frame(master)
        self.widgetLogin.pack()

        self.labelLogin = tkinter.Label(self.widgetLogin, text="Login")
        self.labelLogin["font"] = ("Arial", "13")
        self.labelLogin["width"] = ("13")
        self.labelLogin.pack(side=tkinter.LEFT)

        self.campoLogin = tkinter.Entry(self.widgetLogin)
        self.campoLogin.pack()



        self.widgetSenha = tkinter.Frame(master)
        self.widgetSenha.pack()

        self.labelSenha = tkinter.Label(self.widgetSenha, text="Senha")
        self.labelSenha["font"] = ("Arial", "13")
        self.labelSenha["width"] = ("13")
        self.labelSenha.pack(side=tkinter.LEFT)

        self.campoSenha = tkinter.Entry(self.widgetSenha)
        self.campoSenha["show"] = "*"
        self.campoSenha.pack()



        self.widgetBotao = tkinter.Frame(master)
        self.widgetBotao.pack()

        self.botaoLog = tkinter.Button(self.widgetBotao, text="Entrar")
        self.tipoLog = 1
        self.botaoLog["command"] = self.confirmarLogin
        self.botaoLog.pack(side=tkinter.LEFT)

        self.botaoRegistrar = tkinter.Button(self.widgetBotao, text="Registrar")
        self.botaoRegistrar["command"] = self.telaRegistro
        self.botaoRegistrar.pack()

        # Itens sem pack
        self.botaoVoltar = tkinter.Button(self.widgetBotao, text="Voltar")
        self.botaoVoltar["command"] = self.voltarTelaLogin


        self.widgetNome = tkinter.Frame(master)

        self.labelNome = tkinter.Label(self.widgetNome, text="Nome completo")
        self.labelNome["font"] = ("arial", "13")
        self.labelNome["width"] = ("13")

        self.campoNome = tkinter.Entry(self.widgetNome)


        self.widgetIdade = tkinter.Frame(master)

        self.labelIdade = tkinter.Label(self.widgetIdade, text="Idade")
        self.labelIdade["font"] = ("arial", "13")
        self.labelIdade["width"] = ("13")

        self.campoIdade = tkinter.Entry(self.widgetIdade)



        self.widgetEmail = tkinter.Frame(master)

        self.labelEmail = tkinter.Label(self.widgetEmail, text="Email")
        self.labelEmail["font"] = ("arial", "13")
        self.labelEmail["width"] = ("13")

        self.campoEmail = tkinter.Entry(self.widgetEmail)



        self.widgetContato = tkinter.Frame(master)

        self.labelContato = tkinter.Label(self.widgetContato, text="Contato")
        self.labelContato["font"] = ("arial", "13")
        self.labelContato["width"] = ("13")

        self.campoContato = tkinter.Entry(self.widgetContato)

    def confirmarLogin(self):
        if self.tipoLog == 1:
            usuario = self.campoLogin.get()
            senha = self.campoSenha.get()

            aluno = Login.log(usuario, senha)

            janelaPrincipal.destroy()

            janelaPrincipal2 = tkinter.Tk()
            janelaPrincipal2.title("Menu")
            janelaPrincipal2.geometry('500x225')

            MenuAluno(aluno, janelaPrincipal2)
            janelaPrincipal2.mainloop()
        else:
            usuario = self.campoLogin.get()
            senha = self.campoSenha.get()
            nome = self.campoNome.get()
            idade = self.campoIdade.get()
            email = self.campoEmail.get()
            contato = self.campoContato.get()

            aluno = Login.registrar(usuario, senha, nome, idade, email, contato)

            janelaPrincipal.destroy()

            janelaPrincipal2 = tkinter.Tk()
            janelaPrincipal2.title("Menu")
            janelaPrincipal2.geometry('500x225')

            MenuAluno(aluno, janelaPrincipal2)
            janelaPrincipal2.mainloop()



    def telaRegistro(self):
        # Itens que vão ser mudados de local
        self.widgetBotao.pack_forget()
        self.botaoLog.pack_forget()
        self.botaoRegistrar.pack_forget()

        # Itens que irão aparecer na pagina depois do acionamento da função
        self.widgetNome.pack()
        self.labelNome.pack(side=tkinter.LEFT)
        self.campoNome.pack()

        self.widgetIdade.pack()
        self.labelIdade.pack(side=tkinter.LEFT)
        self.campoIdade.pack()

        self.widgetEmail.pack()
        self.labelEmail.pack(side=tkinter.LEFT)
        self.campoEmail.pack()

        self.widgetContato.pack()
        self.labelContato.pack(side=tkinter.LEFT)
        self.campoContato.pack()

        # Itens realocados
        self.widgetBotao.pack()
        self.botaoLog.pack(side=tkinter.LEFT)
        self.tipoLog = 2
        self.botaoLog["command"] = self.confirmarLogin

        self.botaoVoltar.pack(side=tkinter.LEFT)

    def voltarTelaLogin(self):
        self.widgetNome.pack_forget()
        self.labelNome.pack_forget()
        self.campoNome.pack_forget()

        self.widgetIdade.pack_forget()
        self.labelIdade.pack_forget()
        self.campoIdade.pack_forget()

        self.widgetEmail.pack_forget()
        self.labelEmail.pack_forget()
        self.campoEmail.pack_forget()

        self.widgetContato.pack_forget()
        self.labelContato.pack_forget()
        self.campoContato.pack_forget()

        self.botaoVoltar.pack_forget()

        self.tipoLog = 1
        self.botaoRegistrar.pack(side=tkinter.LEFT)


TelaInicial(janelaPrincipal)
janelaPrincipal.mainloop()