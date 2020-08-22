import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import sqlite3
from sqlite3 import Error

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



part1='<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Bible Passage Test</title>\n  <meta name="description" content="Daily Office Generator">\n  <meta name="author" content="MET">\n\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Cardo">\n  <style>\n   body {\n     font-family: "Cardo";\n    font-size: 22px;\n   }\n  </style>\n\n</head>\n\n<body>\n'

part4='\n</body>\n</html>\n'


#print(thehtml)
#text_file = open("bibtest2.html", "w")
#n = text_file.write(thehtml)
#text_file.close()

#print(part3.replace('\n','\\n'))
conn=create_connection('otsmall.db')
cursor=conn.cursor()
s1='easter'
w1='4'
dbday='2'

thesql='select * from otsample where s1 = \'' +s1+ '\' and w1 =\'' +w1+ '\' and dbday = \'' +dbday+ '\';'
print(thesql)
rows=cursor.execute(thesql)
for row in rows:
    part2='<h2 class="passageref">' + str(row[8]).replace('+',' ') + '</h2>'
    part3=str(row[13]).replace('\\n', '\n')
    #print(row[8])
    #print(row[13])
conn.close()
thehtml = part1 + '\n' + part2 + '\n' + part3 + '\n' + part4
print(thehtml)
text_file = open("bibtest4.html", "w")
n = text_file.write(thehtml)
text_file.close()
