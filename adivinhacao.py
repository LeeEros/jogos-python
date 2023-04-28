import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 100
    print(numero_secreto)

    print("Qual o nível de dificuldade \n")
    print("(1) Fácil (2) Médio (3)Difícil \n")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 3
    elif (nivel == 2):
        total_tentativas = 2
    elif (nivel == 3):
        total_tentativas = 1
    else:
        print(Exception("Você não escolheu uma diculdade esperada: "))

    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {} tentativas".format(rodada, total_tentativas))
        chute_str = input("Digiteum número entre 1 e 100 número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break

        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            if (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

        print("Fim do jogo")
