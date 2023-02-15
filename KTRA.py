def ktrakytu(string: str):
    s = list(string)
    while " " in s:
        s.remove(" ")
    kq = []
    solan = []
    maxsolan = 0
    for i in range(len(s)):
        solan.extend([s.count(s[i])])
        maxsolan = max(solan)
    for i in range(len(s)):
        if s.count(s[i]) == maxsolan and s[i] not in kq:
            kq.extend([s[i]])
    return f"{kq} xuất hiện {maxsolan} lần"


chuoi = "khoa he thong thong tin o"
print(ktrakytu(chuoi))
