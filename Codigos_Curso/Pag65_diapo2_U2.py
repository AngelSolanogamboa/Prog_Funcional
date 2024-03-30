contadores={'chuk':1,'annie':42,'jan': 100}
lista=list(contadores.keys())
print(lista)
lista.sort()
for clave in lista:
    print(clave, contadores[clave])

# contadores={'chuk':1,'annie':42,'jan': 100}
# lista=list(contadores.values())
# print(lista)
# lista.sort()
# for clave in lista:
#     print(clave, contadores[clave])

print()
def  ordena(contadores):
    return list(map(lambda x:(x, contadores[x]), sorted(contadores.keys())))

def imprime(diccionario):
    list(map(lambda x: print(x[0],x[1]), ordena(diccionario)))
imprime({'chuk':1,'annie':42,'jan': 100})

#funcion lower - convierte aminusculas,
#otras funciones puntruction y traslate

