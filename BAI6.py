def hoten(string):
    string_list = string.split()
    ho = string_list[0]
    string_list.pop(0)
    ten = string_list[-1]
    string_list.pop(-1)
    return f"Họ: {ho}\nTên đệm: {' '.join(string_list)}\nTên: {ten}"


hovaten = str(input("Nhập họ và tên: "))
print(hoten(hovaten))
