#pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cadastros"
)

cursor = conexao.cursor()

r = 0

while r != 5:
    r = int(input("""MENU\n1 - Listar Pessoas\n2 - Adicionar Pessoa\n3 - Atualizar Pessoa\n4 - Remover Pessoa\n5 - Fechar Aplicação\n\n-> """))
    print("\n")

    match r:
        case 1:
            cursor.execute("select * from pessoas")
            cadastros = cursor.fetchall()
            for cadastro in cadastros:
                print("Nome: "+ cadastro[0]+"; Idade:", cadastro[1])
            print("\n")
        case 2:
            nome = input("Digite o nome a ser adicionado -> ")
            idade = input("Digite a idade de "+nome+" -> ")
            cursor.execute("insert into pessoas(nome, idade) values ('"+nome+"', "+idade+")")
            conexao.commit()
            print("\n")
        case 3:
            nome = input("Digite o nome a ser atualizado -> ")
            nvNome = input("Digite o novo nome -> ")
            cursor.execute("update pessoas set nome = '"+nvNome+"' where nome = '"+nome+"'")
            conexao.commit()
            print("\n")
        case 4:
            nome = input("Digite o nome da pessoa a ser deletado -> ")
            cursor.execute("delete from pessoas where nome = '"+nome+"'")
            conexao.commit()
            print("\n")
        case 5:
            print("Fechando aplicação...\n")