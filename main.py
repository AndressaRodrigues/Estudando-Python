#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random

d = []
craps = [2, 3, 12]
natural = [7, 11]
deNovo = [4, 5, 6, 8, 9, 10, 11]


def segJogada(x):
    k = random.randint(2, 12)
    if (k == 7):
        print(k)
        return "Craps! Você perdeu."
    elif (k == x):
        print(k)
        return "Você ganhou!"
    else:
        print(k)
        d.append(k)
        segJogada(k)
        return (k)

def jogada():
    i = random.randint(2, 12)
    if i in natural:
        print(i)
        return "Natural. Você ganhou!"
    elif i in craps:
        print(i)
        return "Craps! Você perdeu."
    elif i in deNovo:
        print(i)
        print("Ponto!")
        d.append(i)
        segJogada(i)
    

def jogar(x):
    if (x == "y"):
        print(jogada())
        return True
    elif (x == 'n'): 
        return False
    #elif (b == "!"):
    #    regras()
    else:
        print("Resposta inválda.")
        print("Digite 'y' para jogar, ou 'n' para parar:")
        p = input()
        jogar(p)
        return p

def regras():
    print("As regras do jogo são:")
    print("Dois dados são rolados a cada jogada.")
    print( "Se você tirar 7 ou 11, você venceu.")
    print("Se tirar 2, 3 ou 12, você perdeu.")
    print("Qualquer outro número, você seguirá rolando até achar o mesmo número novamente.")
    print("Porém! Se achar 7 antes de achar o par correspondente, você perde.")
    return

while True:
    print("Digite '!' para ver as regras, 'y' para jogar, ou 'n' para parar:")
    b = input()
    jogar(b)
    if (jogar(b)==False):
        print("fim de jogo")
        break
    