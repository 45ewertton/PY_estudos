"""for int in range(0, 11, 2): #Contando de 0 a 10 apenas os números pares
    print(int)

print('--------------------------------') #Contando de 10 a 0 apenas os números pares

for i in range(10, -1, -2):
    print(i)"""

# Verificando lista par ou impar
lista = []
lista_par = []
lista_impar = []

for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

for ip in lista:
    if ip % 2 == 0:
        lista_par.append(ip)
    else:
        lista_impar.append(ip)

print("Verificador e ordenador de números (pares e impares)")
print("Os números pares são: ", lista_par)
print("Os números ímpares são: ", lista_impar)
print(lista)
lista_par.sort()
lista_impar.sort()
print("------------------")
print("Os números pares na ordem crescente são: ", lista_par)
print("Os números ímpares na ordem crescente são: ", lista_impar)
lista_par.reverse()
lista_impar.reverse()
print("------------------")
print("Os números pares na ordem decrescente são: ", lista_par)
print("Os números ímpares na ordem decrescente são: ", lista_impar)
