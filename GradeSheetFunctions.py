from Entities.GradeSheet import GradeSheet
from Exceptions.DuplicateGradeSheet import DuplicateGradeSheet
from Repositories.GradeSheetRepository import *


class GradeSheetFunctions:
    def __init__(self):
        pass

    @staticmethod
    def getGradeSheet(courseName, studentLogin):
        gradeSheetData = GradeSheetRepository.searchGradeSheet(courseName, studentLogin)
        gradeSheet = GradeSheet(gradeSheetData[1], gradeSheetData[2], gradeSheetData[3], gradeSheetData[4],
                                gradeSheetData[5], gradeSheetData[6], gradeSheetData[7])

        return gradeSheet

    @staticmethod
    def setNewGradeSheet(courseName, student):
        try:
            gradeSheet = GradeSheetRepository.searchGradeSheet(courseName, student.login)
            if gradeSheet:
                raise DuplicateGradeSheet()
            else:
                studentGradeSheet = GradeSheet(student.login, courseName)
                GradeSheetRepository.saveGradeSheetData(studentGradeSheet)

                return True

        except DuplicateGradeSheet as duplicate:
            duplicate.throwGUI()

    @staticmethod
    def cancelGradeSheet(courseName, studentLogin):
        GradeSheetRepository.deleteGradeSheet(courseName, studentLogin)

        return True



    @staticmethod
    def takeListOfAllGradeSheets(student):
        gradeSheetList = GradeSheetRepository.listAllStudentsGradeSheets(student)

        return gradeSheetList
