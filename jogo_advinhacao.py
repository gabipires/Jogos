import random

def jogar_advinhacao():
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    # numero_secreto=42 - número fixo, vamos gerar de forma aleatória
    # numero_secreto=round(int(random.random()*100))

    numero_secreto=random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print(" (1) Fácil (2) Médio (3) Difícil")

    #print(numero_secreto)
    nivel = int(input("Defina o nível:"))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Enquanto ainda há tentativas disponíveis:

    for rodada in range (1, total_de_tentativas+1):

        # print("Tentativa:", rodada, "de", total_de_tentativas)

        # string interpolation
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        # chute_str= input("Digite o seu número: ")
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # O padrão de saída do input é do tipo string

        chute=int(chute_str)

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        print("Você digitou ", chute)

        if (acertou):
            print("Você acertou o número secreto e fez {} pontos!" .format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos" .format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            # print("Você possui {} pontos!" .format(pontos))

        rodada = rodada + 1

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar_advinhacao()