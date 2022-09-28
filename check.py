import logger
# import controller

def chek(num_m):

    if num_m== '1':
        return logger.show_1() 
    elif num_m== '2':
       return logger.add_2() 
    elif num_m== '3':
        return logger.search_3()
    elif num_m== '4':
        return logger.del_4()   
    else:
            print("Вы ошиблись цифрой, ведите еще раз")