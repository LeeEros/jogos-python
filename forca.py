def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    print(palavra)

    palavra_secreta = palavra
    letras_acertadas = ["-" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    num_tentativas = 0
    tentativas = int(input("Insira o número de tentativas \n"))

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            num_tentativas += 1

        enforcou = num_tentativas == tentativas
        acertou = "-" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou o jogo!")
    else:
        print("Você perdeu o jogo!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
