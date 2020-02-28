linha = '-' * 100
titulo = "Jogo da Adivinhação"
nome = "Jéssica Teixeira dos Santos"

print(linha)
print(titulo.center(100))
print(linha)

print(nome.rjust(100))

print("\n\nBem vindo ao jogo da avivinhação, estou pensando em um número inteiro de 0 a 10, que número é este?\nSe você quiser fechar o jogo basta digiar '-1'\n")

from random import *

t = randint(0,10)
z = 0
y = 0

while (z != -1):
    z = input("Digite um número inteiro de 0 a 10:\n")

    if (z == "-1"):
        y = -1

    try:
        val = int(z)
        z = int(z)
    except ValueError:
        try:
            val = float(z)
            print("Este é um Float, eu preciso de um número inteiro de 0 a 10!\n")
            z = int(0)
            y = 1
        except ValueError:
            z = int(0)
            y = 1
            print("Este é um string, eu preciso de um número inteiro de 0 a 10!\n")

    if (z == t):
        print("Você acertou!\n")
        t = randint(0,10)
    elif (z < 0) and (y == 0):
        print("Este numero é muito pequeno, tente novamente!\n")
    elif (z > 10 and y == 0):
        print("Este numero é muito grande, tente novamente!\n")
    elif (z != t) and (y == 0):
        print("Incorreto, tente novamente!\n")
    y = 0

print("Você saiu do Jogo da Adivinhação.")