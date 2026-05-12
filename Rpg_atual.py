#-------- INICIO ----------
import time
import random
import artes




def titulo ():
    
    print("Bem vindo a Cyberpunk RPG!")
    time.sleep(1)
    print("Você deseja viver como um zé ninguém ou morrer como uma lenda?")
    time.sleep(1)
    print("Está pronto pra ter uma vida miserável?")
    time.sleep(1)
    start = input("Digite sim para começar: ")
    if start not in ["sim", "s", "Sim", "S"]:
        time.sleep(1)
        print("Você não tem escolha, prepare-se para o inferno! "
        "Ass: M.E.R.C")
    time.sleep (1)

#-------- Criação de personagem -------
def iniciar_jogo ():
    print("Crie sua aberração cibernética: ")
    time.sleep(1)
    nome_player = input("Nome do seu personagem: ")
    time.sleep(1)
    lvl = 1
    exp = 0
    status = True


    return nome_player, lvl, exp, status
#-------- História --------
def comeco_historia():
    import artes
    print("\nVocê acorda em um ferro velho.")
    time.sleep(2)
    print("\nA luz do sol te cega por alguns segundos, até realmente ver uma pilha de corpos logo adiante.")
    time.sleep(2)
    print("\nSua arma, ao seu lado, tão cromada, que chega a ser doentio, totalmente suja de sangue.")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("\nO MEDO TE CONSOME!!!")
    time.sleep(2)
    print(f"\n{nome_player}: Onde estou? Quem são essas pessoas?")
    time.sleep(2)
    print(f"\n{nome_player} grita: TEM ALGUEM AQUI?")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("\nVocê só escuta o barulho das maquinas da região desértica...")
    time.sleep(2)
    print("\nAo tentar se levantar, seus implantes rangem e saem faísca.")
    time.sleep(2)
    print("\nVocê cai novamente.")
    time.sleep(2)
    print("\nAo tentar verificar sua memória: \n [ERR0R: Fr4gmentos de memór1a corr0mpidos]")
    time.sleep(2)
    print("\nNão há memória. Nenhuma. Só o seu nome, gravado em algum lugar fundo.")
    time.sleep(2)
    print("\nVocê olha um pouco mais ao seu redor e percebe que está na Zona de Exclusão Beta")
    time.sleep(2)
    print(artes.zona_beta)
    time.sleep(2)
    print("\nLocal onde a M.E.R.C. tentou implantar varios sistemas militares, mas por conta de um erro, houve uma grande detonação de bombas")
    time.sleep(2)
    print("\nDesde então, é apenas um local sem natureza, somente lixo, pobres e ladrões, todos buscando sobreviver.")
    time.sleep(2)
    print("\nDe repente, você ouve passos.")
    time.sleep(2)
    print("\nUma voz ao longe: \"É ele. Tá vivo. A recompensa é nossa.\"")
    time.sleep(2)
    print("\nRecompensa.")
    time.sleep(2)
    print("\nAlguém quer você morto... e pagou bem por isso")
    time.sleep(2)
    print("\nVocê não sabe quem, nem por quê.")
    time.sleep(2)
    print("\nMas a resposta está lá fora — se você conseguir sobreviver até encontrá-la.")
    time.sleep(2)
    print("\nDo casebre ao lado, surge o primeiro deles:")
    time.sleep(2)
    print("\n>>> PROTOCÓLO: Derrote os inimigos e chegue ao nível 5")
    time.sleep(2)


