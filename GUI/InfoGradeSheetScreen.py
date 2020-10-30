import tkinter
from tkinter import messagebox
from Facade.FcdCourses import *


class InfoGradeSheetScreen:
    def __init__(self, gradeSheet, master=None):
        self.master = master
        self.gradeSheet = gradeSheet
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.labelCourseName = tkinter.Label(self.mainWidget, text="{}".format(gradeSheet.course_name))
        self.labelCourseName.pack()

        self.infoWidget = tkinter.Frame(self.mainWidget)
        self.infoWidget.pack(pady=(10, 0))

        self.grade1Label = tkinter.Label(self.infoWidget, text="1ª Avaliação: {}".format(gradeSheet.grade1), width=200,
                                         anchor=tkinter.W)
        self.grade1Label.pack()

        self.grade2Label = tkinter.Label(self.infoWidget, text="2ª Avaliação: {}".format(gradeSheet.grade2), width=200,
                                         anchor=tkinter.W)
        self.grade2Label.pack()

        self.grade3Label = tkinter.Label(self.infoWidget, text="3ª Avaliação: {}".format(gradeSheet.grade3), width=200,
                                         anchor=tkinter.W)
        self.grade3Label.pack()

        self.averageLabel = tkinter.Label(self.infoWidget, text="Média: {}".format(gradeSheet.averageGrade), width=200,
                                          anchor=tkinter.W)
        self.averageLabel.pack()

        self.absenceLabel = tkinter.Label(self.infoWidget, text="Faltas: {}".format(gradeSheet.absence), width=200,
                                          anchor=tkinter.W)
        self.absenceLabel.pack()

        self.cancelButton = tkinter.Button(self.infoWidget, text="Cancelar matrícula")
        self.cancelButton["command"] = self.cancelRollment
        self.cancelButton.pack(pady=(10,0))



    def cancelRollment(self):
        answer = messagebox.askyesno("Confirmar procedimento", "Você tem certeza que quer cancelar sua matrícula?")

        if answer:
            expectedBehavior = FcdCourses.cancelGradeSheet(self.gradeSheet.course_name, self.gradeSheet.login_student)
            if expectedBehavior:
                messagebox.showinfo("Cancelamento concluido",
                                    "A sua matrícula no curso de {} foi cancelada com sucesso!".format(self.gradeSheet.course_name))
                self.master.destroy()
        else:
            self.master.destroy()
            messagebox.showinfo("Procedimento cancelado", "Procedimento de exclusão de matrícula não concluido.")

