# -*- coding: cp1254 -*-

liste = []

for sayi in range(150):
    liste.append(sayi)
print liste


kareler_listesi = []

for sayi in range(150):
    kareler_listesi.append(sayi**2)

print kareler_listesi


alt_sinir = input("Başlangıç: ")
ust_sinir = input("Bitiş: ")

kullanici_listesi = []
for sayi in range(alt_sinir,ust_sinir+1):
    kullanici_listesi.append(sayi**2)
