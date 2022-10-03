
from tkinter import *
import logger_GUI as lo

root = Tk()

photo = PhotoImage(file='phone book\phones.png')
root.iconphoto(False,photo)
root.geometry('600x600')
root.title('Телефонная книга')
Name = StringVar()
Number = StringVar()


group_1 = LabelFrame(padx=26, pady=15,text="Данные контакта",font='arial 12 bold')
group_1.place(x=50, y=50)


Label(group_1, text = 'Имя', font='arial 12 bold').grid(row=0, stick = 'W')
entry=Entry(group_1, textvariable = Name,width=50 ).grid(row=0,column=1)

Label(group_1, text = 'Фамилия', font='arial 12 bold').grid(row=1, stick = 'W')
entry1 = Entry(group_1, textvariable = Name,width=50).grid(row=1,column=1)

Label(group_1, text = 'Номер телефона', font='arial 12 bold').grid(row=2,stick = 'W')
entry2 = Entry(group_1, textvariable = Number,width=50).grid(row=2,column=1 )

def show_G1(): 
    mybook = open('phone book\myphonebook.txt', 'r', encoding='utf-8')
    bookcontents = mybook.readlines()

    for item in bookcontents:
            selectb.insert('end',item) 
# def add_item():
#     selectb.insert(END, entry.get())
#     entry.delet(0, END)


Button(root,text="Показать",command = show_G1,  font="arial 12 bold", height= 1, width= 10).place(x= 50, y=180)
Button(root,text="Добавить", font="arial 12 bold",height= 1, width= 10).place(x= 180, y=180)
Button(root,text="Найти",font="arial 12 bold",height= 1, width= 10).place(x= 310, y=180)
Button(root,text="Удалить",font="arial 12 bold",height= 1, width= 10).place(x= 440, y=180)


my_frame = Frame(root)
my_frame.place(x=50, y=240)
selectb = Listbox(my_frame,  height=15, width= 55,font='arial 12 bold')
selectb.pack(side="left", fill="y")
scroll_bar = Scrollbar(my_frame, orient=VERTICAL)
scroll_bar.config(command=selectb.yview)
scroll_bar.pack(side="right", fill="y")
selectb.config(yscrollcommand=scroll_bar.set)






# # Execute Tkinter
root.mainloop()
