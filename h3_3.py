# -*- coding: cp1254 -*-

def E(kutle, hiz):
    return 0.5*kutle*hiz**2
# Boş bir liste:
liste = []
# 1 milyon sayı için hesap yaptım
for V in range(1000000):
    liste.append(E(4, V)) # y54ytf

# list comprehension
