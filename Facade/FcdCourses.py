from Repositories.CourseRepository import CourseRepository

class FcdCourses:
    def __init__(self):
        pass

    @staticmethod
    def takeListOfAllCoursesAndSendToGui(widget):
        list = CourseRepository.listAllCourses()
        for i in range(len(list)):
            widget.insert(i+1, list[i][0])
