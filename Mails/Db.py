from os import environ
import mysql.connector

class Db(object):

    def __init__(self):
        self.conn = ""

    def oppenConection(self):
        print("Iniciando conexion")
        
        try:
            self.con = mysql.connector.connect(
                user=environ['USERDB'],
                password=environ['PASSWORD'],
                host=environ['HOST'],
                port=environ['PORT'],
                database=environ['DATABASE_NAME']
            )
        except Exception, e:
            raise e
        print("Conexion exitosa")
    
    def closeConection(self):
        try:
            self.con.close()
            print("Se ha cerrado la conexion")
        except Exception, e:
            print(e)

    def executeQuery(self,query):
        cursor = self.con.cursor()
        cursor.execute(query)
        return cursor
    
    def executeInsert(self, query,data):
        cursor = self.con.cursor()
        cursor.execute(query,data)
        self.con.commit()
        return cursor