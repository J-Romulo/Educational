from tkinter import messagebox

class DuplicateGradeSheet(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Você já está cadastrado(a) nesse curso!"

    def throwGUI(self):
        messagebox.showerror("Error", "{}".format(self.__str__()))
