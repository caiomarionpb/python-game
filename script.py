def criar_personagem():
    print("=== BEM-VINDO AO LABIRINTO DO FAUNO ===\n")
    print("Espanha, 1944. A guerra civil terminou, mas os horrores continuam...")
    print("Você é uma criança que descobriu um mundo mágico escondido.\n")

    nome = input("Digite seu nome: ")

    print("\nEscolha seu dom especial:")
    print("1 - Coragem (mais resistente aos medos)")
    print("2 - Curiosidade (melhor em resolver enigmas)")
    print("3 - Compaixão (animais mágicos te ajudam)")

    while True:
        escolha_classe = input("\nDigite o número da sua escolha (1-3): ")
        if escolha_classe == "1":
            classe = "Corajoso"
            hp_bonus = 2
            break
        elif escolha_classe == "2":
            classe = "Curioso"
            hp_bonus = 1
            break
        elif escolha_classe == "3":
            classe = "Compassivo"
            hp_bonus = 1
            break
        else:
            print("Escolha inválida! Tente novamente.")

    hp_inicial = 8 + hp_bonus

    print(f"\n{nome}, criança {classe.lower()}, o Fauno te espera...")
    print(f"Você possui {hp_inicial} pontos de esperança.")
    print("ATENÇÃO: Este labirinto é perigoso e impiedoso...")

    return nome, classe, hp_inicial


def mostrar_status(nome, classe, hp):
    if hp >= 7:
        estado = "Determinado"
    elif hp >= 4:
        estado = "Abalado"
    else:
        estado = "Desesperado"

    print(f"\n--- {nome} o {classe} | Esperança: {hp} | Estado: {estado} ---")


def desafio_mandrake():
    print("\nVocê encontra uma árvore retorcida com uma raiz em formato humano - uma Mandrágora!")
    print("Ela sussurra: 'Três gotas de sangue e eu te darei poder...'")
    print("'Mas se errar a quantidade, sua alma será minha!'")

    tentativas = 2
    quantidade_correta = "3"

    for tentativa in range(tentativas):
        resposta = input(f"Tentativa {tentativa + 1}/2 - Quantas gotas? (1-5): ")

        if resposta == quantidade_correta:
            print("A Mandrágora brilha! 'Você é sábio, criança.'")
            print("Ela te dá uma folha mágica que pode salvar sua vida.")
            return 4, True
        else:
            print("A Mandrágora grita! Seus ouvidos sangram!")

    print("Você falhou! A Mandrágora drena sua força vital!")
    return -3, False


def desafio_livro_maldito():
    print("\nUm livro antigo flutua no ar, suas páginas viram sozinhas.")
    print("Palavras aparecem: 'Resolva meu enigma ou pereça em ignorância'")
    print("'O que tem olhos mas não vê, boca mas não fala, e devora tudo que toca?'")

    tentativas = 2
    resposta_correta = "fogo"

    for tentativa in range(tentativas):
        resposta = input(f"Tentativa {tentativa + 1}/2 - Sua resposta: ").lower()

        if resposta == resposta_correta or resposta == "o fogo":
            print("CORRETO! O livro se abre revelando um mapa do labirinto!")
            print("Você ganha conhecimento sobre os perigos à frente.")
            return 2, True
        else:
            print("ERRADO! O livro solta fagulhas que te queimam!")

    print("O livro se fecha com violência e explode em chamas!")
    print("Você é atingido pela explosão mágica!")
    return -4, False


def desafio_espelho_alma():
    print("\nUm espelho ornamentado mostra não seu reflexo, mas seus medos.")
    print("Uma voz ecoa: 'Encare sua verdade mais sombria ou fuja como covarde'")
    print("No espelho você vê...")
    print("1 - Seu maior medo")
    print("2 - Uma versão sombria de você")
    print("3 - Quebrar o espelho")

    escolha = input("O que você faz? ")

    if escolha == "1":
        print("Você encara seu medo de frente!")
        print("O espelho se estilhaça, mas você sai mais forte.")
        return 3
    elif escolha == "2":
        print("Você luta contra sua versão sombria!")
        print("É uma batalha intensa que deixa cicatrizes na alma.")
        return -1
    elif escolha == "3":
        print("Você quebra o espelho em desespero!")
        print("Cada fragmento corta sua esperança.")
        return -3
    else:
        print("Sua hesitação permite que o espelho te capture!")
        return -2


