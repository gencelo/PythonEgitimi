# -*- coding: cp1254 -*-

a = 3
b = 5
if a < b:
    print "a, b den k���kt�r"


def giris():
    for deneme_hakki in range(3):
        girilen_sifre = raw_input("�ifreyi gir: ")
        if girilen_sifre == "123asd":
            print "�ifre do�ru"
            return 1
            break
        else:
            print "�ifre yanl��"
    return 0
    
print giris()
