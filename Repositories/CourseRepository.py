import mysql.connector
from Exceptions.DuplicatePrimaryError import DuplicatePrimaryError

db_connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='', database='sistemabd')
cursor = db_connection.cursor()

class CourseRepository():
    def __init__(self):
        pass

    @staticmethod
    def save(course):
        sql = "INSERT INTO curso (nome, duracao, area) VALUES (%s, %s, %s)"
        values = (course.name, course.duration, course.area)

        try:
            cursor.execute(sql, values)
        except mysql.connector.errors.IntegrityError:
            raise DuplicatePrimaryError()

    @staticmethod
    def delete(name):
        sql = "DELETE FROM curso WHERE nome = {}" .format(name)
        cursor.execute(sql)

    @staticmethod
    def update(name, field, newInfo):
        sql = "UPDATE curso SET {} = '{}' WHERE nome = {}" .format(field, newInfo, name)
        cursor.execute(sql)

    @staticmethod
    def searchCourse(name):
        sql = "SELECT * FROM curso WHERE nome = '{}'".format(name)
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def listCourses():
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        return cursor.fetchall()