def chuanhoachuoi(string: str):
    c = string.split()
    return ' '.join(c)


chuoi = str(input("Nhập chuỗi cần kiểm tra: "))
print(chuanhoachuoi(chuoi))
