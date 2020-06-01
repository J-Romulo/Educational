class Course:

    def __init__(self, name, duration, area):
        self.__name = name
        self.__duration = duration
        self.__area = area


    @property
    def name(self):
        return self.__name

    @property
    def duration(self):
        return self.__duration

    @property
    def area(self):
        return self.__area


    @name.setter
    def name(self, name):
        self.__name = name

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @area.setter
    def area(self, area):
        self.__area = area
