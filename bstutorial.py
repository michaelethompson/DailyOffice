import requests
from bs4 import BeautifulSoup
import html2markdown
import csv

def csv_to_dict(filename):
    result_list=[]
    with open(filename, mode='r', encoding='utf-8-sig') as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            result_list.append(dict(row))
    return result_list

part1='<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Bible Passage Test</title>\n  <meta name="description" content="Daily Office Generator">\n  <meta name="author" content="MET">\n\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">\n  <style>\n   body {\n     font-family: "EB Garamond";\n    font-size: 22px;\n   }\n  </style>\n\n</head>\n\n<body>\n'

part4='\n</body>\n</html>\n'
page = requests.get("http://bible.oremus.org/?version=NRSV&vnum=no&fnote=NO&show_ref=YES&headings=NO&passage=Mark+1:1-12")

soup = BeautifulSoup(page.content, 'html.parser')

passage=soup.find('h2', class_='passageref')
part2=str(passage.decode())
bibtext=soup.find('div', class_='bibletext')

part3=str(bibtext.decode())
#part3=part3.replace('\n','\\n')
#print(html2markdown.convert(bibtext.decode()))
thehtml=part1+'\n'+part2+'\n'+part3+'\n'+part4

#print(thehtml)
#text_file = open("bibtest2.html", "w")
#n = text_file.write(thehtml)
#text_file.close()

#print(part3.replace('\n','\\n'))

biblist=csv_to_dict('testlist.csv')
line_count = 0
for row in biblist:
    if line_count == 0:
        rownames = {",".join(row)}
        print(rownames)
        line_count += 1
    # print(row)
    theurl = "http://bible.oremus.org/?version=NRSV&vnum=no&fnote=NO&show_ref=YES&headings=NO&passage=" + row["OTFormatted"]
    print(theurl)
    page = requests.get(theurl)

    soup = BeautifulSoup(page.content, 'html.parser')

    passage = soup.find('h2', class_='passageref')
    part2 = str(passage.decode())
    bibtext = soup.find('div', class_='bibletext')

    part3 = str(bibtext.decode())
    thehtml = part1 + '\n' + part2 + '\n' + part3 + '\n' + part4
    row['OTPassage'] = part3.replace('\n','\\n')
    line_count += 1

print(f'Processed {line_count} lines.')

csv_columns=['s1','w1','dbday','Season','Day','Psalm MP','Psalm EP','OT','OTFormatted','Epistle','Epistle_Formatted','Gospel','Gospel_Formatted','OTPassage']
with open('testlistwithpassage.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=csv_columns)
    w.writeheader()
    w.writerows(biblist)

