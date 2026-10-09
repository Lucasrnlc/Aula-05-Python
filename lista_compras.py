lista = ["pão", "sucrilhos", "leite", "picanha", "mortadela", "arroz", "refrigerante"]

def listinha():
    print (lista)

def add ():
    add_item = input("Qual item você deseja adicionar?: ")
    lista.append (add_item)

def excluir ():
    excluir_item = input("Qual item você deseja excluir?: ")
    lista.remove

def modificar ():
    item_antigo = input("Qual item você deseja trocar?: ")
    item_novo = input ("Qual item você deseja adicionar?: ")

    posicao = lista.index(item_antigo)
    lista [posicao] == (item_novo)

def sair ():
    print("Saindo do sistema..." )



    while True:
        print ("SUPERMERCADO")
        print ("1 - Mostrar lista")
        print ("2 - Cadastrar item na lista")
        print ("3 - Excluir item da lista")
        print ("4 - Modificar item da lista")
        print ("0 - sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":    
            listinha()

        elif opcao == "2":
            add()

        elif opcao == "3":
            listinha()
            excluir()

        elif opcao == "4":
            modificar()

        elif opcao == "0":
            sair()
            break

    
