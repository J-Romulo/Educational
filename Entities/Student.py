class Student:

    def __init__(self, login, password, name, age, email, contact):
        self.__name = name
        self.__age = age
        self.__contact = contact
        self.__login = login
        self.__password = password
        self.__email = email


    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def contact(self):
        return self.__contact


    @login.setter
    def login(self, login):
        self.__login = login

    @password.setter
    def password(self, password):
        self.__password = password

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @email.setter
    def email(self, email):
        self.__email = email

    @contact.setter
    def contact(self, contact):
        self.__contact = contact
