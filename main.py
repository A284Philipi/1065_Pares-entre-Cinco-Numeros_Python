cont = 0
pares = 0
while cont < 5:
    numero = int(input())
    if  (numero%2 == 0):
        pares = pares + 1
    cont = cont + 1
print("{} valores pares".format(pares))