def taptin(string):
    kq = []
    if string.count(':') == 1 and string[1] == ':' and string[2] == chr(92):
        k = string.rfind('.')
        m = string.rfind(chr(92))
        if k != -1 and m != -1 and string[m-1].isalnum():
            kq += ["Tên tập tin:"] + [string[(m+1):k]] + ["\nPhần mở rộng:"] + [string[k+1:]]
        return ' '.join(kq)
    else:
        return False


duongdan = str(input("Nhập đường dẫn tập tin: "))
if not taptin(duongdan):
    print("Đường dẫn tập tin không hợp lệ")
else:
    print(taptin(duongdan))
