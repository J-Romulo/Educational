import mysql.connector

db_connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='', database='sistemabd')
cursor = db_connection.cursor()

class StudentRepository:
    def __init__(self):
        pass

    @staticmethod
    def save(student):
        sql = "INSERT INTO aluno (login, senha, nome, idade, email,contato) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (student.login, student.password, student.name, student.age, student.email, student.contact)
        cursor.execute(sql, values)

    @staticmethod
    def delete(id):
        sql = "DELETE FROM aluno WHERE id = {}" .format(id)
        cursor.execute(sql)

    @staticmethod
    def editProfile(id, field, newInfo):
        sql = "UPDATE aluno SET {} = '{}' WHERE id = {}" .format(field, newInfo, id)
        cursor.execute(sql)

    @staticmethod
    def searchStudentLogin(login, password):
        sql = "SELECT * FROM aluno WHERE login = '{}' AND senha = '{}' ".format(login, password)
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def listStudents():
        sql = "SELECT * FROM aluno"
        cursor.execute(sql)
        return cursor


# cursor.close()
# db_connection.commit()
# db_connection.close()
