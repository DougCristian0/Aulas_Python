lista = ["Local", 1232, True]

#           0         1         2
nomes = ["Fabio", "Danilo", "Valter", "Joao"]
numeros = [231, 1242, 4324, 321]

def remove():
    nomes.remove("Valter")
    print(nomes)

def Enumerate():
    for e, nome in enumerate(nomes):
        print(e, nomes)
    print(enumerate(nomes))

def ordena():
    nomes.sort()
    nomes.reverse()
    print(nomes)

    numeros.sort()
    print(numeros)

def trocaNome():
    if "Taciano" in nomes:
        nomes[nomes.index("Taciano")] = "Pedro"
        print(nomes)
    else:
        print("Não tem Taciano")

def insere():
    nomes.insert(1, "Danilo")
    cont = 0
    for nome in nomes:
        if nome == "Taciano":
            nomes[cont] = "Pedro"
        cont+=1

def insereNoFinal():
    nomes.append("Marcos")
    nomes.append("Maria")

def contaQuantosNaLista():
    if "Douglas" in nomes:
        print(nomes.count("Douglas"))