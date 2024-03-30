def numero():
    return int(input("ingrese un numero: "))

def es_divisor(numero, divisor):
    return numero % divisor == 0

def divisores(numero):
    return filter(lambda divisor: es_divisor(numero, divisor), range(1, numero + 1))

def main(numero):
    print("Los divisores de", numero, "son:")
    list(map(print, divisores(numero)))

main(numero())