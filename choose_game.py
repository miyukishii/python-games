import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    jogo_forca = 1
    jogo_adivinhacao = 2

    print("({}) Forca ({}) Adivinhação".format(jogo_forca, jogo_adivinhacao))
    jogo_escolhido = int(input("Escolher o jogo: "))

    if(jogo_escolhido == jogo_forca):
        print("Você escolheu o jogo da Forca.")
        forca.jogar()
    else:
        print("Você escolheu o jogo da Adivinhação.")
        adivinhacao.jogar()
        
if(__name__ == "__main__"):
    escolher_jogo()
