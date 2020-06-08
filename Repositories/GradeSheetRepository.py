import mysql.connector

db_connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='', database='sistemabd')
cursor = db_connection.cursor()

class GradeSheetRepository():
    def __init__(self):
        pass


    @staticmethod
    def saveGradeSheetData(gradeSheet):
        sql = "INSERT INTO perfil_curricular (id, login_aluno, nome_curso) VALUES (default, %s, %s) "
        values = (gradeSheet.login_student, gradeSheet.course_name)

        cursor.execute(sql, values)

    @staticmethod
    def listAllStudentsGradeSheets(student):
        sql = "SELECT * FROM perfil_curricular where login_aluno = '{}'".format(student.login)
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def searchGradeSheet(courseName, studentLogin):
        sql = "SELECT * FROM perfil_curricular where login_aluno = '{}' AND nome_curso = '{}'".format(studentLogin, courseName)
        cursor.execute(sql)
        return cursor.fetchone()

