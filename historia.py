print("=== VIAGEM PARA A VILA NEVADA ===\n")

# =============================
# VARIÁVEIS DO JOGO
# =============================

falou_taxista = False
ligou_policia = False
seguiu_grupo = False
personagem = "namorado"
avisou_canivete = False


# =============================
# FINAL DA NAMORADA
# =============================

def final_namorada(avisou_canivete):

    print("\n--- PONTO DE VISTA DA SUA NAMORADA ---\n")
    print("Você acorda presa em uma gaiola dentro de uma gruta.")
    print("Pessoas estranhas estão realizando um ritual.")

    if avisou_canivete:

        print("\nVocê lembra que seu namorado avisou sobre o canivete no seu bolso.")
        print("Você pega o canivete.")

        print("\n1 - Abrir a gaiola e fugir pela gruta")
        print("2 - Atacar um membro da seita e roubar a roupa")

        escolha = input("> ")

        if escolha == "1":

            print("\nVocê abre a gaiola e foge pela gruta.")

            print("Depois de caminhar pela neve você encontra o teleférico.")
            print("Você liga para a polícia.")

            print("A ligação está perfeita.")

            print("\nA polícia diz que seu namorado tentou ligar antes,")
            print("mas a ligação estava cheia de interferência.")

            print("\nA polícia invade a vila e prende toda a seita.")

            print("\n=== FINAL SOBREVIVENTE ===")

        elif escolha == "2":

            print("\nVocê ataca um membro da seita.")
            print("Rouba a roupa dele e se disfarça.")

            print("Você sai andando pela vila sem levantar suspeitas.")

            print("Quando chega no chalé a polícia já está lá.")

            print("\nVocê conta tudo o que aconteceu.")

            print("\n=== FINAL VINGANÇA E FUGA ===")

    else:

        print("\nVocê não sabe que tem um canivete escondido.")

        print("\nUm membro da seita se aproxima.")

        print('"Eu posso te ajudar a fugir... mas precisa confiar em mim."')

        print("\n1 - Confiar nele")
        print("2 - Fingir confiar e fugir depois")

        escolha = input("> ")

        if escolha == "1":

            print("\nEle leva você até um açougue abandonado.")

            print("De repente ele tranca a porta.")

            print("Você percebe tarde demais.")

            print("Ele era um canibal.")

            print("\n=== FINAL CANIBAL ===")

        elif escolha == "2":

            print("\nVocê finge confiar.")

            print("Quando ele se distrai você corre.")

            print("Você encontra o teleférico e foge.")

            print("A polícia é avisada.")

            print("\n=== FINAL FUGA POR INTELIGÊNCIA ===")


# =============================
# INTRODUÇÃO
# =============================

print("Você e sua namorada decidiram passar alguns dias em uma vila isolada nas montanhas.")
print("Depois de horas de viagem, o táxi finalmente chega no chalé que vocês alugaram.")
print("A neve cai lentamente ao redor.\n")

print("1 - Falar com o taxista")
print("2 - Entrar direto no chalé")

escolha = input("> ")

print()

if escolha == "1":

    falou_taxista = True

    print("Você decide falar com o taxista.")
    print('"Tomem cuidado aqui em cima..." ele diz.')
    print('"As linhas telefônicas são péssimas."')
    print('"O único lugar com sinal é perto do teleférico."')

else:

    print("Você pega suas malas e entra no chalé.")


# =============================
# COZINHA
# =============================

print("\nVocês vão para a cozinha preparar algo para comer.")
print("Vocês trouxeram uma pizza.")

print("\nO suporte de facas está vazio.")

print("\n1 - Falar com sua namorada")
print("2 - Ignorar")

escolha2 = input("> ")

if escolha2 == "1":

    print("\nVocê comenta sobre a falta de facas.")
    print("Ela acha estranho também.")

    print("Ela lembra do canivete na mochila.")

else:

    print("\nVocês usam o canivete da mochila.")


print("\nDepois de comer vocês vão dormir.")


# =============================
# MANHÃ SEGUINTE
# =============================

print("\n=== MANHÃ SEGUINTE ===")

print("Sua namorada desapareceu.")

print("\n1 - Ir ao banheiro primeiro")
print("2 - Procurar ela imediatamente")

input("> ")

print("\nVocê procura pela casa inteira.")

print("Ela não está em lugar nenhum.")

print("O canivete também sumiu.")

print("\nA energia do chalé parou.")

print("O disjuntor parece arrombado.")


print("\n1 - Procurar sua namorada")
print("2 - Esperar ela voltar")

escolha4 = input("> ")

if escolha4 == "2":

    print("\nVocê espera um tempo...")
    print("Mas ela não volta.")

print("\nVocê decide procurar ela.")


# =============================
# TELEFÉRICO
# =============================

if falou_taxista:

    print("\nVocê lembra do aviso do taxista e vai até o teleférico.")

else:

    print("\nVocê tenta ligar do chalé mas não consegue sinal.")
    print("Então decide ir até o teleférico.")


print("\nPerto do teleférico você vê um grupo de pessoas com capuzes.")

print("\n1 - Ligar para a polícia")
print("2 - Seguir o grupo")

escolha5 = input("> ")

if escolha5 == "1":

    ligou_policia = True

    print("\nVocê liga para a polícia.")
    print("A ligação tem muita interferência.")

print("\nVocê decide seguir o grupo.")


