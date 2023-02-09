def email(string):
    kq = []
    domain = ['gmail.com', 'uel.edu.vn', 'st.uel.edu.vn']
    if string.count('@') == 1:
        string_list = string.split('@')
        if string_list[1] in domain:
            kq += ["Username:"] + [string_list[0]] + ["\nDomain_name:"] + [string_list[1]]
            return ' '.join(kq)
    else:
        return False


diachi = str(input("Nhập địa chỉ email: "))
if not email(diachi):
    print("Địa chỉ email không hợp lệ")
else:
    print(email(diachi))
