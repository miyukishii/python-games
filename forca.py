import random


def jogar():
    
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    palavra_escondida = codificando_palavra(palavra_secreta)
    acertou = False
    enforcou = False
    tentativas = 7
    # tentativas = len(set(palavra_secreta)) + 3
    
    while(not acertou and not enforcou):
        
        palavra_separada = " ".join(list(palavra_escondida))
        print(f"Você ainda pode errar: {tentativas} vezes")
        print(f"Descubra a seguinte palavra de {len(palavra_secreta)} letras: {palavra_separada}")
        chute = pede_chute()
        # letra_chute = chute.get('letra_chute', None)
        
        if (chute['mensagem_de_erro'] != ""):
            print(chute['mensagem_de_erro'])
            tentativas -= 1
            continue
        
        letra_vezes_encontrada = 0
        listagem = list(palavra_escondida)
        for idx, letra in enumerate(palavra_secreta):
            if(letra.lower() == chute['letra_chute'].lower()):
                letra_vezes_encontrada = letra_vezes_encontrada + 1
                listagem[idx] = letra
            palavra_escondida = "".join(listagem)
        if (letra_vezes_encontrada == 0):
           print("A palavra não contém a letra '{}'".format(chute['letra_chute']))
           tentativas -= 1

        acertou = "_" not in palavra_escondida
        enforcou = tentativas == 0
        imprime_desenho_forca(tentativas)
    
    if(enforcou):
        print("Fim de jogo. Você perdeu! A palavra secreta era: {}".format(palavra_secreta))
    else:
        print("Parabéns, você venceu! A palavra formada é: {}".format(palavra_secreta))
    
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem-vindo ao jogo da forca!***")
    print("*********************************")
    
def imprime_desenho_forca(tentativas: int):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def carrega_palavra_secreta():
    arquivo = open("forca_palavras.txt", "r")
    palavras_opcoes = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras_opcoes.append(linha)
    arquivo.close()
    
    palavra_secreta = random.choice(palavras_opcoes)
    return palavra_secreta

def codificando_palavra(palavra_secreta: str):
    palavra_escondida = len(palavra_secreta) * "_"
    return palavra_escondida

def pede_chute():
    letra_chute = input("Digite uma letra: ").strip()
    mensagem_de_erro = ""
    
    if (letra_chute.isdigit()):
        mensagem_de_erro = "inválido: digite uma letra"

    if not len(letra_chute) == 1:
        mensagem_de_erro = "inválido: digite apenas 1 letra"
    
    return {
        'letra_chute': letra_chute,
        'mensagem_de_erro': mensagem_de_erro
    }



if(__name__ == "__main__"):
    jogar()
    