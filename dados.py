from model import Mago, Guerreiro, Ogre, Dragao

class CriadorPersonagem:
    def criar_heroi(tipo):
        if tipo == "mago":
            return Mago()
        elif tipo == "guerreiro":
            return Guerreiro()
        else:
            print("Tipo de heroi inválido")
            return None


    def criar_monstro(tipo):
        if tipo == "ogre":
            return Ogre()
        elif tipo == "dragao":
            return Dragao()
        else:
            print("Tipo de monstro inválido!")
            return None

def listar_personagens():
    personagens = [
        Mago(),
        Guerreiro(),
        Ogre(),
        Dragao(),
    ]
    
    print("\nPersonagens disponíveis:")
    for personagem in personagens:
        print(f"{personagem.nome}: Vida {personagem.vida}, Ataque {personagem.ataque}")