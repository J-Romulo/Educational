from Entities.Course import Course
from GUI.InfoCourseScreen import InfoCourseScreen
from Repositories.GradeSheetRepository import GradeSheetRepository
from Repositories.CourseRepository import CourseRepository
from Entities.GradeSheet import *
import tkinter

class FcdCourses:
    def __init__(self):
        pass

    @staticmethod
    def getCourse(courseName):
        courseData = CourseRepository.searchCourseByName(courseName)

        course = Course(courseData[0], courseData[1], courseData[2])

        return course

    @staticmethod
    def takeListOfAllCoursesAndSendToGui(widget):
        list = CourseRepository.listAllCourses()
        for i in range(len(list)):
            widget.insert(i+1, list[i][0])

    @staticmethod
    def getGradeSheet(courseName, studentLogin):
        gradeSheetData = GradeSheetRepository.searchGradeSheet(courseName, studentLogin)

        gradeSheet = GradeSheet(gradeSheetData[6], gradeSheetData[7])
        print(gradeSheetData)
        return gradeSheet


    @staticmethod
    def takeListOfAllGradeSheetsAndSendToGui(widget, student):
        list = GradeSheetRepository.listAllStudentsGradeSheets(student)
        for i in range(len(list)):
            widget.insert(i + 1, list[i][7])


    @staticmethod
    def setNewGradeSheet(courseName, student):
        studentGradeSheet = GradeSheet(student.login, courseName)
        GradeSheetRepository.saveGradeSheetData(studentGradeSheet)