def evento_raka():
    print("\n...")
    time.sleep(2)
    print("\n Depois de fazer uma chacina no local, você foge em direção a cidade")
    time.sleep(2)
    print(artes.cidade)
    time.sleep(2)
    print("Ômega City")
    time.sleep(2)
    print("Ao chegar em Ômega City, você para em frente uma loja, bem familiar")
    time.sleep(2)
    print(artes.andando_cidade)
    print("\nVocê sente uma mão te puxar pra dentro de um beco escuro.")
    time.sleep(2)
    print("\nUma mulher de olhos cibernéticos te encara. Ela parece te reconhecer.")
    time.sleep(2)
    print("\nRAKA: Você não devia estar vivo.")
    time.sleep(2)
    print(f"\n{nome_player}: Quem é você?")
    time.sleep(2)
    print("\nPor algum motivo você sabe o nome dela, RAKA.")
    time.sleep(2)
    print(f"\n{nome_player}: Seu nome é RAKA?")
    time.sleep(2)
    print("\nRAKA: Sou apenas alguém que cometeu um erro muito grande.")
    time.sleep(2)
    print("\nRAKA: Eu ajudei a colocar esse implante em você. Em todos vocês.")
    time.sleep(2)
    print("\nRAKA: O que aconteceu naquela noite no ferro velho... não foi um acidente.")
    time.sleep(2)
    print("\nAntes que ela possa dizer mais, um tiro atravessa a janela.")
    time.sleep(2)
    print("\nRAKA cai.")
    time.sleep(2)
    print("\nUma mensagem pisca no seu implante neural:")
    time.sleep(2)
    print("\n>>> SETOR 7. SOZINHO. SE QUISER SABER QUEM VOCÊ ERA. <<<")
    time.sleep(2)
    print("\nVocê volta a caminhar por um beco, esgueirando-se para continuar escondido.")
    time.sleep(2)
    print("\nPor um momento você começa a lembrar o que aconteceu naquele lugar.")
    time.sleep(2)
    print(f"\n{nome_player}: Um protocolo? Eu fugi de algum lugar... Que lugar é esse?")
    time.sleep(3)
    print("\nAntes mesmo de você pensar mais inimigos aparecem para ter a sua recompensa")
    time.sleep(2)

def evento_setor7():
    print("\n...")
    time.sleep(2)
    print("\nHá uma pilha de corpos na sua frente")
    time.sleep(2)
    print(f"\n{nome_player} Mário, melhor sair daqui, antes que alguem descubra quem os matou")
    time.sleep(2)
    print("\nVocê chega ao Setor 7.")
    time.sleep(2)
    print("\nO lugar parece abandonado. Mas você sente que está sendo observado.")
    time.sleep(2)
    print("\nDrones Omnicorp surgem de todos os lados.")
    time.sleep(2)
    print("\nEles sabiam que você viria.")
    time.sleep(2)
    print("\nUma voz ecoa pelos alto-falantes do setor:")
    time.sleep(2)
    print("\nDesconhecido: Você deveria ter morrido no ferro velho.")
    time.sleep(2)
    print(f"\n{nome_player}: Erro de vocês.")
    time.sleep(2)
    print("Ao olhar o portão, Você observa um simbolo...")
    time.sleep(2)
    print(f"\n{nome_player}: Omnicorpe... A maior corporação de tecnologia e implantes neurais da cidade.")
    time.sleep(1)
    print(f"\n{nome_player}Controlam os dados de milhões. Acima da lei. Acima de tudo.")
    time.sleep(2)
    print("\nVocê começa a avançar. Mas algo muda no ar.")
    time.sleep(2)
    print("\nOs agentes Omnicorp recuam. Alguém maior está chegando.")
    time.sleep(2)
    print("\nHelicópteros militares cortam o céu. Soldados descem em cordas.")
    time.sleep(2)
    print("\nM.E.R.C.: Alvo confirmado. Autorização de extermínio concedida.")
    time.sleep(2)
    print(f"\n{nome_player}: Quem são vocês?")
    time.sleep(2)
    print("\nM.E.R.C.: Sua sentença.")
    time.sleep(2)
    print(f"\n{nome_player}: Milícia militar privada. Sem bandeira. Sem código.")
    time.sleep(2)
    print(f"\n{nome_player}: Contratados para terminar o que a Omnicorp não conseguiu.")
    time.sleep(2)
    print("\n>>> DIRETIVA: Elimine os agentes da Omnicorp e da M.E.R.C. e chegue ao nível 15. <<<")
    time.sleep(2)

