from tkinter import messagebox

class BlankFieldError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Preencha todos os campos para continuar"

    def throwGUI(self):
        messagebox.showerror("Error", "{}".format(self.__str__()))

