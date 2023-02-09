def NegativeNumberInStrings(string: str):
    kq = []
    i = 0
    while i + 1 < len(string):
        if string[i] == '-' and string[i+1].isnumeric():
            k = ''
            j = i + 1
            while j < len(string) and string[j].isnumeric():
                k += string[j]
                j += 1
            else:
                kq.extend([-int(k)])
            i = j
        else:
            i += 1
    return kq


chuoi = str(input("Nhập chuỗi cần kiểm tra: "))
if not NegativeNumberInStrings(chuoi):
    print("Không tìm thấy số nguyên âm trong chuỗi")
else:
    print(NegativeNumberInStrings(chuoi))
