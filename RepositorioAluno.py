import mysql.connector

db_connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='', database='sistemabd')
cursor = db_connection.cursor()

class RepositorioAluno:
    def __init__(self):
        pass

    @staticmethod
    def salvar(aluno):
        sql = "INSERT INTO aluno (login, senha, nome, idade, email,contato) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (aluno.login, aluno.senha, aluno.nome, aluno.idade, aluno.email, aluno.contato)
        cursor.execute(sql, values)

    @staticmethod
    def excluir(id):
        sql = "DELETE FROM aluno WHERE id = {}" .format(id)
        cursor.execute(sql)

    @staticmethod
    def modificarPerfil(id, campo, novo):
        sql = "UPDATE aluno SET {} = '{}' WHERE id = {}" .format(campo, novo, id)
        cursor.execute(sql)

    @staticmethod
    def procurarAlunoLogin(login, senha):
        sql = "SELECT * FROM aluno WHERE login = '{}' AND senha = '{}' ".format(login, senha)
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def listarAlunos():
        sql = "SELECT * FROM aluno"
        cursor.execute(sql)
        return cursor


# cursor.close()
# db_connection.commit()
# db_connection.close()
