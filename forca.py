def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = str(input("Qual a letra? \n"))

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Escontrei a letra {} na posição {} ".format(letra, index))
            index = index + 1

        print("jogando...")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
