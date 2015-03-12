Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 423**99
101787950545500423759487221347364995115944800439785614837697337973532171704787868333084267933941909093917605594322302565458158444855420872825206251012632192337206501577994510679896765211513478756337395693160059143831106605284911823528477379077672614965960050487L
>>> 4/3
1
>>> 4.0/3
1.3333333333333333
>>> 4/3.0
1.3333333333333333
>>> 4/3
1
>>> from __future__ import division
>>> 4/3
1.3333333333333333
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> import antigravity
>>> a = 432432
>>> b = 423.4325
>>> c = "güray"
>>> print c
güray
>>> a
432432
>>> a = 432.43243
>>> a
432.43243
>>> a = a + 1
>>> a
433.43243
>>> print "güray"*10
güraygüraygüraygüraygüraygüraygüraygüraygüraygüray
>>> print "g
SyntaxError: EOL while scanning string literal
r
>>> print "güray" + "yýldýrým
SyntaxError: EOL while scanning string literal
>>> print "güray" + "yýldýrým"
gürayyýldýrým
>>> isimler = ["güray", "oðuzhan", "burak", "muratcan", "oya", "ilayda"]
>>> print isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda']
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda']
>>> len(isimler)
6
>>> len("guray yildirim")
14
>>> help(len)
Help on built-in function len in module __builtin__:

len(...)
    len(object) -> integer
    
    Return the number of items of a sequence or collection.

>>> dir(isimler)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> isimler.append
<built-in method append of list object at 0x0283B418>
>>> help(isimler.append)
Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> isimler.append("mustafa")
>>> print isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa']
>>> help(isimler.count)
Help on built-in function count:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> isimler.count("mustafa")
1
>>> isimler.append("mustafa")
>>> isimler.count("mustafa")
2
>>> print isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa']
>>> sayilar = [3.14,  67556, 654, 5]
>>> print sayilar
[3.14, 67556, 654, 5]
>>> sayilar.append(7)
>>> sayilar
[3.14, 67556, 654, 5, 7]
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa']
>>> help(isimler.extend)
Help on built-in function extend:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable

>>> isimler.extend(sayilar)
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654, 5, 7]
>>> dir(isimler)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(isimler.index)
Help on built-in function index:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> isimler.index("mustafa")
6
>>> isimler.index(5)
11
>>> help(isimler.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> isimler
['g\xfcray', 'o\xf0uzhan', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654, 5, 7]
>>> isimler.insert(2, "tunç")
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'tun\xe7', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654, 5, 7]
>>> help(isimler.pop)
Help on built-in function pop:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> isimler.pop()
7
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'tun\xe7', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654, 5]
>>> isimler.pop()
5
i
>>> simler

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    simler
NameError: name 'simler' is not defined
>>> isimler
['g\xfcray', 'o\xf0uzhan', 'tun\xe7', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654]
>>> isimler.pop(0)
'g\xfcray'
>>> isimler
['o\xf0uzhan', 'tun\xe7', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 'mustafa', 3.14, 67556, 654]
>>> isimler.remove("mustafa")
>>> isimler
['o\xf0uzhan', 'tun\xe7', 'burak', 'muratcan', 'oya', 'ilayda', 'mustafa', 3.14, 67556, 654]
>>> help(isimler.remove)
Help on built-in function remove:

remove(...)
    L.remove(value) -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> dir(isimler)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> isimler.reverse()

>>> isimler
[654, 67556, 3.14, 'mustafa', 'ilayda', 'oya', 'muratcan', 'burak', 'tun\xe7', 'o\xf0uzhan']
>>> isimler.sort()
>>> isimler
[3.14, 654, 67556, 'burak', 'ilayda', 'muratcan', 'mustafa', 'oya', 'o\xf0uzhan', 'tun\xe7']
>>> help(isimler.sort)
Help on built-in function sort:

sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> isimler.sort(reverse=True)
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> isimler[1]
'o\xf0uzhan'
>>> print isimler[1]
oðuzhan
>>> isimler.index("mustafa")
3
>>> yer = isimler.index("mustafa")
>>> yer
3
>>> print isimler[3]
mustafa
>>> print isimler[yer]
mustafa
>>> isimler[-1]
3.14
>>> isimler[len(isimler)]

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    isimler[len(isimler)]
IndexError: list index out of range
>>> isimler[len(isimler)-1]
3.14
>>> isimler[-2]
654
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> print "dasffas", "dsfg"
dasffas dsfg
>>> ================================ RESTART ================================
>>> 
1. sayý: 534
2. sayý: 423
3. sayý: 56
Sýralanmamýþ liste:  [534, 423, 56]
Sýralanmýþ liste:  [56, 423, 534]
>>> a = 4
>>> a = 654
>>> a
654
>>> deger = input("bir sayi gir: ")
bir sayi gir: 656563456
>>> print deger
656563456
>>> isimler

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    isimler
NameError: name 'isimler' is not defined
>>> isimler = ['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> print isimler[0]
tunç
>>> isimler[0]
'tun\xe7'
i
>>> isimler[1]
'o\xf0uzhan'
>>> isimler[2]
'oya'
>>> isimler[0:5]
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan']
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> isimler[2:6]
['oya', 'mustafa', 'muratcan', 'ilayda']
>>> isimler[0:100]
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> isimler[-1:-4]
[]
>>> isimler[-4:-1]
['burak', 67556, 654]
>>> isimler[-4:0]
[]
>>> isimler[-4:]
['burak', 67556, 654, 3.14]
>>> isimler[-3:]
[67556, 654, 3.14]
>>> isimler[:5]
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan']
>>> isimler[:]
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> a = 3
>>> b = a
>>> b
3
>>> a
3
>>> b = 5
>>> a
3
>>> b
5
>>> kopyaliste = isimler
>>> kopyaliste
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.14]
>>> kopyaliste.pop()
3.14
7
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654]
>>> kopyaliste
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654]
>>> liste = isimler[:]
>>> liste
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654]
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654]
>>> liste.pop()
654
>>> liste
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556]
i
>>> simler

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    simler
NameError: name 'simler' is not defined
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654]
>>> a = 4
>>> b = a
>>> from math import pi
>>> isimler.append(pi)
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.141592653589793]
>>> isimler
['tun\xe7', 'o\xf0uzhan', 'oya', 'mustafa', 'muratcan', 'ilayda', 'burak', 67556, 654, 3.141592653589793]
>>> isimler[::2]
['tun\xe7', 'oya', 'muratcan', 'burak', 654]
>>> help(range)
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(11)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11,2)
[1, 3, 5, 7, 9]
>>> range(1,11,3)
[1, 4, 7, 10]
>>> range(1,101,2)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> range(1,101)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> liste = range(1, 101)
>>> liste
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> liste[::2]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> liste = range(0, 101)
>>> liste
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
KeyboardInterrupt
>>> liste[::2]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> liste = range(1, 101)
>>> liste
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> liste[::2]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> liste[1::2]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> teksayilar = liste[::2]
>>> ciftsayilar = liste[1::2]
>>> teksayilar
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> ciftsayilar
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> teksayilar+ciftsayilar
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> sonliste = teksayilar+ciftsayilar
>>> sonliste.sort()
>>> sonliste
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> a = 10
>>> print a
10
>>> del a
>>> print a

Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    print a
NameError: name 'a' is not defined
>>> sonliste
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> del sonliste
>>> sonliste

Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    sonliste
NameError: name 'sonliste' is not defined
>>> sonliste

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    sonliste
NameError: name 'sonliste' is not defined
>>> liste = range(1,101)
ü
>>> liste
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> del liste(::2)
SyntaxError: invalid syntax
>>> liste[::2]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> del liste[::2]
>>> liste
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> len(liste)
50
>>> del liste[-10:]
>>> liste
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]
>>> len(liste)
40
>>> del liste[13]
>>> liste
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]
>>> 
