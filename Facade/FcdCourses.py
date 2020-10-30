from CourseFunctions import *
from GradeSheetFunctions import *

class FcdCourses:
    def __init__(self):
        pass

    @staticmethod
    def getCourse(courseName):
        return CourseFunctions.getCourseData(courseName)

    @staticmethod
    def takeListOfAllCoursesAndSendToGui(widget):
        list = CourseFunctions.takeListOfAllCourses()
        for i in range(len(list)):
            widget.insert(i+1, list[i][0])

    @staticmethod
    def getGradeSheet(courseName, studentLogin):
        return GradeSheetFunctions.getGradeSheet(courseName, studentLogin)


    @staticmethod
    def takeListOfAllGradeSheetsAndSendToGui(widget, student):
        list = GradeSheetFunctions.takeListOfAllGradeSheets(student)
        for i in range(len(list)):
            widget.insert(i + 1, list[i][2])


    @staticmethod
    def setNewGradeSheet(courseName, student):
        return GradeSheetFunctions.setNewGradeSheet(courseName, student)

    @staticmethod
    def cancelGradeSheet(courseName, studentLogin):
        return GradeSheetFunctions.cancelGradeSheet(courseName, studentLogin)








