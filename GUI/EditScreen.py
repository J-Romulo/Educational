import tkinter
from tkinter import messagebox
from Facade.FcdStudent import *


class EditScreen:
    def __init__(self, student, tipoTela, master=None):
        self.student = student
        self.master = master

        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()


        self.loginConfirmLabel = tkinter.Label(self.mainWidget, text='Confirme seu Login: ')
        self.loginConfirmLabel.pack()

        self.loginConfirmField = tkinter.Entry(self.mainWidget)
        self.loginConfirmField.pack()

        self.passwordConfirmLabel = tkinter.Label(self.mainWidget, text='Confirme sua senha')
        self.passwordConfirmLabel.pack()

        self.passwordConfirmField = tkinter.Entry(self.mainWidget)
        self.passwordConfirmField.pack()


        self.newLoginLabel = tkinter.Label(self.mainWidget, text='Login Novo: ')
        self.newLoginField = tkinter.Entry(self.mainWidget)

        self.newPasswordLabel = tkinter.Label(self.mainWidget, text='Senha Nova: ')
        self.newPasswordField = tkinter.Entry(self.mainWidget)

        self.newNameLabel = tkinter.Label(self.mainWidget, text='Novo nome: ')
        self.newNameField = tkinter.Entry(self.mainWidget)

        self.saveButton = tkinter.Button(self.mainWidget, text='Salvar')

        if(tipoTela == 1):
            self.newLoginLabel.pack()
            self.newLoginField.pack()
            self.saveButton.pack()
            self.saveButton["command"] = self.editLogin

        elif(tipoTela == 2):
            self.newPasswordLabel.pack()
            self.newPasswordField.pack()
            self.saveButton.pack()
            self.saveButton["command"] = self.editPassword

        else:
            self.newNameLabel.pack()
            self.newNameField.pack()
            self.saveButton.pack()
            self.saveButton["command"] = self.editName


    def editLogin(self):
        login = self.loginConfirmField.get()
        password = self.passwordConfirmField.get()
        newLogin = self.newLoginField.get()

        answer = messagebox.askyesno("Está seguro?", "Você tem certeza que quer mudar seu login?")

        if answer:
            expectedBehavior = FcdStudent.editLogin(self.student, login, password, newLogin)

            if expectedBehavior:
                self.master.destroy()
                messagebox.showinfo("Login Atualizado", "Seu login foi atualizado com sucesso!")
        else:
            self.master.destroy()
            messagebox.showinfo("Cancelado com sucesso","Procedimento de mudança de login cancelado.")



    def editPassword(self):
        login = self.loginConfirmField.get()
        password = self.passwordConfirmField.get()
        newPassword = self.newPasswordField.get()

        answer = messagebox.askyesno("Está seguro?", "Você tem certeza que quer mudar sua senha?")

        if answer:
            expectedBehavior = FcdStudent.editPassword(self.student, login, password, newPassword)

            if expectedBehavior:
                self.master.destroy()
                messagebox.showinfo("Senha Atualizada", "Sua senha foi atualizada com sucesso!")

        else:
            self.master.destroy()
            messagebox.showinfo("Cancelado com sucesso","Procedimento de mudança de senha cancelado.")



    def editName(self):
        login = self.loginConfirmField.get()
        password = self.passwordConfirmField.get()
        newName = self.newNameField.get()

        answer = messagebox.askyesno("Está seguro?", "Você tem certeza que quer mudar seu nome?")

        if answer:
            expectedBehavior = FcdStudent.editName(self.student, login, password, newName)

            if expectedBehavior:
                self.master.destroy()
                messagebox.showinfo("Nome Atualizado", "Seu nome foi atualizado com sucesso!")

        else:
            self.master.destroy()
            messagebox.showinfo("Cancelado com sucesso", "Procedimento de mudança de nome cancelado.")