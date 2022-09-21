from os import environ
from Mails.LetterFunctions import *
from Mails.Configutation import load
from Mails import Db
import sys
import datetime
import locale


def main():

    sendMail()

def sendMail():
    con = Db.Db()
    con.oppenConection()

    #query = ("SELECT CONCAT(uu.name,',', uu.lastname) AS full_name, uu.email, DATEDIFF(NOW(), FROM_UNIXTIME(rq.last_modified)) AS datediff"
    #" FROM list_users uu INNER JOIN request AS rq ON rq.user_id = uu.id  WHERE rq.step <= 3 AND uu.phone IS NOT NULL"
    #" AND rq.last_modified >= UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 1 MONTH)) HAVING datediff > 15 AND (datediff <= 28) ORDER BY rq.last_modified")

    query = ("SELECT CONCAT(uu.first_name,',', uu.last_name) AS full_name, uu.email FROM sys_user AS uu WHERE uu.status = 1")

    cursor = con.executeQuery(query)
    rows = cursor.fetchall()

    for row in rows:
        letter(str(row[0]),str(row[1]),"letter-template","Mail sended with python 2.7") #Send email
        #name,email,template_name,subject

    con.closeConection()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    locale.setlocale( locale.LC_ALL, '')
    load() #Load basic configurations
    main() #Init process