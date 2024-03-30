def entrada():
    return input("Ingrese un numero: ")

def es_numero(entradas,lista):
    try:
        float(entradas)
        lista.append(float(entradas))
        return es_numero(entrada(),lista)
    except ValueError: 
        return max_minLista(lista) if (entradas == 'hecho') else es_numero(entrada(),lista)

def  max_minLista(lista):
    print("Maximo" + str(max(lista)))
    print("Minimo" + str(min(lista)))

es_numero(entrada(),[])