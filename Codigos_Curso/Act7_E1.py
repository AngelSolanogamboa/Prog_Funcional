def cortar(lista):
    return lista[1:-1]
    
def recortar(lista):
    cortar(lista)
    return lista.clear()

def medio(lista):
    return lista[1:-1]
    
print(recortar(["a","b","c","d"]))
print(medio(["a","b","c","d"]))