def par_impar(num1,num2):
    return list(map(lambda x: f"{x} es par" if x % 2==0 else f"{x} es impar",range(num1,num2+1)))
    
def numeros():
    return int(input("ingrese un numero: "))
    
print("\n".join(par_impar(numeros(),numeros())))