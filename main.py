from dados import CriadorPersonagem, listar_personagens

class Menu:
    def __init__(self):
        self.opcao = None
        self.menu = """
*** MENU ***
1 - Iniciar nova batalha
2 - Listar personagens disponíveis
0 - Sair do Sistema
"""
    def introducao(self):
        print("Bem-vindo ao Vale das Sombras!")
        print("És um dos últimos heróis que se levantou para enfrentar a maldição que assola o reino.")
        print("Escolhe o teu herói e prepara-te para lutar!")

    def executar(self):
        self.introducao()
        while True:
            print(self.menu)
            self.opcao = int(input("Selecione uma opção:\n"))
            if self.opcao == 1:
                self.iniciar_batalha()
            elif self.opcao == 2:
                listar_personagens()
                input("Pressione Enter para continuar...")  # Espera que o utilizador pressione Enter
            elif self.opcao == 0:
                print("A terminar programa!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def iniciar_batalha(self):
        heroi = None
        while heroi is None:
            tipo_heroi = input("Escolhe o teu heroi (mago/guerreiro):\n")
            heroi = CriadorPersonagem.criar_heroi(tipo_heroi)

        monstro = None
        while monstro is None:
            tipo_monstro = input("Escolhe um monstro (ogre/dragao):\n")
            monstro = CriadorPersonagem.criar_monstro(tipo_monstro)

        self.batalha(heroi, monstro)

    def batalha(self, hero, monstro):
        print(f"\nUma tempestade se aproxima... Um {monstro.nome} aparece diante de ti!")
        print(f"Estás pronto para a batalha, {hero.nome}?")

        while hero.esta_vivo() and monstro.esta_vivo():
            print(f"\nVida do {hero.nome}: {hero.vida} | Vida do {monstro.nome}: {monstro.vida}")
            print("Escolhe uma ação:")
            print("1 - Ataque comum")
            print("2 - Usar Habilidade Especial")
            acao = int(input("Selecione uma opção:\n"))

            if acao == 1:
                dano_heroi = hero.atacar(monstro)
                print(f"{hero.nome} ataca {monstro.nome} e inflige {dano_heroi} de dano!")
            elif acao == 2:
                dano_heroi = hero.habilidade(monstro)
                print(f"{hero.nome} usa uma habilidade especial em {monstro.nome} e inflige {dano_heroi} de dano!")
            else:
                print("Ação inválida!")

            if monstro.esta_vivo():
                dano_monstro = monstro.atacar(hero)
                print(f"{monstro.nome} ataca {hero.nome} e inflige {dano_monstro} de dano!")

        if hero.esta_vivo():
            print(f"\n{hero.nome} venceu a batalha e restaurou a paz no Vale das Sombras!")
        else:
            print(f"\n{monstro.nome} venceu a batalha. O Vale das Sombras continua sob ameaça!")

# Executar o menu
menu = Menu()
menu.executar()