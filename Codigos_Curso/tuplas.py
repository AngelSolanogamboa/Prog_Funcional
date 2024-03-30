t1='a',
print(type(t1))


t=tuple('altramuces')
print(t)

t2=('a','b','c','d','e')
print(t2)

t3=('a','b','c','d','e')
t3= ('A',) + t3[1:0]
print(t3)

m=('pasalo','bien')
x,y =m
print(x)
print(y)

m=['pasalo','bien']
(x,y)=m
print(x)
print(y)


d={'a':10,'b':1,'c':22}
t=list(d.items())
print(t)
t.sort()
print(t)