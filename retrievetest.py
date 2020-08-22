import sqlite3
from sqlite3 import Error
import base64


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


#part1='<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Bible Passage Test</title>\n  <meta name="description" content="Daily Office Generator">\n  <meta name="author" content="MET">\n\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">\n  <style>\n   body {\n     font-family: "EB Garamond";\n    font-size: 22px;\n   }\n  </style>\n\n</head>\n\n<body>\n'

#part4='\n</body>\n</html>\n'


conn=create_connection('ottest2.db')
cur=conn.cursor()

cur.execute("select * from otsample where s1 ='easter' and w1='4' and dbday='6'")

rows = cur.fetchall()

for row in rows:
    thepassagehtml=base64.b64decode(row[13].encode('UTF-8')).decode('UTF-8')
    print(row[0],row[8].replace('+',' '))
    print(thepassagehtml)
