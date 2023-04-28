import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("********Esolha o seu jogo!*******")
    print("*********************************")

    print("Jogo 1: Forca\n")
    print("Jogo 2: Adivinhacao\n")

    jogo = int(input("Qual jogo?\n"))

    if (jogo == 1):
        print("Jogo da forca!")
        forca.jogar()
    elif (jogo == 2):
        print("Jogo da adivinhação")
        import adivinhacao
        adivinhacao.jogar()

    if (__name__ == "__main__"):
        escolhe_jogo()