def evento_raka_chefe():
    print("\n...")
    time.sleep(2)
    print("\nNo centro do Setor 7, você encontra o terminal que enviou a mensagem.")
    time.sleep(2)
    print("\nAo acessá-lo, arquivos começam a aparecer.")
    time.sleep(2)
    print("\nFotos. Relatórios. Experimentos.")
    time.sleep(2)
    print("\nTodos com o seu rosto.")
    time.sleep(3)
    print("\nUm arquivo de voz. Sua própria voz.")
    time.sleep(2)
    print(f"\n{nome_player} (gravação): Se você está ouvindo isso... funcionou.")
    time.sleep(2)
    print(f"\n{nome_player} (gravação): Não confie em ninguém que sobreviveu àquela noite além de você.")
    time.sleep(3)
    print("\nVocê ouve passos atrás de você.")
    time.sleep(2)
    print("\nRAKA está de pé. O tiro não a matou.")
    time.sleep(2)
    print("\nRAKA: Demorou mais do que eu esperava pra você chegar aqui.")
    time.sleep(2)
    print(f"\n{nome_player}: Você estava morta.")
    time.sleep(2)
    print("\nRAKA: Eu nunca estive tão viva.")
    time.sleep(2)
    print("\nRAKA: Você era o único erro que eu precisava corrigir.")
    time.sleep(2)
    print("\nEla sorri. Seus olhos cibernéticos pulsam em vermelho.")
    time.sleep(2)
    print("\n>>> RAKA — PROTÓTIPO 0 <<<")
    time.sleep(2)
    print(">>> HP: 200 | FORÇA: 20 | AGILIDADE: 16 <<<")
    time.sleep(3)

def evento_final():
    print("\n...")
    time.sleep(2)
    print("\nRAKA cai pela última vez.")
    time.sleep(2)
    print("\nO terminal começa a piscar. Uma contagem regressiva.")
    time.sleep(2)
    print("\n>>> AUTODESTRUIÇÃO INICIADA — 60 SEGUNDOS <<<")
    time.sleep(2)
    print(f"\n{nome_player} corre.")
    time.sleep(2)
    print("\nAs paredes do Setor 7 colapsam atrás de você.")
    time.sleep(2)
    print("\nVocê escapa.")
    time.sleep(3)
    print("\n...")
    time.sleep(2)
    print("\nNa sua mão, um último arquivo do terminal.")
    time.sleep(2)
    print("\nVocê abre.")
    time.sleep(2)
    print("\n>>> PROJETO LAZARUS — STATUS: ENCERRADO <<<")
    time.sleep(2)
    print("\n>>> SOBREVIVENTES CONFIRMADOS: 1 <<<")
    time.sleep(3)
    print(f"\n{nome_player}.")
    time.sleep(3)
    print("\nPor enquanto.")
    time.sleep(3)
    print("\n>>> FIM <<<")

