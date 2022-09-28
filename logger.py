
import view 


def show_1():   #Чтение телефонного справочника
    mybook = open('myphonebook.txt', 'r', encoding='utf-8')
    bookcontents = mybook.read()
    print(bookcontents)
    mybook.close

def add_2():
    first = input("Введите Имя ")
    last = input("Введите Фамилию ")
    phon_num = input("Введите номер телефона ")
   
    cont_add =(first + " " + last + " " + phon_num )
    mybook = open('myphonebook.txt','a', encoding='utf-8')
    mybook.write(cont_add + "\n")
    print(f"Контактные данные:\n{cont_add}\nдобавлены в телефонную книгу")

def search_3():
    s_name = input("Введите имя для поиска записи ")
    mybook = open('myphonebook.txt','r+', encoding='utf-8')
    bookcontents = mybook.readlines()
    found = False
    for line in bookcontents:
        if s_name in line:
            print("Контактная информация:", end ="")
            print(line)
            found = True
            break
    if found == False:
        print("Контакта нет в телефонной книге")

def del_4():
    del_first = input("Введите имя для удаления записи ")
    del_last = input("Введите фамилию для удаления записи ")
    del_name = (del_first + " " + del_last)
    mybook = open('myphonebook.txt','r', encoding='utf-8')
    bookcontents = mybook.readlines()
    mybook = open('myphonebook.txt','w', encoding='utf-8')
    found = False
    for line in bookcontents:
        if del_name  in line:
            print("Контактная информация стерта")
            found = True
            
        else: 
            mybook.write(line)
    if  found == False:
        print("Контакта нет в списке")



