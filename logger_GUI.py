


def show_G1(): 
    import gui_1
    mybook = open('phone book\myphonebook.txt', 'r', encoding='utf-8')
    bookcontents = mybook.readlines()

    for item in bookcontents:
        gui_1.selectb.insert('end',item) 
