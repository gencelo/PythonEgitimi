# -*- coding: cp1254 -*-


def P(x):
    return x**3 + 5*x**2 + 10*x + 7

# Uzun hali:
liste = []
for i in range(100):
    liste.append(P(i))
print liste

# Kısa hali:
liste2 = [P(i) for i in range(100)]
print liste2
