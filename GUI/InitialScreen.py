from Facade.FcdStudent import *
from GUI.MenuStudent import *

mainFrame = tkinter.Tk()
mainFrame.title("Tela Inicial")


class InitialScreen:
    def __init__(self, master=None):
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.title = tkinter.Label(self.mainWidget, text="SistemaBD de gestão")
        self.title.pack()
        self.title["font"] = ("Arial", "20", "bold")

        self.loginWidget = tkinter.Frame(master)
        self.loginWidget.pack()

        self.loginLabel = tkinter.Label(self.loginWidget, text="Login")
        self.loginLabel["font"] = ("Arial", "13")
        self.loginLabel["width"] = ("13")
        self.loginLabel.pack(side=tkinter.LEFT)

        self.loginField = tkinter.Entry(self.loginWidget)
        self.loginField.pack()

        self.passwordWidget = tkinter.Frame(master)
        self.passwordWidget.pack()

        self.passwordLabel = tkinter.Label(self.passwordWidget, text="Senha")
        self.passwordLabel["font"] = ("Arial", "13")
        self.passwordLabel["width"] = ("13")
        self.passwordLabel.pack(side=tkinter.LEFT)

        self.passwordField = tkinter.Entry(self.passwordWidget)
        self.passwordField["show"] = "*"
        self.passwordField.pack()

        self.buttonWidget = tkinter.Frame(master)
        self.buttonWidget.pack()

        self.logButton = tkinter.Button(self.buttonWidget, text="Entrar")
        self.tipoLog = 1
        self.logButton["command"] = self.loginConfirm
        self.logButton.pack(side=tkinter.LEFT)

        self.registerButton = tkinter.Button(self.buttonWidget, text="Registrar")
        self.registerButton["command"] = self.registerScreen
        self.registerButton.pack()

        # Itens sem pack
        self.goBackButton = tkinter.Button(self.buttonWidget, text="Voltar")
        self.goBackButton["command"] = self.voltarTelaLogin

        self.nameWidget = tkinter.Frame(master)

        self.nameLabel = tkinter.Label(self.nameWidget, text="Nome completo")
        self.nameLabel["font"] = ("arial", "13")
        self.nameLabel["width"] = ("13")

        self.nameField = tkinter.Entry(self.nameWidget)

        self.ageWidget = tkinter.Frame(master)

        self.ageLabel = tkinter.Label(self.ageWidget, text="Nascimento")
        self.ageLabel["font"] = ("arial", "13")
        self.ageLabel["width"] = ("13")

        self.ageField = tkinter.Entry(self.ageWidget)

        self.emailWidget = tkinter.Frame(master)

        self.emailLabel = tkinter.Label(self.emailWidget, text="Email")
        self.emailLabel["font"] = ("arial", "13")
        self.emailLabel["width"] = ("13")

        self.emailField = tkinter.Entry(self.emailWidget)

        self.contactWidget = tkinter.Frame(master)

        self.contactLabel = tkinter.Label(self.contactWidget, text="Contato")
        self.contactLabel["font"] = ("arial", "13")
        self.contactLabel["width"] = ("13")

        self.contactField = tkinter.Entry(self.contactWidget)

    def loginConfirm(self):  # Função com muitas logica. Melhorar posteriormente! Utilizar a fachada
        if self.tipoLog == 1:
            user = self.loginField.get()
            password = self.passwordField.get()

            student = FcdStudent.log(user, password)

            if (student):
                mainFrame.destroy()

                mainFrame2 = tkinter.Tk()
                mainFrame2.title("Menu")
                mainFrame2.geometry('630x275')

                MenuStudent(student, mainFrame2)
                mainFrame2.mainloop()
        else:
            usuario = self.loginField.get()
            senha = self.passwordField.get()
            nome = self.nameField.get()
            idade = self.ageField.get()
            email = self.emailField.get()
            contato = self.contactField.get()

            aluno = FcdStudent.register(usuario, senha, nome, idade, email, contato)

            if (aluno):
                mainFrame.destroy()

                mainFrame2 = tkinter.Tk()
                mainFrame2.title("Menu")
                mainFrame2.geometry('630x275')

                MenuStudent(aluno, mainFrame2)
                mainFrame2.mainloop()

    def registerScreen(self):
        # Itens que vão ser mudados de local
        self.buttonWidget.pack_forget()
        self.logButton.pack_forget()
        self.registerButton.pack_forget()

        # Itens que irão aparecer na pagina depois do acionamento da função
        self.nameWidget.pack()
        self.nameLabel.pack(side=tkinter.LEFT)
        self.nameField.pack()

        self.ageWidget.pack()
        self.ageLabel.pack(side=tkinter.LEFT)
        self.ageField.pack()

        self.emailWidget.pack()
        self.emailLabel.pack(side=tkinter.LEFT)
        self.emailField.pack()

        self.contactWidget.pack()
        self.contactLabel.pack(side=tkinter.LEFT)
        self.contactField.pack()

        # Itens realocados
        self.buttonWidget.pack()
        self.logButton.pack(side=tkinter.LEFT)
        self.tipoLog = 2
        self.logButton["command"] = self.loginConfirm

        self.goBackButton.pack(side=tkinter.LEFT)

    def voltarTelaLogin(self):
        self.nameWidget.pack_forget()
        self.nameLabel.pack_forget()
        self.nameField.pack_forget()

        self.ageWidget.pack_forget()
        self.ageLabel.pack_forget()
        self.ageField.pack_forget()

        self.emailWidget.pack_forget()
        self.emailLabel.pack_forget()
        self.emailField.pack_forget()

        self.contactWidget.pack_forget()
        self.contactLabel.pack_forget()
        self.contactField.pack_forget()

        self.goBackButton.pack_forget()

        self.tipoLog = 1
        self.registerButton.pack(side=tkinter.LEFT)


InitialScreen(mainFrame)
mainFrame.mainloop()
