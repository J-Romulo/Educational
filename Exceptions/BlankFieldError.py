import Facade.FcdStudent as facade


class BlankFieldError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Preencha todos os campos para continuar"

    def throwGUI(self):
        facade.FcdStudent.throwExceptionGUI(self.__str__())
