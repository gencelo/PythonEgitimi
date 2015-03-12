# -*- coding: cp1254 -*-

a = 3
b = 5
if a < b:
    print "a, b den küçüktür"


def giris():
    for deneme_hakki in range(3):
        girilen_sifre = raw_input("Şifreyi gir: ")
        if girilen_sifre == "123asd":
            print "Şifre doğru"
            return 1
            break
        else:
            print "Şifre yanlış"
    return 0
    
print giris()
