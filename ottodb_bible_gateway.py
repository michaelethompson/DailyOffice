import requests
from bs4 import BeautifulSoup
import csv
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

def csv_to_dict(filename):
    result_list=[]
    with open(filename, mode='r', encoding='utf-8-sig') as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            result_list.append(dict(row))
    return result_list

#part1='<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Bible Passage Test</title>\n  <meta name="description" content="Daily Office Generator">\n  <meta name="author" content="MET">\n\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">\n  <style>\n   body {\n     font-family: "EB Garamond";\n    font-size: 22px;\n   }\n  </style>\n\n</head>\n\n<body>\n'

#part4='\n</body>\n</html>\n'


conn=create_connection('ottest2.db')
cursor=conn.cursor()

biblist=csv_to_dict('testlist.csv')

line_count = 0
for row in biblist:
    if line_count == 0:
        rownames = {",".join(row)}
        print(rownames)
        line_count += 1
    theurl = 'https://www.biblegateway.com/passage/?search=' + row["OTFormatted"] + '&version=CEV'
    print(theurl)
    page = requests.get(theurl)
    html = BeautifulSoup(page.content, 'html.parser')
    li = html.find(class_="passage-text")
    thepassage=str(li).replace('publisher-info-bottom with-single','publisher-info-bottom-with-single')
#    message = str(li)
    message_bytes = thepassage.encode('UTF-8')
    base64_bytes = base64.b64encode(message_bytes)
    #base64_passage = base64_bytes.decode('UTF-8')
    row['OTPassage'] = base64_bytes.decode('UTF-8')
    #print(base64_message)
    #print(base64.b64decode(base64_message.encode('UTF-8')).decode('UTF-8'))
    #####################################
    keys = ','.join(row.keys())
    rowitems = tuple(row.values())
    #print(keys)
    #print(rowitems)
    thesql=' INSERT INTO otsample(' + str(keys) +') VALUES '+ str(rowitems)
    print(thesql)
    cursor.execute(thesql)
    line_count += 1

print(f'Processed {line_count} lines.')

conn.commit()
conn.close()

