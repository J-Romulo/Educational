import tkinter
from tkinter import messagebox

class InfoCourseScreen:
    def __init__(self, student, course, fcdCourse, master=None):
        self.fcdCourse = fcdCourse
        self.student = student
        self.course = course
        self.master = master
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.labelCourseName = tkinter.Label(self.mainWidget, text="{}".format(course.name))
        self.labelCourseName.pack()



        self.infoWidget = tkinter.Frame(self.mainWidget)
        self.infoWidget.pack()

        self.labelCourseArea = tkinter.Label(self.infoWidget, text="Área: {}".format(course.area), width = 200, anchor=tkinter.W)
        self.labelCourseArea.pack()

        self.labelCourseDuration = tkinter.Label(self.infoWidget, text="Duração: {} horas".format(course.duration), width = 200, anchor=tkinter.W)
        self.labelCourseDuration.pack()


        self.rollmentButton = tkinter.Button(self.mainWidget, text="Matricular-se")
        self.rollmentButton["command"] = self.setRollment
        self.rollmentButton.pack(side=tkinter.BOTTOM, pady=(5,0))


    def setRollment(self):
        answer = messagebox.askyesno("Confirmar procedimento",
                                     "Você tem certeza que quer se matricular no curso de {}?".format(self.course.name))

        if answer:
            expectedBehavior = self.fcdCourse.setNewGradeSheet(self.course.name, self.student)
            if expectedBehavior:
                messagebox.showinfo("Procedimento concluido",
                                    "Matrícula registrada com sucesso! Reentre no sistema para as informações em tela serem atualizadas.")
                self.master.destroy()