def encontro_capitao():
    print("\nVocê ouve botas militares ecoando!")
    print("O Capitão Vidal aparece, seus olhos frios como aço.")
    print("'Uma criança perdida... que pena.'")
    print("1 - Tentar se esconder")
    print("2 - Confrontá-lo bravamente")
    print("3 - Tentar distraí-lo com uma mentira")

    escolha = input("Sua escolha: ")

    if escolha == "1":
        print("Você se esconde atrás de uma coluna.")
        print("Ele passa sem te ver, mas você está abalado.")
        return -1
    elif escolha == "2":
        print("'Você não me assusta!' você grita.")
        print("Ele ri cruelmente e te empurra.")
        return -2
    elif escolha == "3":
        print("'Estou procurando minha mãe!' você mente.")
        print("Ele te ignora, mas você sente vergonha da mentira.")
        return -1
    else:
        print("Você congela de medo!")
        return -3


def sala_sapos():
    print("\nVocê entra numa sala úmida cheia de sapos gigantes!")
    print("Eles bloqueiam todas as saídas, croakando ameaçadoramente.")
    print("1 - Tentar passar correndo entre eles")
    print("2 - Oferecer algo em troca da passagem")
    print("3 - Cantar uma canção para acalmá-los")

    escolha = input("O que você faz? ")

    if escolha == "1":
        print("Você corre! Alguns sapos te atacam com suas línguas!")
        return -2
    elif escolha == "2":
        print("Você oferece um botão do seu casaco.")
        print("Os sapos ficam interessados e abrem caminho.")
        return 1
    elif escolha == "3":
        print("Sua canção ecoa pela sala.")
        print("Os sapos ficam hipnotizados e te deixam passar.")
        return 2
    else:
        print("Você fica parado. Os sapos te cercam!")
        return -3


