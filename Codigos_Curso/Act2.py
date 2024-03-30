#funciones puras
def suma(b1,b2):
    return b1 + b2

print(suma(2,2))
print(suma(2,2))
print(suma(2,2))

print()
#funciones no puras
total = 0
def suma2(b1,b2):
    global total

    total = total + b1 + b2

    return total

print(suma2(2,2))
print(suma2(2,2))
print(suma2(2,2))

#composicion de funciones 

def alCuadrado(numero):
    return numero * numero 

def sumaDeCuadrados(num1,num2):
    return alCuadrado(num1) + alCuadrado(num2)

def cuadradoAntecesorMasSucesor(numero):
    return  sumaDeCuadrados(numero+1,numero-1)

print(cuadradoAntecesorMasSucesor(5))

#funciones recursivas 
def duplicarLista(lista):
    if (len(lista) == 1):
        return [lista[0]*2]
    else:
        return [lista[0]*2] + duplicarLista(lista[1:])

mi_Lista = [1,2,3,4]
print(duplicarLista(mi_Lista))

# funciones de alto orden 
def mapearLista(lista, accion):
    if (len(lista) == 1):
        return [accion(lista[0])]
    else:
        return [accion(lista[0])] + mapearLista(lista[1:],accion)

My_Lista = [1,2,3,4]
print(mapearLista(My_Lista, lambda numero: numero*2))

