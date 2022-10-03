



import view as vi
import check
def resut():
    vi.book()
    num_b = vi.number_book()
    
    if num_b == '1':
        vi.menu()
        num_m = vi.number_menu()
        return check.chek_1(num_m)
    elif num_b == '2':
        vi.menu()
        num_m = vi.number_menu()
        return check.chek_2(num_m)


    


