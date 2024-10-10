import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, adversario):
        dano = random.randint(self.ataque - 10, self.ataque + 20)
        adversario.vida -= dano
        return dano

    def esta_vivo(self):
        return self.vida > 0


class Heroi(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def habilidade(self, adversario):
        pass


class Mago(Heroi):
    def __init__(self):
        super().__init__("Mago", vida=80, ataque=25)

    def atacar(self, adversario):
        dano = random.randint(self.ataque + 5, self.ataque + 10)
        adversario.vida -= dano
        return dano

    def habilidade(self, adversario):
        dano = random.randint(30, 45)
        adversario.vida -= dano
        return dano


class Guerreiro(Heroi):
    def __init__(self):
        super().__init__("Guerreiro", vida=120, ataque=15)

    def atacar(self, adversario):
        dano = random.randint(self.ataque, self.ataque + 10)
        adversario.vida -= dano
        return dano

    def habilidade(self, adversario):
        dano = random.randint(20, 40)
        adversario.vida -= dano
        return dano


class Monstro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=15)


class Ogre(Monstro):
    def __init__(self):
        super().__init__("Ogre")
        self.vida = 100
        self.ataque = 20


class Dragao(Monstro):
    def __init__(self):
        super().__init__("Dragão")
        self.vida = 120
        self.ataque = 25