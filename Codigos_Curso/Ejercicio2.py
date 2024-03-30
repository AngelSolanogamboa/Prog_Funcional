def numero():
    return int(input("ingrese un numero: "))
    
def divisores(numero,lista,i):
    return divisores(numero-1,lista.append(numero-1),i+1) if (i < numero) else lista

def divisores    
print (divisores(numero(),[],0))