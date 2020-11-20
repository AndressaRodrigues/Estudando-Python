#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random

craps = [2, 3, 12]
natural = [7, 11]
deNovo = [4, 5, 6, 8, 9, 10, 11]
entradas = ["!", "y", "n"]
buscaPar = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 0]

def segJogada(x):
    buscaPar[10] = x
    while True:
        k = random.randint(2, 12)
        if (k == 7):
            print("O número sorteado foi:", k)
            print("Craps! Você perdeu.")
            break
        if (k == buscaPar[-1]):
            print("O número sorteado foi:", k)
            print("Você ganhou!")
            break
        if k in buscaPar[0:9]:
            print("O número sorteado foi:", k)
            print("Vamos de novo.")



def jogada():
    i = random.randint(2, 12)
    if i in natural:
        print("O número sorteado foi:", i)
        return "Natural. Você ganhou!"
    if i in craps:
        print("O número sorteado foi:", i)
        return "Craps! Você perdeu."
    if i in deNovo:
        print("Ponto!")
        print("Seu número da sorte é:", i)
        print("Rolando os dados de n...")
        segJogada(i)
    

def jogar(x):
    while True:
        if (x == "y"):
            jogada()
            return True
       

def regras():
    print("As regras do jogo são:")
    print("Dois dados são rolados a cada jogada.")
    print( "Se você tirar 7 ou 11, você venceu.")
    print("Se tirar 2, 3 ou 12, você perdeu.")
    print("Qualquer outro número, você seguirá rolando até achar o mesmo número novamente.")
    print("Porém! Se achar 7 antes de achar o par correspondente, você perde.\n")
    return True

while True:
    try:
        print("Digite '!' para ver as regras, 'y' para jogar, ou 'n' para parar:")
        b = input()
        if (b =="y"):
            jogar(b)
        if (b == "!"):
            regras()
        if (b == "n"):
            print("fim de jogo")
            break
           
    except (KeyboardInterrupt, SystemExit):
        raise
 
    