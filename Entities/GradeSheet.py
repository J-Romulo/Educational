class GradeSheet:
    def __init__(self, login_student, course_name, grade1 = 0, grade2 = 0, grade3 = 0, averageGrade = 0, absence = 0):
        self.__login_student = login_student
        self.__course_name = course_name
        self.__grade1 = grade1
        self.__grade2 = grade2
        self.__grade3 = grade3
        self.__averageGrade = averageGrade
        self.__absence = absence


    @property
    def login_student(self):
        return self.__login_student

    @property
    def course_name(self):
        return self.__course_name

    @property
    def grade1(self):
        return self.__grade1

    @property
    def grade2(self):
        return self.__grade2

    @property
    def grade3(self):
        return self.__grade3

    @property
    def averageGrade(self):
        return self.__averageGrade

    @property
    def absence(self):
        return self.__absence



    @login_student.setter
    def login_student(self, login_student):
        self.__login_student = login_student

    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    @grade1.setter
    def grade1(self, grade1):
        self.__grade1 = grade1

    @grade2.setter
    def grade2(self, grade2):
        self.__grade2 = grade2

    @grade3.setter
    def grade3(self, grade3):
        self.__grade3 = grade3

    @averageGrade.setter
    def averageGrade(self, averageGrade):
        self.__averageGrade = averageGrade

    @absence.setter
    def absence(self, absence):
        self.__absence = absence

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.login_student,
                                                   self.course_name,
                                                   self.grade1,
                                                   self.grade2,
                                                   self.grade3,
                                                   self.averageGrade,
                                                   self.absence)