def w1():
    import random
    resp = input().upper()

    while resp == "S":
        print(random.randint(0,100))
        resp = input("Mais um ? (S/N): ").upper()

def w2():
    contaAluno = 0
    while contaAluno < 3:
        nota1 = int(input("N1 ->"))
        nota2 = int(input("N2 ->"))
        media = (nota1 + nota2) / 2
        print(media)
        contaAluno += 1

def w3():
    acesso = False

    while acesso == False:
        senha = int(input("Senha -> "))

        if senha == 2002:
            print("Acesso Liberado")
            acesso = True
        else:
            print("Acesso Negado")

def wD():

    num = 5
    divisor = num
    cont = 0

    while divisor != 0:
        if num % divisor == 0:
            cont += 1
        divisor -= 1

    if cont == 2:
        print("É primo")
    else:
        print("Não é primo")

wD()