def jogo_principal():
    nome, classe, hp = criar_personagem()
    tem_giz = False
    tem_folha_magica = False
    tem_mapa = False
    passos_dados = 0
    tarefas_completadas = 0

    print(f"\n{nome}, você está na entrada do labirinto subterrâneo.")
    print("O Fauno disse que CINCO tarefas te aguardam antes de encontrar a verdade...")
    print("Mas cuidado... nem todos que entram conseguem sair...")

    while hp > 0 and tarefas_completadas < 5:
        mostrar_status(nome, classe, hp)
        passos_dados += 1

        if hp <= 3:
            print("\n⚠️  PERIGO: Sua esperança está se esgotando!")

        # Cenários aleatórios baseados nos passos
        cenario = passos_dados % 6

        if cenario == 1:
            print("\nVocê chega a uma bifurcação no labirinto:")
            print("1 - Seguir pelo corredor com raízes de árvore")
            print("2 - Entrar na câmara com símbolos antigos")
            print("3 - Descer pela escadaria em espiral")
            print("4 - Voltar ao mundo real")

            escolha = input("O que você escolhe? (1-4): ")

            if escolha == "1":
                print("\nVocê segue pelo corredor orgânico...")
                hp_ganho, encontrou_item = desafio_mandrake()
                hp += hp_ganho
                if encontrou_item:
                    tem_folha_magica = True
                    tarefas_completadas += 1

            elif escolha == "2":
                print("\nVocê entra na câmara misteriosa...")
                hp_ganho, tem_mapa = desafio_livro_maldito()
                hp += hp_ganho
                if tem_mapa:
                    tarefas_completadas += 1

            elif escolha == "3":
                print("\nVocê desce as escadas rangendo...")
                hp += encontro_capitao()

            elif escolha == "4":
                print(f"\n{nome} decide que o mundo mágico é muito perigoso.")
                print("FINAL COVARDE - Você fugiu antes mesmo de tentar.")
                return

        elif cenario == 2:
            print("\nVocê encontra uma sala de espelhos!")
            hp += desafio_espelho_alma()
            tarefas_completadas += 1

        elif cenario == 3:
            print("\nVocê entra numa câmara alagada...")
            hp += sala_sapos()

        elif cenario == 4:
            print("\nSoldados! Você ouve vozes se aproximando!")
            print("1 - Se esconder e esperar")
            print("2 - Procurar outra rota rapidamente")

            escolha = input("Sua escolha: ")
            if escolha == "1":
                print("Você consegue se esconder, mas perde tempo precioso.")
                hp -= 1
            else:
                print("Você corre e se perde ainda mais no labirinto!")
                hp -= 2

        elif cenario == 5:
            print("\nO labirinto parece estar mudando ao seu redor!")
            print("As paredes se movem sozinhas!")
            if tem_mapa:
                print("Seu mapa te guia pela mudança!")
                hp += 1
            else:
                print("Você fica perdido e desesperado!")
                hp -= 2

        else:
            print("\nVocê encontra uma fonte com água cristalina.")
            print("1 - Beber da fonte")
            print("2 - Ignorar e seguir em frente")

            escolha = input("Sua escolha: ")
            if escolha == "1":
                if passos_dados % 3 == 0:
                    print("A água está envenenada! Você se sente mal!")
                    hp -= 3
                else:
                    print("A água restaura suas forças!")
                    hp += 2

        if hp <= 0:
            break

        # Verificação de itens especiais
        if hp <= 2 and tem_folha_magica:
            print("\n🍃 A folha mágica brilha! Ela restaura sua esperança!")
            hp += 3
            tem_folha_magica = False

        # Encontro com o Homem Pálido (mais punitivo)
        if tarefas_completadas >= 3:
            print(f"\nO ar fica pesado... você sente uma presença maligna!")
            print("O Homem Pálido emerge das sombras!")
            print("'Criança tola... você chegou longe demais.'")

            print("\n1 - Enfrentar diretamente")
            print("2 - Tentar resolver seu enigma")
            print("3 - Tentar fugir")
            if tem_giz:
                print("4 - Usar o giz mágico")

            escolha_inimigo = input("Sua escolha: ")

            if escolha_inimigo == "1":
                print("\nVocê encara a criatura!")
                if classe == "Corajoso":
                    dano = 1 if passos_dados % 4 == 0 else 2
                elif classe == "Curioso":
                    dano = 2 if passos_dados % 3 == 0 else 1
                else:
                    dano = 1 if passos_dados % 2 == 1 else 3

                hp -= dano
                print(f"Você luta bravamente mas se machuca! Perdeu {dano} esperança.")

            elif escolha_inimigo == "2":
                print("\n'Três portas, duas mentiras, uma verdade. Qual escolher?'")
                resposta = input("Porta 1, 2 ou 3? ")

                if resposta == "2":
                    print("Correto! Era uma ilusão - você passa!")
                    hp += 1
                else:
                    print("ERRADO! Armadilhas disparam de todas as direções!")
                    hp -= 4

            elif escolha_inimigo == "3":
                print("Você tenta fugir mas ele é mais rápido!")
                hp -= 3

            elif escolha_inimigo == "4" and tem_giz:
                print("O giz cria uma barreira, mas ela se quebra rapidamente!")
                hp -= 1
                tem_giz = False

            tarefas_completadas += 1

    # Finais baseados no estado atual
    if hp <= 0:
        if passos_dados < 5:
            print(f"\n=== FINAL PREMATURO ===")
            print(f"{nome} sucumbiu cedo demais aos perigos...")
            print("O labirinto engoliu mais uma alma inocente.")
        elif tem_folha_magica or tem_mapa:
            print(f"\n=== FINAL HEROICO ===")
            print(f"{nome} lutou até o fim com coragem!")
            print("Mesmo derrotado, sua bravura ecoará pelos corredores.")
        else:
            print(f"\n=== FINAL SOMBRIO ===")
            print(f"{nome} se perdeu completamente no labirinto...")
            print("Nem mesmo o Fauno consegue mais encontrá-lo.")

    elif tarefas_completadas >= 5:
        print(f"\nVocê finalmente chega ao coração do labirinto...")
        print("O Fauno está lá, mas parece mais sério e sombrio.")
        print("'Você provou ser resiliente, criança. Mas o preço foi alto.'")
        print("'A última escolha determinará não apenas seu destino,'")
        print("'mas o de todos que você deixou para trás.'")

        print("\n1 - Aceitar o trono e esquecer o mundo mortal")
        print("2 - Voltar e lutar no mundo real")
        print("3 - Pedir para salvar os outros também")

        escolha_final = input("Sua escolha final: ")

        if escolha_final == "1":
            print(f"\n=== FINAL EGOÍSTA ===")
            print(f"{nome} se torna governante, mas à custa de abandonar todos.")
            print("O poder corrompe, e você se torna um tirano cruel.")

        elif escolha_final == "2":
            print(f"\n=== FINAL SACRIFICIAL ===")
            print(f"{nome} renuncia à magia para lutar no mundo real.")
            print("Você volta determinado a fazer a diferença, custando a própria vida.")

        elif escolha_final == "3":
            if hp >= 6:
                print(f"\n=== FINAL VERDADEIRO ===")
                print(f"{nome} usa sua pureza para salvar ambos os mundos!")
                print("Você se torna a ponte entre realidade e fantasia!")
            else:
                print(f"\n=== FINAL TRÁGICO ===")
                print(f"{nome} tenta salvar todos, mas não tem força suficiente.")
                print("Ambos os mundos desmoronam. Sua bondade causou o fim.")

    else:
        print(f"\n=== FINAL INCOMPLETO ===")
        print(f"{nome} não conseguiu completar todas as tarefas.")
        print("Você fica preso no labirinto para sempre, nem vivo nem morto.")


if __name__ == "__main__":
    jogo_principal()