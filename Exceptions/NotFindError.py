from tkinter import messagebox

class NotFindError(IndexError):
    def __init__(self):
        pass

    def __str__(self):
        return "Nome de usuário e/ou senha incorretos\nNenhum usuário encontrado"

    def throwGUI(self):
        messagebox.showerror("Error", "{}".format(self.__str__()))
