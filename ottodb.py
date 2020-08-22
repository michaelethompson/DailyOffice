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

def csv_to_dict(filename):
    result_list=[]
    with open(filename, mode='r', encoding='utf-8-sig') as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            result_list.append(dict(row))
    return result_list

part1='<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Bible Passage Test</title>\n  <meta name="description" content="Daily Office Generator">\n  <meta name="author" content="MET">\n\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">\n  <style>\n   body {\n     font-family: "EB Garamond";\n    font-size: 22px;\n   }\n  </style>\n\n</head>\n\n<body>\n'

part4='\n</body>\n</html>\n'


#print(thehtml)
#text_file = open("bibtest2.html", "w")
#n = text_file.write(thehtml)
#text_file.close()

#print(part3.replace('\n','\\n'))
conn=create_connection('otsmall.db')
cursor=conn.cursor()
biblist=csv_to_dict('testlist.csv')
line_count = 0
for row in biblist:
    if line_count == 0:
        rownames = {",".join(row)}
        print(rownames)
        line_count += 1
    # print(row)


    theurl = "http://bible.oremus.org/?version=NRSV&vnum=no&fnote=NO&show_ref=YES&headings=NO&passage=" + row["OTFormatted"]
    #print(theurl)
    page = requests.get(theurl)

    soup = BeautifulSoup(page.content, 'html.parser')

    bibtext = soup.find('div', class_='bibletext')

    row['OTPassage'] =  str(bibtext.decode())
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