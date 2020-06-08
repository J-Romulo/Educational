import tkinter

class InfoCourseScreen:
    def __init__(self, student, course, fcdCourse, master=None):
        self.mainWidget = tkinter.Frame(master)
        self.mainWidget.pack()

        self.labelCourseName = tkinter.Label(self.mainWidget, text="{}".format(course.name))
        self.labelCourseName.pack()



        self.infoWidget = tkinter.Frame(self.mainWidget)
        self.infoWidget.pack()

        self.labelCourseArea = tkinter.Label(self.infoWidget, text="Área: {}".format(course.area), width = 200, anchor=tkinter.W)
        self.labelCourseArea.pack()

        self.labelCourseDuration = tkinter.Label(self.infoWidget, text="Duração: {} meses".format(course.duration), width = 200, anchor=tkinter.W)
        self.labelCourseDuration.pack()


        self.rollmentButton = tkinter.Button(self.mainWidget, text="Matricular-se")
        self.rollmentButton["commando"] = fcdCourse.setNewGradeSheet(course.name, student)
        self.rollmentButton.pack(side=tkinter.BOTTOM)



