import csv
from typing import Dict

def reader_1():
    with open("phone book\myphonebook.csv","r",encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(*row)


def writer_2():
    first = input("Введите Имя ")
    last = input("Введите Фамилию ")
    phon_num = input("Введите номер телефона ")
    f_name =['Имя','Фамилия','Телефон']
    line = {'Имя':first,'Фамилия':last,'Телефон':phon_num}

    with open("phone book\myphonebook.csv","a",encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=f_name)
        writer.writerow(line)


def look_3():
    s_name = input("Введите имя для поиска записи ")
    with open("phone book\myphonebook.csv","r+",encoding='utf8') as f:
        f_name =['Имя','Фамилия','Телефон']
        data = csv.DictReader(f,fieldnames=f_name)
        # reader = csv.reader(f)
        rez={}
        for row in data:
            if row['Имя'] == s_name:
                rez = row 
                print (*rez.values())
            else: 
                print ('Контакт не найден')
            
def removal_4():
    del_first = input("Введите имя для удаления записи ")
    del_last = input("Введите фамилию для удаления записи ")
    with open("phone book\myphonebook.csv","r",encoding='utf8') as inp: 
        reader = csv.reader(inp)
        rez=[]
        found = False
        for row in reader:
            if  del_first in row[0] and del_last in row[1]:
                print("Контакт удален")
                found = True
            else:
                rez.append(row)
                    
                    
        if found == False:
                print("Контакта нет в списке")
            
    with open("phone book\myphonebook.csv","w",encoding='utf8', newline='') as out :
        writer = csv.writer(out)
        for row in rez:
            writer.writerow(row)

    
   