#-------Criar classe -------
def classe ():
    print("Escolha sua classe:")
    time.sleep(1)
    print("\n1- Cyber Samurai: + 2 força, 20 HP + 2 agilidade .")
    time.sleep(2)
    print("Habilidades: Zandatsu, Amolador de plasma")
    time.sleep(2)
    print("\n2- BioHacker:  25 HP, + 8 cura extra, + 3 estimulantes.")
    time.sleep(2)
    print("Hablidades: Seringa de adrenalina Overclock, Toxina experimental.")
    time.sleep(2)
    print("\n3- Netrunner: + 1 força, 15 HP + 4 agilidade")
    time.sleep(2)
    print("Habilidades:Software de Transmissão Viral, Chip de hack.")
    time.sleep(2)
    while True: 
        clas = input(f"Qual será a classe de {nome_player} ? ")
        if clas == "1":
            print("Um guerreiro das ruas que trocou a honra pelo cromo.  Usa uma Katana Cromada de alta frequência, para cortar qualquer coisa")
            time.sleep(2)
            print("Descrição de habilidades: \n Zandatsu: Capacidade de parar o tempo e fatiar o inimigo quantas vezes quiser.")
            time.sleep(2)   
            print("Causa morte instantanea no próximo crítico.")
            time.sleep(2)
            print("\nAmolador de plasma: Amolador avançado, reconstrói totalmente o fio da espada.")
            time.sleep(2)
            print("+ 3 de força por 5 turnos.")
            time.sleep(2)
            break
        elif clas == "2":
            print("Metade humano, metade laboratório ambulante. Hackeou o próprio corpo e sabe exatamente onde uma bala de 9mm dói mais.\nCarrega Kit Médico porque sempre precisa se remendar depois.")
            time.sleep(2)
            print("Descrição de habilidades: \nSeringa Overclock: Seringa de alta capacidade elétrica, fortalece os neurônios em 200%, fazendo o usuário enxergar os pontos vitais do inimigo.")
            time.sleep(2)
            print("+ 15 HP e crítico nos próximos 2 turnos.")
            time.sleep(2)
            print("\nToxina experimental: \nToxina inventada em laboratório próprio, faz todo o cromo inimigo corroer apenas ao entrar em contato.")
            time.sleep(2)
            print("Causa 3 de dano por 5 turnos.")
            time.sleep(2)
            break
        elif clas == "3":
            print("Vive na borda entre o mundo real e a rede. Antes de você puxar o gatilho, ele já travou seus implantes. Usa uma Pistola Furtiva e Hack Chips pra deixar você nu no sistema.")    
            time.sleep(2)
            print("Descrição de habilidades: \n Software de Transmissão Viral: Hack que infecta o sistema neural do inimigo, o fazendo atacar a sí.")
            time.sleep(2)
            print("O inimigo causa dano em sí no próximo turno.")
            time.sleep(2)
            print("Chip de hack: Implante neural que possibilita a leitura do próximo ataque inimigo.")
            time.sleep(2)
            print("Defende o próximo ataque inimigo.")
            time.sleep(2)
            break  
        else:
            print("Digite somente 1, 2 ou 3.")
             
    return clas
    
def aplicar_classe(clas):
    
    if clas == "1":  # Cyber Samurai
        hp_max = 20
        hp = 20
        forca = 3
        agil = 3   
        crit_classe = 9       
        inventario = ["Estimulante"]
        chance_combo = 0.4
        cura_bonus = 0
        nome_classe = "Cyber Samurai"

    elif clas == "2":  # BioHacker
        hp_max = 30
        hp = 25
        forca = 1
        agil = 1   
        crit_classe = 8       
        inventario = ["Estimulante", "Estimulante", "Estimulante"]
        chance_combo = 0.3
        cura_bonus = 8
        nome_classe = "BioHacker"

    elif clas == "3":  # Netrunner
        hp_max = 15
        hp = 15
        forca = 2
        agil = 5   
        crit_classe = 10      
        inventario = ["Hack Chip", "Estimulante"]
        chance_combo = 0.5
        cura_bonus = 0
        nome_classe = "Netrunner"

    print(f"\n[+] Classe {nome_classe} ativada!")
    print(f"    HP: {hp} | Força: {forca} | Agilidade: {agil} | Inventário: {inventario}")

    return hp, hp_max, forca, agil, inventario, chance_combo, cura_bonus, crit_classe
# -------- CYBER SAMURAI --------
def usar_zandatsu():
    global zandatsu_disponivel, zandatsu_ativo
    if not zandatsu_disponivel:
        time.sleep(1)
        print("\n[!] Zandatsu já foi usado nesse combate.")
        return
    
    time.sleep(2)
    print("[*] ZANDATSU ATIVADO — Próximo crítico será HITKILL!")
    zandatsu_disponivel = False
    zandatsu_ativo = True

def usar_amolador(amolador_ativo):
    if amolador_ativo > 0:
        time.sleep(1)
        print(f"\n[!] Amolador já está ativo por mais {amolador_ativo} turnos.")
        return amolador_ativo
    time.sleep(1)
    print("\nVocê balança a espada e puxa o amolador de plasma.")
    time.sleep(1)
    print("[*] AMOLADOR ATIVO — +3 de força pelos próximos 3 turnos!")
    return 3

