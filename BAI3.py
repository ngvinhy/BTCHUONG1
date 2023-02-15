def NegativeNumberInStrings(string: str):
    kq = []
    s = string.split('-')
    while "" in s:
        s.remove("")
    for item in s:
        if item[0].isdigit():
            i = 0
            while i + 1 < len(item):
                if item[i+1].isnumeric():
                    i += 1
                else:
                    break
            if "-" + item in string:
                kq.extend([-int(item[:i+1])])
    return kq


chuoi = str(input("Nhập chuỗi cần kiểm tra: "))
if not NegativeNumberInStrings(chuoi):
    print("Không tìm thấy số nguyên âm trong chuỗi")
else:
    print(NegativeNumberInStrings(chuoi))
