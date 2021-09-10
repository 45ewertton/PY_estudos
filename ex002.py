# Média com condição para aprovação
n1 = float(input("primeira Nota parcial: "))
n2 = float(input("segunda Nota parcial: "))

media = (n1 + n2) / 2

if media < 0 or media > 10:
    print("Informe valores entre 0 e 10!")
elif media == 10:
    print("Aprovado com destinção, média:", media)
elif media >= 7:
    print("Aprovado com média:", media)
else:
    print("Reprovado com média:", media)