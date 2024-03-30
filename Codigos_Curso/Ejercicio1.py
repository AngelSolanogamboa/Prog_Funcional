def num1():
    return int(input("ingrese el primer numero: "))
def num2():
    return int(input("ingrese el segundo numero: "))

def myLista(num1,num2,lista):
    lista.append(num1)
    return myLista(num1+1,num2,lista) if (num1<= num2) else lista[:]
    
def par(myLista,listaPar,listaInpar,i):
    return par(myLista,listaPar.append(myLista[i]),listaInpar.append(myLista[i+1]),i+2) if (myLista[i] % 2 == 0 & i <= len(myLista)) else inpar(myLista,listaPar,listaInpar,i)

def inpar(myLista,listaPar,listaInpar,i):
    return inpar(myLista,listaPar.append(myLista[i+1]),listaInpar.append(myLista[i]),i+2) if (i <= len(myLista)) else imprimir(listaPar,listaInpar)
 
def imprimirPares(lista1,lista2,i):
    print(lista1[i])
    return imprimirPares(lista1,i+1) if (i < len(lista1)) else print("inpares: ");imprimirPares(lista2,0) 
                                         
def imprimirInpares(lista2,i):
    print(lista2[i])
    return imprimirInpares(lista2,i+1) if (i < len(lista2)) else print() 
                                         
def imprimir(listaP,listaI):
    print("Pares: ")
    imprimirPares(listaP,listaI,0)

        
     
par(myLista(num1(),num2(),[]),[],[],0)