# =============================
# ENCONTRO COM A SEITA
# =============================

print("\nVocê segue o grupo pela neve.")

print("\nO que você faz?")
print("1 - Falar com o grupo")
print("2 - Se esconder e observar")

escolha6 = input("> ")

if escolha6 == "1":

    print("\nVocê se aproxima do grupo.")

    print("Eles olham para você.")

    print('"Quem é você?"')

    print("Você explica que sua namorada desapareceu.")

    print('"Sabemos onde ela está."')

    print("Eles dizem que vão levar você até ela.")

    print("\nVocês caminham por uma trilha estranha.")

    print("Você vê símbolos demoníacos nas pedras.")

    print("\nVocês chegam a uma enorme mansão.")

    print("\nDe repente algo atinge sua cabeça.")

    print("Tudo fica escuro.")

    print("\nVocê acorda em uma gruta.")

    print("Sua namorada está presa ao seu lado.")

    print("Você vê o canivete no bolso dela.")

    print("\n1 - Avisar ela sobre o canivete")
    print("2 - Não avisar")

    escolha = input("> ")

    if escolha == "1":
        avisou_canivete = True

    print("\nVocê é sacrificado.")

    personagem = "namorada"


elif escolha6 == "2":

    print("\nVocê decide seguir o grupo escondido.")

    print("\nDepois de algum tempo a trilha se divide.")

    print("\n1 - Continuar seguindo eles")
    print("2 - Pegar um caminho mais seguro")

    escolha7 = input("> ")

    if escolha7 == "1":

        print("\nVocê continua seguindo eles.")

        print("Mas um deles percebe suas pegadas na neve.")

        print("\nEles te encontram.")

        print("Antes que você consiga reagir...")

        print("Você é atacado.")

        personagem = "namorada"

        print("\n=== VOCÊ MORREU ===")

    elif escolha7 == "2":

        print("\nVocê decide pegar um caminho mais seguro.")

        print("A trilha é mais longa.")

        print("\nVocê começa a ver símbolos estranhos nas árvores.")

        print("Alguns corpos congelados aparecem pelo caminho.")

        print("\nDepois de muito tempo caminhando...")

        print("Você chega em uma área aberta.")

        print("No centro existe uma enorme mansão.")

        print("Pessoas chegam de várias trilhas e entram nela.")

        print("\nAlgo muito errado está acontecendo nessa vila.")

        personagem = "namorado"


# =============================
# MANSÃO
# =============================

if personagem == "namorado":

    print("\nVocê chega perto da mansão da seita.")
    print("Você precisa entrar sem ser visto.")

    print("\n1 - Entrar por uma brecha no muro")
    print("2 - Procurar uma passagem secreta")

    escolha8 = input("> ")

    if escolha8 == "1":

        print("\nVocê tenta entrar pela brecha.")

        print("Mas várias pessoas aparecem.")

        print("Você foi encurralado.")

        print("Eles explicam que você será o sacrifício.")

        personagem = "namorada"

        print("\n=== VOCÊ FOI SACRIFICADO ===")

    elif escolha8 == "2":

        print("\nVocê encontra uma gruta secreta.")
        print("Ela conecta a floresta com a mansão.")

        print("\nDepois de caminhar você encontra sua namorada.")
        print("Ela está presa em uma gaiola.")

        print("\nVocê escuta passos chegando.")

        print("\n1 - Atacar o membro da seita")
        print("2 - Continuar escondido")

        escolha9 = input("> ")

        if escolha9 == "1":

            print("\nVocê ataca o membro da seita e vence.")

            print("\n1 - Roubar a roupa dele")
            print("2 - Esconder o corpo")

            escolha10 = input("> ")

            if escolha10 == "1":

                print("\nVocê veste a roupa da seita.")

                print("Você pega sua namorada.")

                print("Vocês passam pela cozinha e pulam a janela.")

                print("Vocês escapam pelo muro.")

                print("\nVocês voltam pela trilha até o chalé.")

                if ligou_policia:

                    print("\nA polícia chega logo depois.")

                    print("Toda a seita é presa.")

                    print("\n=== FINAL SOBREVIVENTES ===")

                else:

                    print("\nVocês fogem da vila e nunca mais voltam.")

                    print("\n=== FINAL FUGA ===")

                personagem = "final"

            elif escolha10 == "2":

                print("\nVocê esconde o corpo.")

                print("Você abre a gaiola com o canivete.")

                print("Vocês fogem pela gruta.")

                print("\nDepois de muito tempo andando...")

                print("Vocês encontram uma estrada.")

                print("Mas pessoas da vila cercam vocês.")

                print("\nVocês dois são sacrificados.")

                print("\n=== FINAL SACRIFÍCIO ===")

                personagem = "final"

        elif escolha9 == "2":

            print("\nVocê fica escondido.")

            print("O membro da seita percebe o canivete.")

            print("Ele pega o canivete dela.")

            print("\nVocê tenta arrombar a gaiola.")

            print("O barulho ecoa pela gruta.")

            print("\nVocês tentam fugir.")

            print("Mas acabam capturados.")

            print("\nVocês dois são sacrificados.")

            print("\n=== FINAL TRÁGICO ===")

            personagem = "final"








# =============================
# MORTE DO PERSONAGEM
# =============================

if personagem == "namorada":

    print("\n=== VOCÊ MORREU ===")
    print("Agora você joga com a NAMORADA.")

    final_namorada(avisou_canivete)