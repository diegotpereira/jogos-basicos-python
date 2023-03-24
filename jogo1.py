import random

# Classe Jogador
class Jogador:
    
    def __init__(self, nome, vida):

        self.nome = nome
        self.vida = vida

    def ataque(self):

        return random.randint(1, 10)

# classe inimigo
class Inimigo:

    def __init__(self, nome, vida):

        self.nome = nome
        self.vida = vida 

    def ataque(self):

        return random.randint(1, 5)

# função principal
def main():

    # definir jogador e inimigo
    jogador = Jogador("Jogador", 100)
    inimigo = Inimigo("Inimigo", 50)

    # loop do jogo
    while True:

        # jogador atacando inimigo
        inimigo.vida -= jogador.ataque()
        print(f"{jogador.nome} atacou {inimigo.nome}! {inimigo.nome} agora tem {inimigo.vida} de vida.")

        # verifica se inimigo foi derrotado
        if inimigo.vida <= 0:
            print(f"{jogador.nome} venceu o jogo!")
            break;

        # inimifo ataca jogador
        jogador.vida -= inimigo.ataque()
        print(f"{inimigo.nome} atacaou {jogador.nome}! {jogador.nome} agora tem {jogador.vida} de vida.")

        # verifica se jogador foi derrotado
        if jogador.vida <= 0:
            print(f"{inimigo.nome} venceu o jogo!")
            break;

# iniciar o jogo
main()