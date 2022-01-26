import random

def rolador(lista):
    saida = random.choice(lista)
    return saida

continuar = "s"
while continuar == "s":
    d = int(input("Escolha se irá rolar um dado de 4, 6, 8, 10, 12, 20, 100 lados: "))
    if  d == 4 or d == 6 or d == 8 or d == 10 or d == 12 or d == 20 or d == 100:
        
        dado = list(range(1,d+1))

        resultado = rolador(dado)
        print()
        print("O resultado é:",resultado)
        print()
        continuar = input("Deseja rolar outro dado? Digite s para continuar. ")
    else:
        print()
        print("Entrada inválida.")
    
print("Fim da execuçao!")
    
