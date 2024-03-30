#ordenar lista conforme a los 
def ordena(lista):
    lista.sort(key=lambda x:x[1], reverse=False)
    print(lista)
ordena(list({'a':10,'b':2,'c':20}.items()))