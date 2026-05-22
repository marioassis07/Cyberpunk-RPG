import time
import random
import arts
import sys
def digitacao (texto, velocidade=0.05):#criando a sensação de escrita
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def titulo ():
    
    digitacao("Bem vindo ao Cyberpunk RPG!",0.1)
    digitacao("Você deseja viver como um zé ninguém ou morrer como uma lenda?",0.1)
    digitacao("Está pronto pra ter uma vida miserável?",0.1)
    start = input("Digite sim para começar: ")
    if start not in ["sim", "s", "Sim", "S"]:
        time.sleep(1)
        digitacao("Você não tem escolha, prepare-se para o inferno! "
        "Ass: M.E.R.C",0.05)
    time.sleep (1)

#-------- Criação de personagem -------
def iniciar_jogo ():
    digitacao("Crie sua aberração cibernética: ",0.05)
    nome_player = input("Nome do seu personagem: ")
    time.sleep(1)
    lvl = 1
    exp = 0
    status = True


    return nome_player, lvl, exp, status
#-------- História --------
#cap1
def comeco_historia():
    import arts
    digitacao("\n\033[1;37;40mVocê acorda em um ferro velho.\033[m",0.1)
    digitacao("\n\033[1;37;40mA luz do sol te cega por alguns segundos, até realmente ver uma pilha de corpos logo adiante.\033[m",0.1)
    digitacao("\n\033[1;37;40mSua arma, ao seu lado, tão cromada, que chega a ser doentio, totalmente suja de sangue.\033[m",0.1)
    if clas == "1":
        print(arts.katana)
        time.sleep(4)
    digitacao('\033[1;37;40m...\033[m',0.3)
    digitacao("\n\033[1;37;40mO MEDO TE CONSOME!!!\033[m",0.1)

    digitacao(f"\n\033[1;37;40m{nome_player}: Onde estou? Quem são essas pessoas?\033[m",0.1)

    digitacao(f"\n\033[1;37;40m{nome_player} grita: TEM ALGUEM AQUI?\033[m",0.1)

    digitacao('\033[1;37;40m...\033[m',0.3)

    digitacao("\n\033[1;37;40mVocê só escuta o barulho das maquinas da região desértica...\033[m",0.05)

    digitacao("\n\033[1;37;40mAo tentar se levantar, seus implantes rangem e saem faísca.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê cai novamente.\033[m",0.05)

    digitacao("\n\033[1;37;40mAo tentar verificar sua memória: \n [ERR0R: Fr4gmentos de memór1a corr0mpidos]\033[m",0.05)

    digitacao("\n\033[1;37;40mNão há memória. Nenhuma. Só o seu nome, gravado em algum lugar fundo.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê olha um pouco mais ao seu redor e percebe que está na Zona de Exclusão Beta\033[m",0.05)

    digitacao(arts.zona_beta,0.005)

    digitacao("\n\033[1;37;40mLocal onde a M.E.R.C. tentou implantar varios sistemas militares, mas por conta de um erro, houve uma grande detonação de bombas\033[m",0.05)

    digitacao("\n\033[1;37;40mDesde então, é apenas um local sem natureza, somente lixo, pobres e ladrões, todos buscando sobreviver.\033[m")
    digitacao("\n\033[1;37;40mDe repente, você ouve passos.\033[m",0.05)

    digitacao("\n\033[1;37;40mUma voz ao longe: \"É ele. Tá vivo. A recompensa é nossa.\033[m",0.05)

    digitacao("\n\033[1;37;40mRecompensa.\033[m",0.05)

    digitacao("\n\033[1;37;40mAlguém quer você morto... e pagou bem por isso\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê não sabe quem, nem por quê.\033[m",0.05)

    digitacao("\n\033[1;37;40mMas a resposta está lá fora — se você conseguir sobreviver até encontrá-la.\033[m",0.05)

    digitacao("\n\033[1;37;40mDo casebre ao lado, surge o primeiro deles:\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> PROTOCÓLO: Derrote os inimigos e chegue ao nível 5!!\033[m",0.05)
