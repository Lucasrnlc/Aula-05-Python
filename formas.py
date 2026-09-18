def Circulo ():
    raio = float(input("Digite o raio do círculo: "))
    resultado = raio * raio * 3.14 
    print (resultado)

def Triângulo ():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    resultado = base * altura / 2
    print (resultado)

def Quadrado ():
    base = float(input("Digite o valor da base do quadrado: "))
    altura = float(input("Digite o valor da altura do quadrado: "))
    resultado = base * altura
    print (resultado)


def Retângulo ():
    base = float(input("Digite o valor da base do retângulo: "))
    altura = float(input("Digite o valor da altura do retângulo: "))
    resultado = base * altura
    print (resultado)

def Sair ():
    print ("Saindo do sistema...")


def Paralelogramo ():
    base = float(input("Digite o valor da base do paralelogramo: "))
    altura = float(input("Digite o valor da altura do paralelogramo: "))
    resultado = base * altura
    print (resultado)

def Losango ():
    diagonal1 = float(input("Digite o valor da primeira diagonal: "))
    diagonal2 = float(input("Digite o valor da segunda diagonal: "))
    resultado = diagonal2 * diagonal1 /2
    print (resultado)

def Trapézio ():
    base1 = float(input("Digite o valor da primeira base: "))
    base2 = float(input("Digite o valor da segunda base: "))
    altura = float(input("Digite o valor da altura do trapézio: "))
    resultado = (base2 + base1) * altura /2
    print (resultado)

while True:
    print ("ÁREA")
    print ("1 - Círculo")
    print ("2 - Triângulo")
    print ("3 - Quadrado")
    print ("4 - Retângulo")
    print ("0 - Sair")
    print ("5 - Paralelogramo")
    print ("6 - Losango")
    print ("7 - Trapézio")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Circulo()

    elif opcao == "2":
        Triângulo()

    elif opcao == "3":
        Quadrado()

    elif opcao == "4":
        Retângulo()

    elif opcao == "0":
        Sair()

    elif opcao == "5":
        Paralelogramo()

    elif opcao == "6":
        Losango()

    elif opcao == "7":
        Trapézio()