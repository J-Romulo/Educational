import Facade.FcdStudent as facade

class NotFindError(IndexError):
    def __init__(self):
        pass

    def __str__(self):
        return "Nome de usuário e/ou senha incorretos\nNenhum usuário encontrado"

    def throwGUI(self):
        facade.FcdStudent.throwExceptionGUI(self.__str__())
