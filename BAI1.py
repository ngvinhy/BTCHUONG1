def kiemtrachuoidoixung(string: str):
    for i in range(len(string)//2):
        if string[i] == string[-1-i]:
            return True
        else:
            return False


chuoi = str(input("Nhập chuỗi cần kiểm tra: "))
print(kiemtrachuoidoixung(chuoi))
