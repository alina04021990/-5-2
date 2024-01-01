c = input("Введите слово")
b = c.split()
a=b.count ("a")
e=b.count ("e")
i=b.count ("i")
o=b.count ("o")
u=b.count ("u")
if a == 0:
    print('a=false')
else:
    print(a)
if e == 0:
    print('e=false')
else:
    print(e)
if i == 0:
    print('i=false')
else:
    print(i)
if o == 0:
    print('o=false')
else:
    print(o)
if u == 0:
    print('u=false')
else:
    print(u)
print("Гласных: ", a + e + i + o + u) 
print("Согласных:", len(b) - (a + e + i + o + u))


