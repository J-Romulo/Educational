import Facade.FcdStudent as facade


class DuplicatePrimaryError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Login já existente.\nTente outro para completar o registro"

    def throwGUI(self):
        facade.FcdStudent.throwExceptionGUI(self.__str__())
