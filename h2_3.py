def sonHarf(isim):
    return isim[-1]

liste = ["mustafa", "hakan", "ilayda", "oya", "burak"]

liste.sort(key = sonHarf)
print liste
