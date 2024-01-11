# упражнение №3
# даны четыре множества:
#
# a = set('0123456789')
# b = set('02468')
# c = set('12345')
# d = set('56789')
# найти элементы, принадлежащие множеству e:
# ((A\B)∩(C\D))∪((D\A)∩(B\C))

a = set('0123456789')
b = set('02468')
c = set('12345')
d = set('56789')

p1 = a.difference(b)
p2 = c.difference(d)
p3 = d.difference(a)
p4 = b.difference(c)
p5 = p1.intersection(p2)
p6 = p3.intersection(p4)
res = p5.union(p6)
print(res)
res = (a.difference(b)).intersection(c.difference(d)).union((d.difference(a)).intersection(b.difference(c)))
print(res)