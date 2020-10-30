from Entities.Course import Course
from Repositories.CourseRepository import *


class CourseFunctions:
    def __init__(self):
        pass

    @staticmethod
    def takeListOfAllCourses():
        return CourseRepository.listAllCourses()

    @staticmethod
    def getCourseData(courseName):
        courseData = CourseRepository.searchCourseByName(courseName)

        course = Course(courseData[0], courseData[1], courseData[2])

        return course
