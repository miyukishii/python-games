import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    acertou = False

    nivel_facil = 1
    nivel_medio = 2
    nivel_dificil = 3

    print("Qual nível de dificuldade?")
    print("({}) Fácil ({}) Médio ({}) Difícil".format(nivel_facil, nivel_medio, nivel_dificil))

    nivel = int(input("Defina o nível: "))

    if(nivel == nivel_facil):
        total_de_tentativas = 20
    elif(nivel == nivel_medio):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # utilizando while
    # while(total_de_tentativas > 0 and acertou == False):
    #     print("Você ainda possui: {} de tentativa(s)".format(total_de_tentativas))
    #     chute = int(input("Digite o seu número: "))
    #     print("Você digitou:", chute)

    #     acertou = chute == numero_secreto
    #     chute_alto = chute > numero_secreto
    #     chute_baixo = chute < numero_secreto

    #     if(acertou):
    #         acertou = True
    #         print("Parabéns, você acertou!")
    #     else:
    #         if(chute_alto):
    #             print("Você errou. O seu chute foi maior que o número secreto.")
    #         elif(chute_baixo):
    #             print("Você errou. O seu chute foi menor que o número secreto.")

    #     total_de_tentativas = total_de_tentativas - 1
        
    # utilizando for
    for rodada in range(1, total_de_tentativas + 1):
        print("Você ainda possui: {} de tentativa(s)".format(total_de_tentativas + 1 - rodada))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou:", chute)
        
        chute_valor_min = 1
        chute_valor_max = 100
        chute_valor_invalido = (chute < chute_valor_min) or (chute > chute_valor_max)
        
        if (chute_valor_invalido):
            print("Número inválido. Você deve digitar um número entre 1 e 100")
            continue
        
        acertou = chute == numero_secreto
        chute_alto = chute > numero_secreto
        chute_baixo = chute < numero_secreto

        if (acertou):
            acertou = True
            print("Parabéns, você acertou!")
            break
        else:
            if(chute_alto):
                print("Você errou. O seu chute foi maior que o número secreto.")
            elif(chute_baixo):
                print("Você errou. O seu chute foi menor que o número secreto.")

    print("Fim de jogo, o número secreto era: {}".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()