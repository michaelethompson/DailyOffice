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


biblist=csv_to_dict('testlistwithpassage.csv')

print(list(biblist))
line_count = 0
for row in biblist:
    if line_count == 0:
        rownames = {",".join(row)}
        print(rownames)
        line_count += 1
    # print(row)
    part2 = row["OTFormatted"].replace('+',' ')

    part3 = row["OTPassage"]
    thehtml = part1 + '\n' + part2 + '\n' + part3 + '\n' + part4

    line_count += 1

print(f'Processed {line_count} lines.')


#print(thehtml)
text_file = open("bibtest3.html", "w")
n = text_file.write(thehtml)
text_file.close()
