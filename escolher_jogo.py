import jogo_forca
import jogo_advinhacao

def escolhe_jogo():

    print("********************************")
    print("***** Escolha o seu jogo *******")
    print("********************************")


    print(" (1) Forca (2) Advinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando Forca!")
        jogo_forca.jogar_forca()
    elif (jogo == 2):
        print("Jogando Advinhação!")
        jogo_advinhacao.jogar_advinhacao ()

if(__name__ == "__main__"):
    escolhe_jogo()