# -------- BIOHACKER --------
def usar_seringa(hp, hp_max, seringa_criticos):
    if seringa_criticos > 0:
        time.sleep(1)
        print(f"\n[!] Seringa já está ativa por mais {seringa_criticos} ataques.")
        return hp, seringa_criticos
    time.sleep(1)
    print("\nVocê injeta a seringa no braço e grita de dor.")
    time.sleep(1)
    hp = min(hp_max, hp + 15)
    seringa_criticos = 2
    time.sleep(1)
    print(f"[*] OVERCLOCK ATIVO — +15 HP | Próximos 2 ataques são críticos! HP: {hp}")
    return hp, seringa_criticos

def usar_toxina(toxina_ativa):
    if toxina_ativa > 0:
        time.sleep(1)
        print(f"\n[!] Toxina já está ativa por mais {toxina_ativa} turnos.")
        return toxina_ativa
    time.sleep(1)
    print("\nVocê avança e lança um líquido verde no inimigo.")
    time.sleep(1)
    print("[*] TOXINA ATIVA — 3 de dano por 5 turnos!")
    return 5

# -------- NETRUNNER --------
def usar_viral(viral_ativo):
    if viral_ativo:
        time.sleep(1)
        print("\n[!] Software Viral já está ativo.")
        return viral_ativo
    time.sleep(1)
    print("\nVocê transmite um vírus nos sistemas do inimigo.")
    time.sleep(1)
    print("[*] SOFTWARE VIRAL — Inimigo vai se atacar no próximo turno!")
    return True
#sistema de esquivas
def tentar_esquiva(agil):
    chance = min(agil * 0.04, 0.30)  # 4% por ponto, máximo 30%
    return random.random() < chance

# --------- Sorteio de inimigos --------------
def sorteio_inimigo(lvl):
    fracos = [["Ladrão", 1, 15, 1, 2], ["Nomade", 1, 20, 2, 1], ["Robô", 3, 30, 3, 1]]
    rua =    [["Ghostwire", 5, 35, 4, 2], ["Cyberpsicopata", 5, 45, 7, 3], ["Sucateiro", 2, 25, 5, 1]]
    omni =   [["Drone Omnicorp", 2, 40, 10, 2], ["Agente Omnicorp", 3, 55, 12, 3], ["Pacificador Omnicorp", 6, 70, 14, 2]]
    merc =   [["Soldado M.E.R.C.", 2, 50, 12, 2], ["General M.E.R.C.", 3, 65, 14, 2], ["Exterminador M.E.R.C.", 4, 80, 16, 2]]

    if lvl < 5:
        return random.choice(fracos)
    elif lvl < 10:
        return random.choice(rua)
    else:
        return random.choice(omni + merc)
       
#------- Sistema de combate unificado em dados ---------