#cap2
def evento_raka():
    digitacao("\n\033[1;37;40m...\033[m",0.05)

    digitacao("\n\033[1;37;40mDepois de fazer uma chacina no local, você foge em direção a cidade\033[m",0.05)

    digitacao(arts.cidade,0.005)

    digitacao("\033[1;37;40mÔmega City\033[m",0.05)

    digitacao("\n\033[1;37;40mChegando na cidade, uma loja chama sua atenção. Parece bem familiar.\033[m",0.05)

    digitacao(arts.andando_cidade,0.005)

    digitacao(f"\n\033[1;37;40m{nome_player}: Esse lugar...\033[m",0.05)

    digitacao("\n\033[1;37;40mMas, enquanto tenta se lembrar, você sente uma mão te puxar pra dentro de um beco escuro.\033[m",0.05)

    digitacao("\n\033[1;37;40mUma mulher de olhos cibernéticos te encara. Ela parece te reconhecer.\033[m",0.05)

    digitacao("\n\033[1;37;40mDesconhecida: Você não devia estar vivo.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Quem é você?\033[m",0.05)

    digitacao("\n\033[1;37;40mPor algum motivo você sabe o nome dela, Syn.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Seu nome é Syn?\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: Sou quem cometeu o pior dos pecados.\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: Eu ajudei a colocar esses implantes em você. Em todos vocês.\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: O que aconteceu naquela noite no laboratório, foi um acidente. Não é culpa sua.\033[m",0.05)

    digitacao("\n\033[1;37;40mAntes que ela possa dizer algo, uma gangue chega com um carro:\033[m",0.05)

    digitacao(arts.carro,0.005)

    digitacao("\n\033[1;37;40mAo olhar pro lado, Syn desaparece e deixa uma mensagem dentro de um chip, no chão.\033[m",0.05)

    digitacao("\n\033[1;37;40mApós coloca-lo em seu slot de neurochip, uma mensagem aparece:\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> SETOR 7. SOZINHO. SE QUISER SABER QUEM VOCÊ ERA. <<<\033[m",0.05)

    digitacao("\n\033[1;37;40mPor um momento você começa a lembrar o que aconteceu naquele lugar.\033[m",0.05)

    digitacao('\n\033[1;37;40mO neurochip possuia memórias. Suas? Talvez.\033[m',0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Um protocolo? Eu fugi de algum lugar... Que lugar é esse?\033[m",0.05)

    digitacao("\n\033[1;37;40mMas, antes mesmo de você pensar, a gangue te ataca\033[m",0.05)

    digitacao('\033[1;37;40m>>> PROTOCÓLO: Derrote os inimigos e chegue ao nível 10!!\033[m',0.05)
#cap3
def evento_setor7():
    digitacao("\n\033[1;37;40m...\033[m",0.05)

    digitacao("\n\033[1;37;40mHá uma pilha de corpos na sua frente\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Melhor sair daqui, antes que a polícia apareça.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê entra na Porshe da gangue que te atacou, vasculha um pouco e acha algumas coisas.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Esse carro era de um tal de V, acho que ja ouvi falar nesse nome.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Talvez seja aquele cara que surgiu depois do David Martinez.\033[m",0.05)

    digitacao("\n\033[1;37;40mAlgumas horas depois...\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê chega ao Setor 7.\033[m",0.05)

    digitacao("\n\033[1;37;40mO lugar parece abandonado. Mas você sente que está sendo observado.\033[m",0.05)

    digitacao("\n\033[1;37;40mDrones Omnicorp surgem de todos os lados.\033[m",0.05)

    digitacao("\n\033[1;37;40mEles sabiam que você viria.\033[m",0.05)

    digitacao("\n\033[1;37;40mUma voz ecoa pelos alto-falantes do setor:\033[m",0.05)

    digitacao("\n\033[1;37;40mDesconhecido: Você deveria ter morrido no ferro velho.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Erro de vocês.\033[m",0.05)

    digitacao("\n\033[1;37;40mAo olhar o portão, você observa um simbolo...\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Omnicorpe... A maior corporação de tecnologia e implantes neurais da cidade.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}Controlam os dados de milhões. Acima da lei. Acima de tudo.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Poxa, só isso? Achei que vocês tinham toda aquela tecnologia imparável.\033[m",0.05)

    digitacao("\n\033[1;37;40mOs agentes Omnicorp param. Tem algo errado...\033[m",0.05)

    digitacao("\n\033[1;37;40mHelicópteros militares cortam o céu. Soldados descem em cordas.\033[m",0.05)

    digitacao(arts.heli,0.005)

    digitacao("\n\033[1;37;40mM.E.R.C.: Alvo confirmado. Autorização de extermínio concedida.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Quem são vocês? Era melhor eu ter ficado quieto.\033[m",0.05)

    digitacao("\n\033[1;37;40mM.E.R.C.: Corporação de Resposta e Execução Militar, fique parado onde está!\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Milícia militar privada. Sem bandeira. Sem código.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Contratados para terminar o que a Omnicorp não conseguiu.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Achei que vocês só matavam esses cyberpsicóticos por aí. Eu tava só de passagem.\033[m",0.05)

    digitacao("\n\033[1;37;40mEquipe de exterminio: Bravo, aqui é Delta, alvo na mira.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Melhor eu correr...\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> DIRETIVA: Elimine os agentes da Omnicorp e da M.E.R.C. e chegue ao nível 15. <<<\033[m",0.05)
#boss fight
def evento_raka_chefe():
    digitacao("\n\033[1;37;40m...\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Achei que vocês fossem melhores\033[m",0.05)

    digitacao("\n\033[1;37;40mUm soldado ainda estava vivo, implorando pela sua vida.\033[m",0.05)

    digitacao("\n\033[1;37;40mAo chegar perto, ele fala:\033[m",0.05)

    digitacao("\n\033[1;37;40mSoldado M.E.R.C.: Você acabou com a minha família, por que você tinha que fugir do laboratório!?\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Laboratório? Do que você está falando?\033[m",0.05)

    digitacao("\n\033[1;37;40mSoldado M.E.R.C.: Não se faça de idiota, seu lixo de experimento\033[m",0.05)

    digitacao("\n\033[1;37;40mSoldado M.E.R.C.: Vai fingir que não lembra de toda destruição que causou no Laboratório 312!?\033[m",0.05)

    digitacao("\n\033[1;37;40mSoldado M.E.R.C.: Minha esposa estava no meio dos cientistas, você também a matou, seu psicopata!\033[m",0.05)

    digitacao("\n\033[1;37;40mSoldado M.E.R.C.: Eles deviam ter deixado você morrer com todo esse cromo no seu corpo\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê fica totalmente abalado com o que ouviu e antes mesmo do soldado terminar, você o executa.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: Eu nunca faria algo assim... O que eu sou? Quem sou eu?\033[m",0.05)

    digitacao("\n\033[1;37;40mAo entrar no centro do Setor 7, você encontra o terminal que enviou a mensagem.\033[m",0.05)

    digitacao(arts.terminal,0.005)

    digitacao("\n\033[1;37;40mAo acessá-lo, arquivos começam a aparecer.\033[m",0.05)

    digitacao("\n\033[1;37;40mFotos... Relatórios... Experimentos....\033[m",0.05)

    digitacao("\n\033[1;37;40mTodos com o seu rosto.\033[m",0.05)

    digitacao("\n\033[1;37;40mUm arquivo de voz. Sua própria voz.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player} (gravação): Se você está ouvindo isso... funcionou.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player} (gravação): Não confie em ninguém que sobreviveu àquela noite além de você.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê ouve passos atrás de você.\033[m",0.05)

    digitacao("\n\033[1;37;40mAo se virar:\033[m",0.05)

    digitacao(arts.Syn,0.005)

    digitacao("\n\033[1;37;40mSyn: Demorou mais do que eu esperava pra você chegar aqui.\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}: O que é tudo isso!? Quem é você?\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: O que importa é o que você é.\033[m",0.05)

    digitacao("\n\033[1;37;40mSy: O primeiro a fugir, você era o mais forte dos cyberpsicóticos.\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: Então tentamos revive-lo, para trabalhar para a Omnicorp, mas deu tudo errado.\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn: Você foi executado uma vez, então eu estou aqui para fazer isso de novo.\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> Syn - A pecadora <<<\033[m",0.05)

    digitacao("\033[1;37;40m>>> HP: 200 | FORÇA: 20 | AGILIDADE: 16 <<<",0.05)
#fim de jogo
def evento_final():
    digitacao("\n\033[1;37;40m...\033[m",0.05)

    digitacao("\n\033[1;37;40mSyn cai\033[m",0.05)

    digitacao("\n\033[1;37;40mO terminal começa a piscar. Uma contagem regressiva.\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> AUTODESTRUIÇÃO INICIADA — 60 SEGUNDOS <<<\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player} corre.\033[m",0.05)

    digitacao("\n\033[1;37;40mAs paredes do Setor 7 colapsam atrás de você.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê escapa.\033[m",0.05)

    digitacao("\n\033[1;37;40m...\033[m",0.05)

    digitacao("\n\033[1;37;40mNa sua mão, um último arquivo do terminal.\033[m",0.05)

    digitacao("\n\033[1;37;40mVocê abre.\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> PROJETO LAZARUS — STATUS: ENCERRADO <<<\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> SOBREVIVENTES CONFIRMADOS: 1 <<<\033[m",0.05)

    digitacao(f"\n\033[1;37;40m{nome_player}.\033[m",0.05)

    digitacao("\n\033[1;37;40mPor enquanto.\033[m",0.05)

    digitacao("\n \033[1;37;40mVocê descansa em frente ao por do sol...\033[m",0.05)

    digitacao(arts.sol,0.005)

    digitacao("\n\033[1;37;40mAté o seu fim...\033[m",0.05)

    digitacao("\n\033[1;37;40m>>> FIM DE JOGO <<<\033[m",0.05)

    digitacao("\033[1;37;40mFeito por: Mário de Assis, Kauã Cabral\033[m",0.05)

    digitacao("\033[1;37;40mArtes de: asciiart.eu\033[m",0.05)

#-------Criar classe -------
def classe ():
    digitacao("Escolha sua classe:",0.1)
    digitacao("\n\033[36m1- Cyber Samurai: + 2 força, 20 HP + 2 agilidade .\033[m",0.05)#classe

    digitacao("\033[31mHabilidades: Zandatsu, Amolador de plasma\033[m",0.05)#habilidades

    digitacao("\n\033[36m2- BioHacker:  25 HP, + 8 cura extra, + 3 estimulantes.\033[m",0.05)

    digitacao("\033[31mHablidades: Seringa de adrenalina Overclock, Toxina experimental.\033[m",0.05)

    digitacao("\n\033[36m3- Netrunner: + 1 força, 15 HP + 4 agilidade\033[m",0.05)

    digitacao("\033[31mHabilidades:Software de Transmissão Viral, Chip de hack.\033[m",0.05)
    while True: 
        clas = input(f"Qual será a classe de {nome_player} ? ")
        if clas == "1":
            digitacao("Um guerreiro das ruas que trocou a honra pelo cromo.  Usa uma Katana Cromada de alta frequência, para cortar qualquer coisa",0.05)

            digitacao("Descrição de habilidades: \n\033[31mZandatsu: Capacidade de parar o tempo e fatiar o inimigo quantas vezes quiser.\033[m",0.05)

            digitacao("\033[31mCausa morte instantânea no próximo crítico.\033[m",0.05)

            digitacao("\n\033[31mAmolador de plasma: Amolador avançado, reconstrói totalmente o fio da espada.\033[m",0.05)

            digitacao("\033[31m+ 3 de força por 5 turnos.\033[m",0.05)
            break
        elif clas == "2":
            digitacao("Metade humano, metade laboratório ambulante. Hackeou o próprio corpo e sabe exatamente onde uma bala de 9mm dói mais.\nCarrega Kit Médico porque sempre precisa se remendar depois.",0.05)

            digitacao("Descrição de habilidades: \n\033[33mSeringa Overclock: Seringa de alta capacidade elétrica, fortalece os neurônios em 200%, fazendo o usuário enxergar os pontos vitais do inimigo.\033[m",0.05)

            digitacao("\033[33m+ 15 HP e crítico nos próximos 2 turnos.\033[m",0.05)

            digitacao("\n\033[33mToxina experimental: \nToxina inventada em laboratório próprio, faz todo o cromo inimigo corroer apenas ao entrar em contato.\033[m",0.05)

            digitacao("\033[33mCausa 3 de dano por 5 turnos.\033[m",0.05)
            break
        elif clas == "3":
            digitacao("Vive na borda entre o mundo real e a rede. Antes de você puxar o gatilho, ele já travou seus implantes. Usa uma Pistola Furtiva e Hack Chips pra deixar você nu no sistema.", 0.05)

            digitacao("Descrição de habilidades: \n\033[34mSoftware de Transmissão Viral: Hack que infecta o sistema neural do inimigo, o fazendo atacar a sí.\033[m", 0.05)

            digitacao("\033[34mO inimigo causa dano em sí no próximo turno.\033[m", 0.05)

            digitacao("\033[34mChip de hack: Implante neural que possibilita a leitura do próximo ataque inimigo.\033[m", 0.05)

            digitacao("\033[34mDefende o próximo ataque inimigo.\033[m", 0.05)
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
    global zandatsu_disponivel, zandatsu_ativo #permite que uma variavel seja modificada dentro dessa função
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
        print(f"\n[!] Seringa já está ativa por mais {seringa_criticos} ataques.") # faz com que a seringa só ative 1 vez
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
    print("\nVocê avança e lança um líquido no inimigo, fazendo seus implantes derreterem!")
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
    chance = min(agil * 0.04, 0.30)  # a chance da esquiva aumenta 4% por ponto de agilidade, máximo 30%
    return random.random() < chance

# --------- Sorteio de inimigos --------------
def sorteio_inimigo(lvl):
    fracos = [["Ladrão", 1, 15, 1, 2], ["Nomade", 1, 20, 2, 1], ["Robô", 3, 30, 3, 1]] #inimigos cap1
    rua =    [["Ghostwire", 5, 35, 4, 2], ["Cyberpsicopata", 5, 45, 7, 3], ["Sucateiro", 2, 25, 5, 1]]#inimigos cap 2
    omni =   [["Drone Omnicorp", 2, 40, 10, 2], ["Agente Omnicorp", 3, 55, 12, 3], ["Pacificador Omnicorp", 6, 70, 14, 2]]#inimigos cap 3
    merc =   [["Soldado M.E.R.C.", 2, 50, 12, 2], ["General M.E.R.C.", 3, 65, 14, 2], ["Exterminador M.E.R.C.", 4, 80, 16, 2]]#inimigos cap3

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

    critico = atacante_sorte >= crit_classe #o crítico será contabilizado se o dado for maior ou igual os pontos de critico
    mitigar = defensor_sorte == 10 # se o defensor atigir o dado 10, o dano vai ser diminuido
    
    dano = max(1, atacante_forca + atacante_sorte - defensor_forca )# dano só vai até 1, para não ter dano 0 sem aviso
    
    #aplicação de efeitos
    if mitigar:
        dano = int(dano // 2)
        dano = max(1, dano)
        dano = int(dano) #diminui o dano na metade, com minimo 1 de dano
    if critico:
        dano *= 2 #critico causa dobro de dano

    if atacante_sorte > 0:
        time.sleep(1)
        print(f"{atacante_nome} atacou")
   
    if critico:
        time.sleep(1)
        print(f"{atacante_nome} \033[31macertou um crítico\033[m")
    
    if mitigar:
        time.sleep(1)
        print(f"{defensor_nome} \033[34musou suas habilidades para diminuir o dano\033[m")
    return dano, atacante_sorte, critico

#sistema de combo
def tentar_combo(chance):
    return random.random() < chance

#sistema de uso de itens
def usar_item(jogador_inventario, jogador_hp, hp_maximo, cura_bonus=0):
    hack_ativado = False
    if not jogador_inventario: # se não tiver itens no inventario aparecerá a mensagem
        time.sleep(1)
        print("\n[!] Inventário vazio.")
        return jogador_hp, False

    print(f"\n--- INVENTÁRIO ---")
    time.sleep(1)
    for index, item in enumerate(jogador_inventario):
        print(f"{index + 1}. {item}") # vai numerar os itens no inventario

    try:
        escolha = int(input("\nEscolha o item (0 para voltar): "))
        if escolha == 0:
            time.sleep(1)
            return jogador_hp, False

        item_escolhido = jogador_inventario[escolha - 1]

        if "Estimulante" in item_escolhido:
            cura = 5 + cura_bonus  # BioHacker cura 8, outros curam 5
            jogador_hp = min(hp_maximo, jogador_hp + cura) #soma a vida atual com a cura e não passa do maximo de hp
            time.sleep(1)
            print(f"\033[36m[*] Você injetou {item_escolhido}\033[m. \033[36mHP atual: {jogador_hp}\033[m")
            jogador_inventario.pop(escolha - 1)

        elif "Hack Chip" in item_escolhido:
            time.sleep(1)
            print("\033[33m[*] Hack Chip ativado! Próximo ataque do inimigo será anulado.\033[m")
            jogador_inventario.pop(escolha - 1)
            hack_ativado = True


    except (ValueError, IndexError):
        time.sleep(1)
        print("[!] Opção inválida.") # se o jogador escrever o numero errado vai dar mensagem de erro, evitando a quebra do jogo

    return jogador_hp, hack_ativado

#Sistema de drop de itens
def obter_kit():
        chance = random.random() # drop de cura
        if chance <= 0.40: 
            time.sleep(1)
            print("Você obteve Estimulante")
            return "Estimulante"
        else:
            return None


                                        # ---------- Sistema de progressão -------------
def calculo_lvl(lvl, exp, hp, hp_max, forca, exp_inimigo):
    global ato
    exp += exp_inimigo
    exp_necessaria = 20 * lvl # faz com que o nível suba a cada luta
   

    if exp >= exp_necessaria:
        lvl += 1
        hp_max += 5
        hp = hp_max
        forca += 1
        digitacao(f"Você subiu para o nível \033[36m{lvl}!\033[m",0.05)

        digitacao("\033[32m+5 HP max\033[m | \033[31m+ 1 Força\033[m",0.05)

        if lvl == 2:

            digitacao("\n\033[1;37;40m>>> Os rumores se espalharam. Mais caçadores estão vindo. <<<\033[m",0.05)
        elif lvl == 3:

            digitacao("\n\033[1;37;40m>>> Seu nome já circula no mercado negro. A recompensa aumentou. <<<\033[m",0.05)
        elif lvl == 4:

            digitacao("\n>>>\033[1;37;40m Você começa a recuperar fragmentos. Flashes. Rostos que não reconhece. <<<\033[m",0.05)
    if lvl == 5 and ato == 1:
        evento_raka()
        digitacao("\n>>>\033[1;37;40m DIRETIVA: Chegue ao nível 10 para encontrar o Setor 7. <<<\033[m",0.05)

    if lvl == 10 and ato == 1:
         ato = 2
         evento_setor7()
         digitacao("\n>>>\033[1;37;40m DIRETIVA: Elimine os agentes da Omnicorp e chegue ao nível 15. <<<\033[m",0.05)

    
    return lvl, exp, hp, hp_max, forca




# ==========================================
#EXECUÇÃO DO JOGO (PARTE FINAL)
# ==========================================

# 1. ---------Título e Criação-------
print(arts.logo) # traz os dados de outro arquivo e printa
titulo()

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
hack_ativo = False #tudo é falso pq o combate precisa iniciar sem nenhum efeito
chance_combo_base = chance_combo 
#3.-------------- História -------------
ato = 1
raka_ativa = False # o boss sempre está aqui, mas desativado
zona_beta = comeco_historia() 
#4-------------COMBATE------------------
jogador_enfrentando_inimigo = False #inicio do loop de combate, está false pois não há inimigo

while True:
    if not jogador_enfrentando_inimigo:
        if lvl >= 15 and not raka_ativa: #se o jogador chegar ao level 15, o boss será ativado
            evento_raka_chefe()
            raka_ativa = True
            raka_hp = 200

        if raka_ativa: # status do boss
            inimigo_nome = "Syn"
            inimigo_forca = 20
            inimigo_agil = 6
            inimigo_hp = raka_hp
            inimigo_lvl = 16
            inimigo_exp_valor = 0
        else:
            inimigo_sorteado = sorteio_inimigo(lvl) #se não for o boss, o sorteio funcionará normalmente com os inimigos
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
        inventario_salvo = inventario.copy() #salva o inventario no inicio de todo combate, para o tente novamente
        time.sleep(1)
        digitacao(f"\n[!] {inimigo_nome} aparece!",0.05)

    print(f"\n\033[36m--- {nome_player} vs {inimigo_nome} ---\033[m")
    time.sleep(1)
    print(f"\033[32mSeu HP: {hp}\033[m | \033[31mHP do Inimigo: {inimigo_hp}\033[m")
   
    time.sleep(1)
    print("\033[31m1. Atacar\033[m | \033[36m2. Usar item \033[m| \033[36m3. Habilidades\033[m | \033[36m4. Status.\033[m | \033[36m5. Sair\033[m")
    
    try:
        time.sleep(1)
        opcao = int(input("\033[36mEscolha sua ação: \033[m"))
    except ValueError:
        time.sleep(1)
        print("Digite um número válido!")
        continue

    max_combos = 3 # o combo só pode ser feito 3 vezes seguidas
    combos_feitos = 0

    if opcao == 1:
        time.sleep(1)
        print("-------- SUA VEZ --------")
        #habilidade amolador
        forca_atual = forca + (3 if amolador_ativo > 0 else 0) # cmais 3 de força
    
    # aplica seringa 
        if seringa_criticos > 0:
            crit_classe_atual = 1  # sempre crítico
            seringa_criticos -= 1 # diminui a quantidade de criticos restantes
        else:
            crit_classe_atual = crit_classe # quando acaba, o critico volta ao normal
        if tentar_esquiva(inimigo_agil):
            time.sleep(1)
            print(f"{inimigo_nome} esquivou do seu ataque!")
        else:
            dano_p, dado_p, critico = ataque(nome_player, forca_atual, inimigo_nome, inimigo_forca, crit_classe_atual)
            if zandatsu_ativo and critico:  # crítico aconteceu e o zandatsu está ativo
                digitacao("\n\033[34mO tempo congela.\033[m",0.2)
                digitacao("\033[34mVocê avança em câmera lenta\033[m, \033[34mfatiando o inimigo quantas vezes quiser..\033[m",0.1)
                digitacao(f"\033[33m[ZANDATSU] {nome_player} fatia {inimigo_nome} em pedaços!.\033[m",0.05)
                inimigo_hp = 0
                zandatsu_ativo = False
            else:
                if dano_p > 0:
                    time.sleep(1)
                    print(f"{nome_player} causou \033[31m{dano_p} de dano!\033[m")
                    inimigo_hp -= dano_p
                    if raka_ativa:
                        raka_hp = inimigo_hp

            if dano_p > 0 and combos_feitos < max_combos and tentar_combo(chance_combo):
                combos_feitos += 1
                time.sleep(1)
                print(f"\033[33mATAQUE EXTRA! (Combo x{combos_feitos})\033[m")
                chance_combo *= 0.7 
                if inimigo_hp <= 0:
                    if raka_ativa:#quebra o combro se o jogo chegar ao final
                        evento_final()
                        break
                    else:
                        time.sleep(1)
                        print(f"\033[33mO {inimigo_nome} foi destruído no combo!\033[m") # quebra o combo se o inimigo morrer com combo ativo
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
            print(f"\033[33m{inimigo_nome} foi destruído!\033[m") # descontinua o combate e volta pro loop
            if raka_ativa:
                evento_final()
                break # se for o boss vai quebrar o loop de combate e partir para o fim do jogo
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
                    inventario.append(item_dropado) # todo esse bloco vai resetar os dados ao terminar cada combate e depois volta ao loop

                lvl, exp, hp, hp_max, forca = calculo_lvl(lvl, exp, hp, hp_max, forca, inimigo_exp_valor)
                continue
        else:
                time.sleep(1)
                print(f"-------- VEZ DE {inimigo_nome} --------") # se o inimigo não morrer, vai continuar o loop de combate para o inimigo
                # Toxina
                if toxina_ativa > 0:
                    time.sleep(1)
                    print(f"[*] \033[32mToxina\033[m \033[32mcausa 3 de dano em {inimigo_nome}!\033[m")
                    inimigo_hp -= 3
                    toxina_ativa -= 1
                    if raka_ativa:
                        raka_hp = inimigo_hp

                if viral_ativo:
                    print(f"\033[33m[*] {inimigo_nome} está sob controle do vírus e se ataca!\033[m")
                    dano_viral, _, _ = ataque(inimigo_nome, inimigo_forca, inimigo_nome, inimigo_forca, 10) # o dano do inimigo vai ser aplicado nele mesmo, inves do jogador
                    inimigo_hp -= dano_viral
                    time.sleep(1)
                    print(f"\033[33m {inimigo_nome}\033[m \033[33mcausou {dano_viral} de dano em si mesmo!\033[m")
                    viral_ativo = False
                    if raka_ativa:
                        raka_hp = inimigo_hp
                    if inimigo_hp <= 0:
                        inimigo_hp = 0
                        print(f"\033[33m {inimigo_nome} foi destruído!\033[m")                            
                        if raka_ativa:
                            evento_final()
                            break
                        jogador_enfrentando_inimigo = False
                        lvl, exp, hp, hp_max, forca = calculo_lvl(lvl, exp, hp, hp_max, forca, inimigo_exp_valor)
                elif not viral_ativo:
                            if hack_ativo:
                                time.sleep(1)
                                print(f"\033[33mO hack chip preveu o ataque e você bloqueou o ataque de\033[m \033[33m{inimigo_nome}!\033[m")
                                hack_ativo = False
                            elif tentar_esquiva(agil):
                                        time.sleep(1)
                                        print(f"{nome_player} \033[mesquivou do ataque!\033[m")
                            else:
                                dano_i, dado_i, _ = ataque(inimigo_nome, inimigo_forca, nome_player, forca // 3, 10) # quanto menos defesa, mais dano passa, por isso a força é //3
                                if dano_i > 0:
                                    time.sleep(1)
                                    print(f"\033[31m{inimigo_nome}\033[m \033[31mcausou {dano_i} de dano!\033[m")
                                    hp -= dano_i

                            if amolador_ativo > 0:
                                amolador_ativo -= 1
                                if amolador_ativo == 0:
                                    time.sleep(1)
                                    print("\033[37m[*] Amolador de Plasma acabou.\033[m")
                                

                            if hp <= 0:
                                time.sleep(1)
                                print("\033[1;31;40m[ERR0R] V0CÊ VIROU SUCATA!\033[m")
                                print("\n\033[36m1. Tentar novamente\033[m |\033[36m 2. Sair\033[m")
                                escolha = input("Escolha: ")
                                
                                if escolha == "1":
                                        hp = hp_salvo
                                        forca = forca_salva
                                        inventario = inventario_salvo.copy()
                                        inimigo_hp = inimigo_hp_salvo
                                        jogador_enfrentando_inimigo = True
                                      
                                else:
                                    break
                                                            
            
                

    elif opcao == 2:    # menu inventario
        hp, hack_ativo = usar_item(inventario, hp, hp_max, cura_bonus)
        if hack_ativo:
            hack_ativo = True
                
    
    elif opcao == 3: # menu de habilidades
        time.sleep(1)
        print("\033[33m>> MENU DE HABILIDADES <<\033[m")
        if clas == "1":
            time.sleep(1)
            print("\033[33m1. Zandatsu \033[m|\033[33m 2. Amolador de Plasma\033[m")
            hab = input("Escolha: ")
            if hab == "1":
                usar_zandatsu()
            elif hab == "2":
                amolador_ativo = usar_amolador(amolador_ativo)

        elif clas == "2":
            time.sleep(1)
            print("\033[33m1. Seringa Overclock \033[m|\033[33m 2. Toxina Experimental\033[m")
            hab = input("Escolha: ")
            if hab == "1":
                hp, seringa_criticos = usar_seringa(hp, hp_max, seringa_criticos)
            elif hab == "2":
                toxina_ativa = usar_toxina(toxina_ativa)

        elif clas == "3":
            time.sleep(1)
            print("\033[33m1. Software Viral\033[m")
            hab = input("Escolha: ")
            if hab == "1":
                viral_ativo = usar_viral(viral_ativo)

    elif opcao == 4:
        time.sleep(1) # status do personagem
        print(f"\n\033[36m>> STATUS DE {nome_player} <<\033[m")
        time.sleep(1)
        print(f"\033[36mLVL: {lvl}\033[m | \033[36mHP: {hp} \033[m| \033[36mFORÇA: {forca}\033[m | \033[36mLVL: {lvl} \033[m| \033[36m AGI: {agil}\033[m")
        time.sleep(1)
        print(f"\033[36mINV: {inventario}\033[m")

    if opcao == 5: # sai do jogo
            time.sleep(1)
            print("\033[36mDesconectando da rede...\033[m")
            break