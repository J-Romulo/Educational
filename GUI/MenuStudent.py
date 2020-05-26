from GUI.EditScreen import *

class MenuStudent:
    def __init__(self, student, master=None):
        self.student = student
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.titleLabel = tkinter.Label(self.mainWidget, text="Menu Principal do Aluno")
        self.titleLabel["font"] = ("Arial", "15", "bold")
        self.titleLabel.pack()



        self.profileInfoWidget = tkinter.Frame(master)
        self.profileInfoWidget.pack()

        self.nameLabel = tkinter.Label(self.profileInfoWidget)
        self.nameLabel["text"] = ("Nome: {}".format(student.name))
        self.nameLabel.pack(side=tkinter.LEFT)

        self.ageLabel = tkinter.Label(self.profileInfoWidget)
        self.ageLabel["text"] = ("Idade: {}".format(student.age))
        self.ageLabel.pack(side=tkinter.LEFT)

        self.emailLabel = tkinter.Label(self.profileInfoWidget)
        self.emailLabel["text"] = ("Email: {}".format(student.email))
        self.emailLabel.pack(side=tkinter.LEFT)

        self.contactLabel = tkinter.Label(self.profileInfoWidget)
        self.contactLabel["text"] = ("Contato: {}".format(student.contact))
        self.contactLabel.pack(side=tkinter.LEFT)



        self.optionsWidget = tkinter.Frame(master)
        self.optionsWidget.pack()

        self.openEditProfileAreaButton = tkinter.Button(self.optionsWidget, text='Modificar Perfil')
        self.openEditProfileAreaButton.pack(side=tkinter.LEFT)
        self.openEditProfileAreaButton["command"] = self.edit


        #Itens sem pack
        self.editNameButton = tkinter.Button(self.optionsWidget, text='Atualizar Nome')
        self.editLoginButton = tkinter.Button(self.optionsWidget, text='Atualizar Login')
        self.editPasswordButton = tkinter.Button(self.optionsWidget, text='Atualizar Senha')

        self.editFieldsAreaWidget = tkinter.Frame(master)

    def edit(self):
        self.openEditProfileAreaButton.pack_forget()

        self.editLoginButton.pack(side=tkinter.LEFT)
        self.editLoginButton["command"] = self.loginScreen

        self.editPasswordButton.pack(side=tkinter.LEFT)
        self.editPasswordButton["command"] = self.passwordScreen

        self.editNameButton.pack(side=tkinter.LEFT)
        self.editNameButton["command"] = self.nameScreen

    
    def loginScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Login")
        EditScr.geometry('200x150')

        EditScreen(self.student, 1, EditScr)
        EditScr.mainloop()


    def passwordScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Senha")
        EditScr.geometry('200x150')

        EditScreen(self.student, 2, EditScr)
        EditScr.mainloop()


    def nameScreen(self):
        EditScr = tkinter.Tk()
        EditScr.title("Modificar Nome")
        EditScr.geometry('200x150')

        EditScreen(self.student, 3, EditScr)
        EditScr.mainloop()