def ataque(atacante_nome, atacante_forca, defensor_nome, defensor_forca, crit_classe):
    #Calcula o dano baseado em força e sorte.
    atacante_sorte = random.randint(1, 10)
    defensor_sorte = random.randint(1, 10)

    critico = atacante_sorte >= crit_classe
    mitigar = defensor_sorte == 10
    
    dano = max(1, atacante_forca + atacante_sorte - defensor_forca )# dano só vai até 1, para não ter dano 0 sem aviso
    
    #aplicação de efeitos
    if mitigar:
        dano = int(dano // 2)
        dano = max(1, dano)
        dano = int(dano)
    if critico:
        dano *= 2

    if atacante_sorte > 0:
        time.sleep(1)
        print(f"{atacante_nome} atacou")
   
    if critico:
        time.sleep(1)
        print(f"{atacante_nome} acertou um crítico")
    
    if mitigar:
        time.sleep(1)
        print(f"{defensor_nome} usou suas habilidades para diminuir o dano")
    return dano, atacante_sorte, critico

#sistema de combo
def tentar_combo(chance):
    return random.random() < chance

#sistema de uso de itens
def usar_item(jogador_inventario, jogador_hp, hp_maximo, cura_bonus=0):
    hack_ativado = False
    if not jogador_inventario:
        time.sleep(1)
        print("\n[!] Inventário vazio.")
        return jogador_hp, False

    print(f"\n--- INVENTÁRIO ---")
    time.sleep(1)
    for index, item in enumerate(jogador_inventario):
        print(f"{index + 1}. {item}")

    try:
        escolha = int(input("\nEscolha o item (0 para voltar): "))
        if escolha == 0:
            time.sleep(1)
            return jogador_hp, False

        item_escolhido = jogador_inventario[escolha - 1]

        if "Estimulante" in item_escolhido:
            cura = 5 + cura_bonus  # BioHacker cura 8, outros curam 5
            jogador_hp = min(hp_maximo, jogador_hp + cura)
            time.sleep(1)
            print(f"[*] Você injetou {item_escolhido}. HP atual: {jogador_hp}")
            jogador_inventario.pop(escolha - 1)

        elif "Hack Chip" in item_escolhido:
            time.sleep(1)
            print("[*] Hack Chip ativado! Próximo ataque do inimigo será anulado.")
            jogador_inventario.pop(escolha - 1)
            hack_ativado = True


    except (ValueError, IndexError):
        time.sleep(1)
        print("[!] Opção inválida.")

    return jogador_hp, hack_ativado

#Sistema de drop de itens
def obter_kit():
        chance = random.random()
        if chance <= 0.4:
            time.sleep(1)
            print("Você obteve Estimulante")
            return "Estimulante"
        else:
            return None


                                        # ---------- Sistema de progressão -------------
def calculo_lvl(lvl, exp, hp, hp_max, forca, exp_inimigo):
    global ato
    exp += exp_inimigo
    exp_necessaria = 20 * lvl
   

    if exp >= exp_necessaria:
        lvl += 1
        hp_max += 5
        hp = hp_max
        forca += 1
        print(f"Você subiu para o nível {lvl}!")
        time.sleep(1)
        print("+5 HP max | + 1 Força")

        if lvl == 2:
            time.sleep(1)
            print("\n>>> Os rumores se espalharam. Mais caçadores estão vindo. <<<")
        elif lvl == 3:
            time.sleep(1)
            print("\n>>> Seu nome já circula no mercado negro. A recompensa aumentou. <<<")
        elif lvl == 4:
            time.sleep(1)
            print("\n>>> Você começa a recuperar fragmentos. Flashes. Rostos que não reconhece. <<<")

    if lvl == 5 and ato == 1:
        evento_raka()
        time.sleep(1)
        print("\n>>> DIRETIVA: Chegue ao nível 10 para encontrar o Setor 7. <<<")

    if lvl == 10 and ato == 1:
         ato = 2
         evento_setor7()
         time.sleep(1)
         print("\n>>> DIRETIVA: Elimine os agentes da Omnicorp e chegue ao nível 15. <<<")


    return lvl, exp, hp, hp_max, forca




# ==========================================
#EXECUÇÃO DO JOGO (PARTE FINAL)
# ==========================================

# 1. ---------Título e Criação-------
print(artes.logo)
#titulo()

    

nome_player, lvl, exp, status = iniciar_jogo()

# 2. ----------classes-------- 
clas = classe() 

# -------------- Seleção de classe --------
hp, hp_max, forca, agil, inventario, chance_combo, cura_bonus, crit_classe = aplicar_classe(clas)
# Controle de habilidades e efeitos
zandatsu_disponivel = clas == "1"
zandatsu_ativo = False
amolador_ativo = 0
seringa_criticos = 0        
toxina_ativa = 0            
viral_ativo = False         
hack_ativo = False
chance_combo_base = chance_combo 
#3.-------------- História -------------
ato = 1
raka_ativa = False
zona_beta = comeco_historia() 
#4-------------COMBATE------------------
jogador_enfrentando_inimigo = False

while True:
    if not jogador_enfrentando_inimigo:
        if lvl >= 15 and not raka_ativa:
            evento_raka_chefe()
            raka_ativa = True
            raka_hp = 200

        if raka_ativa:
            inimigo_nome = "RAKA"
            inimigo_forca = 20
            inimigo_agil = 6
            inimigo_hp = raka_hp
            inimigo_lvl = 16
            inimigo_exp_valor = 0
        else:
            inimigo_sorteado = sorteio_inimigo(lvl)
            inimigo_nome = inimigo_sorteado[0]
            inimigo_lvl = inimigo_sorteado[1]
            inimigo_hp = inimigo_sorteado[2]
            inimigo_forca = inimigo_sorteado[3]
            inimigo_agil = inimigo_sorteado[4]
            inimigo_exp_valor = inimigo_lvl * 20

        jogador_enfrentando_inimigo = True 
        inimigo_hp_salvo = inimigo_hp
        hp_salvo = hp
        forca_salva = forca
        inventario_salvo = inventario.copy()
        time.sleep(1)
        print(f"\n[!] {inimigo_nome} aparece!")
        time.sleep(1)

    print(f"\n--- {nome_player} vs {inimigo_nome} ---")
    time.sleep(1)
    print(f"Seu HP: {hp} | HP do Inimigo: {inimigo_hp}")
   
    time.sleep(1)
    print("1. Atacar | 2. Usar item | 3. Habilidades | 4. Status. | 5. Sair")
    
    try:
        time.sleep(1)
        opcao = int(input("Escolha sua ação: "))
    except ValueError:
        time.sleep(1)
        print("Digite um número válido!")
        continue

    max_combos = 3
    combos_feitos = 0

    if opcao == 1:
        time.sleep(1)
        print("-------- SUA VEZ --------")
        #habilidade amolador
        forca_atual = forca + (3 if amolador_ativo > 0 else 0)
    
    # aplica seringa 
        if seringa_criticos > 0:
            crit_classe_atual = 1  # sempre crítico
            seringa_criticos -= 1
        else:
            crit_classe_atual = crit_classe
        if tentar_esquiva(inimigo_agil):
            time.sleep(1)
            print(f"{inimigo_nome} esquivou do seu ataque!")
        else:
            dano_p, dado_p, critico = ataque(nome_player, forca_atual, inimigo_nome, inimigo_forca, crit_classe_atual)
            if zandatsu_ativo and critico:  # crítico aconteceu
                time.sleep(1)
                print("\nO tempo congela.")
                time.sleep(1)
                print("Você avança em câmera lenta, fatiando o inimigo quantas vezes quiser.")
                time.sleep(1)
                print(f"[ZANDATSU] {nome_player} fatia {inimigo_nome} em pedaços!")
                inimigo_hp = 0
                zandatsu_ativo = False
            else:
                if dano_p > 0:
                    time.sleep(1)
                    print(f"{nome_player} causou {dano_p} de dano!")
                    inimigo_hp -= dano_p
                    if raka_ativa:
                        raka_hp = inimigo_hp

            if dano_p > 0 and combos_feitos < max_combos and tentar_combo(chance_combo):
                combos_feitos += 1
                time.sleep(1)
                print(f"ATAQUE EXTRA! (Combo x{combos_feitos})")
                chance_combo *= 0.7
                if inimigo_hp <= 0:
                    if raka_ativa:
                        evento_final()
                        break
                    else:
                        time.sleep(1)
                        print(f"O {inimigo_nome} foi destruído no combo!")
                        jogador_enfrentando_inimigo = False
                        item_dropado = obter_kit()
                        if item_dropado:
                            inventario.append(item_dropado)
                        lvl, exp, hp, hp_max, forca = calculo_lvl(lvl, exp, hp, hp_max, forca, inimigo_exp_valor)
                        continue
                opcao = 1
                continue

        if inimigo_hp <= 0:
            time.sleep(1)
            print(f"O {inimigo_nome} foi destruído!")
            if raka_ativa:
                evento_final()
                break
            else:
                jogador_enfrentando_inimigo = False
                time.sleep(1)
                chance_combo = chance_combo_base
                zandatsu_disponivel = clas == "1"
                zandatsu_ativo = False
                amolador_ativo = 0
                seringa_criticos = 0
                toxina_ativa = 0
                viral_ativo = False 
                hack_ativo = False
                item_dropado = obter_kit()
                if item_dropado:
                    inventario.append(item_dropado)

                lvl, exp, hp, hp_max, forca = calculo_lvl(lvl, exp, hp, hp_max, forca, inimigo_exp_valor)
                continue
        else:
                time.sleep(1)
                print(f"-------- VEZ DO {inimigo_nome} --------")
                # Toxina
                if toxina_ativa > 0:
                    time.sleep(1)
                    print(f"[*] Toxina causa 3 de dano em {inimigo_nome}!")
                    inimigo_hp -= 3
                    toxina_ativa -= 1
                    if raka_ativa:
                        raka_hp = inimigo_hp

                if viral_ativo:
                    print(f"[*] {inimigo_nome} está sob controle do vírus e se ataca!")
                    dano_viral, _, _ = ataque(inimigo_nome, inimigo_forca, inimigo_nome, inimigo_forca, 10)
                    inimigo_hp -= dano_viral
                    time.sleep(1)
                    print(f"{inimigo_nome} causou {dano_viral} de dano em si mesmo!")
                    viral_ativo = False
                    if raka_ativa:
                        raka_hp = inimigo_hp
                    if inimigo_hp <= 0:
                        inimigo_hp = 0
                        print(f"{inimigo_nome} foi destruído!")                            
                        if raka_ativa:
                            evento_final()
                            break
                        jogador_enfrentando_inimigo = False
                        lvl, exp, hp, hp_max, forca = calculo_lvl(lvl, exp, hp, hp_max, forca, inimigo_exp_valor)
                elif not viral_ativo:
                            if hack_ativo:
                                time.sleep(1)
                                print(f"O hack chip preveu o ataque e você bloqueou o ataque de {inimigo_nome}!")
                                hack_ativo = False
                            elif tentar_esquiva(agil):
                                        time.sleep(1)
                                        print(f"{nome_player} esquivou do ataque!")
                            else:
                                dano_i, dado_i, _ = ataque(inimigo_nome, inimigo_forca, nome_player, forca // 3, 10)
                                if dano_i > 0:
                                    time.sleep(1)
                                    print(f"{inimigo_nome} causou {dano_i} de dano!")
                                    hp -= dano_i

                            if amolador_ativo > 0:
                                amolador_ativo -= 1
                                if amolador_ativo == 0:
                                    time.sleep(1)
                                    print("[*] Amolador de Plasma acabou.")
                                

                            if hp <= 0:
                                time.sleep(1)
                                print("[ERR0R] V0CÊ VIROU SUCATA!")
                                print("\n1. Tentar novamente | 2. Sair")
                                escolha = input("Escolha: ")
                                if escolha == "1":
                                        hp = hp_salvo
                                        forca = forca_salva
                                        inventario = inventario_salvo.copy()
                                        inimigo_hp = inimigo_hp_salvo
                                        jogador_enfrentando_inimigo = True
                                        continue
                                else:
                                    break
                                                            
            
                

    elif opcao == 2:    
        hp, hack_ativo = usar_item(inventario, hp, hp_max, cura_bonus)
        if hack_ativo:
            hack_ativo = True
                
    
    elif opcao == 3:
        time.sleep(1)
        print(">> MENU DE HABILIDADES <<")
        if clas == "1":
            time.sleep(1)
            print("1. Zandatsu | 2. Amolador de Plasma")
            hab = input("Escolha: ")
            if hab == "1":
                usar_zandatsu()
            elif hab == "2":
                amolador_ativo = usar_amolador(amolador_ativo)

        elif clas == "2":
            time.sleep(1)
            print("1. Seringa Overclock | 2. Toxina Experimental")
            hab = input("Escolha: ")
            if hab == "1":
                hp, seringa_criticos = usar_seringa(hp, hp_max, seringa_criticos)
            elif hab == "2":
                toxina_ativa = usar_toxina(toxina_ativa)

        elif clas == "3":
            time.sleep(1)
            print("1. Software Viral")
            hab = input("Escolha: ")
            if hab == "1":
                viral_ativo = usar_viral(viral_ativo)

    elif opcao == 4:
        time.sleep(1)
        print(f"\n>> STATUS DE {nome_player} <<")
        time.sleep(1)
        print(f"LVL: {lvl} | HP: {hp} | FORÇA: {forca} | EXP: {exp} | AGI: {agil}")
        time.sleep(1)
        print(f"INV: {inventario}")

    if opcao == 5:
            time.sleep(1)
            print("Desconectando da rede...")
            break
