def daonguocchuoi(string):
    string_list = string.split()
    string_list.reverse()
    kq = ' '.join(string_list)
    return kq


chuoi = str(input("Nhập chuỗi cần đảo ngược: "))
print("Chuỗi đảo ngược:", daonguocchuoi(chuoi))
