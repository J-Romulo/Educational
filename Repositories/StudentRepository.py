import mysql.connector
from Exceptions.DuplicatePrimaryKeyError import DuplicatePrimaryKeyError

db_connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='', database='sistemabd')
cursor = db_connection.cursor()

class StudentRepository():
    def __init__(self):
        pass

    @staticmethod
    def saveStudentData(student):
        sql = "INSERT INTO aluno (login, senha, nome, nascimento, email,contato) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (student.login, student.password, student.name, student.age, student.email, student.contact)

        try:
            cursor.execute(sql, values)
        except mysql.connector.errors.IntegrityError:
            raise DuplicatePrimaryKeyError()

    @staticmethod
    def deleteStudentByLogin(login):
        sql = "DELETE FROM aluno WHERE login = {}" .format(login)
        cursor.execute(sql)

    @staticmethod
    def editProfileField(login, field, newInfo):
        sql = "UPDATE aluno SET {} = '{}' WHERE login = {}" .format(field, newInfo, login)
        cursor.execute(sql)

    @staticmethod
    def searchStudentByLogin(login, password):
        sql = "SELECT * FROM aluno WHERE login = '{}' AND senha = '{}' ".format(login, password)
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def listAllStudents():
        sql = "SELECT * FROM aluno"
        cursor.execute(sql)
        return cursor.fetchall()

# cursor.close()
# db_connection.commit()
# db_connection.close()
