nota1 = 7
nota2 = 7
nota = 2

if nota1 == 7 or nota2 == 7:
    print("Aprovado")
else:
    print("Reprovado")

if nota1 == 5 and nota2 == 8:
    print("Aprovado")
else:
    print("Reprovado")

#Se nota <= 3 -> reprovado; nota <= 6 -> recuperação; nota > 6 -> aprovado

if nota <= 3:
    print("reprovado")
elif nota <= 6 :
    print("recuperação")
elif nota > 6:
    print("aprovado")
