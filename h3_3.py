# -*- coding: cp1254 -*-

def E(kutle, hiz):
    return 0.5*kutle*hiz**2
# Bo� bir liste:
liste = []
# 1 milyon say� i�in hesap yapt�m
for V in range(1000000):
    liste.append(E(4, V)) # y54ytf

# list comprehension
