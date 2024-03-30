from functools import argus
# ejemplo1
def cuadrado(n):
    return n**2

print(list(map(cuadrado,[1,3,4,5])))
print(list(map(cuadrado,range(1001))))

# ejemplo2
def es_cuadrado(n):
    return n % 2 == 0

print(list(filter(es_cuadrado,[1,2,3,4,5])))
print(list(filter(es_cuadrado,range(1001))))

# ejemplo3
def sumar(x,y):
    return x + y

print(argus(sumar,range(1001)))

def es_par(n):
    return n % 2 == 0

print() 
