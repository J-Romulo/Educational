import tkinter

class InfoGradeSheetScreen:
    def __init__(self, gradeSheet, master=None):
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.labelCourseName = tkinter.Label(self.mainWidget, text="{}".format(gradeSheet.course_name))
        self.labelCourseName.pack()



        self.infoWidget = tkinter.Frame(self.mainWidget)
        self.infoWidget.pack()

        self.grade1Label = tkinter.Label(self.infoWidget, text="1ª Avaliação: {}".format(gradeSheet.grade1), width = 200, anchor=tkinter.W)
        self.grade1Label.pack()

        self.grade2Label = tkinter.Label(self.infoWidget, text="2ª Avaliação: {}".format(gradeSheet.grade2), width=200, anchor=tkinter.W)
        self.grade2Label.pack()

        self.grade3Label = tkinter.Label(self.infoWidget, text="3ª Avaliação: {}".format(gradeSheet.grade3), width=200, anchor=tkinter.W)
        self.grade3Label.pack()

        self.averageLabel = tkinter.Label(self.infoWidget, text="Média: {}".format(gradeSheet.averageGrade), width=200, anchor=tkinter.W)
        self.averageLabel.pack()

        self.absenceLabel = tkinter.Label(self.infoWidget, text="Faltas: {}".format(gradeSheet.absence), width=200, anchor=tkinter.W)
        self.absenceLabel.pack()