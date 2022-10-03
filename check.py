import logger
import logger_csv
# import controller



def chek_1(num_m):

    if num_m == '1':
        return logger.show_1() 
    elif num_m== '2':
       return logger.add_2() 
    elif num_m== '3':
        return logger.search_3()
    elif num_m== '4':
        return logger.del_4()   
    else:
            print("Вы ошиблись цифрой, ведите еще раз")

def chek_2(num_m):
    if num_m== '1':
        return logger_csv.reader_1()
    elif num_m== '2':
        return logger_csv.writer_2()
    elif num_m== '3':
        return logger_csv.look_3()
    elif num_m== '4':
           return logger_csv.removal_4()
    else:
            print("Вы ошиблись цифрой, ведите еще раз")