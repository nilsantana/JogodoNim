

### Função da jogada do computador
###
def computador_escolhe_jogada(pecas,maxi):
    """
Função jogada do computador
    """
    if pecas <= maxi: #Avalia se pode limpar a mesa
        jogada = pecas
    elif pecas % (maxi+1) != 0:   # Avalia se  pecas não é  múltiplo de (m+1)
        jogada = pecas % (maxi+1) # deixa  múltiplo de (m+1) para o oponente
    else:
        jogada = maxi #retira o máximo de peças disponíveis
    print ("O computador retirou %d peças "%jogada)
    print ("Agora restam %d peças no tabuleiro."%(pecas-jogada))
    print("")
    return jogada #jogada efetivada
  

### Função da jogada do usuário
###
def usuario_escolhe_jogada(pecas,maxi):
    """
Função jogada do usuário
    """
    valido = False
    while not valido:
        jogada = (input("Quantas peças você vai tirar? "))
        if not jogada.isdigit(): #Validando se valor é inteiro
            print("\nOops! Jogada inválida! Tente de novo.\n")        
        elif jogada.isdigit(): #caso seja um inteiro
            jogada = int(jogada) #variável é convertida para validação de regra de jogada
            if (jogada > maxi)or (jogada > pecas) or (jogada <=0): # validação máximo de peças, total de peças disponíveis, valor negativo
                print("\nOops! Jogada inválida! Tente de novo.\n")
                print("")
            else: 
                valido = True #jogada aceita
            
    print ("Você tirou %d peças "%jogada)
    print ("Agora restam %d peças no tabuleiro."%(pecas-jogada))
    print("")
    return jogada #jogada efetivada
  
### Função da partida
###
def partida():
    """
Função da partida
    """
    
    totalPecas = False
    limite = False
    
    while not totalPecas: #iniciando verificação do total de peças da partida para que seja um inteiro positivo
            pecas = (input("Quantas peças? "))
            if not pecas.isdigit():# se não for digitado um número inteiro positivo o usuário precisará informar novamente o total de peça
                 print("Digite apenas números inteiros positivos")
                 
            elif pecas.isdigit():
                pecas = int(pecas)
                if pecas == 0: # se o total de peças for zero é preciso informar novamente o total de peças, não faz sentido começar o jogo com zero peças
                  print("Zero não é um número positivo")
                else:
                    pecas = int(pecas)
                    totalPecas = True # validado valor total de peças como número inteiro maior que zero
    while not limite:   #iniciando verificação do limite para que seja um inteiro positivo menor qque o total das peças
            maxi = (input("Limite de peças por jogada? "))
            if not maxi.isdigit():
                 print("Digite apenas números inteiros positivos")
                 
            elif maxi.isdigit():
                maxi = int(maxi)
                if maxi == 0:
                    print("Zero não é um número positivo")
                elif (maxi > pecas): #validação de valores excedentes para limite de jogada
                    print ("Jogada invalida, digite valores do limite menor que o número de peças")  
                else:
                    maxi = int(maxi)
                    limite = True # validado valor do limite como número inteiro maior que zero
                    print("")
   
    if pecas % (maxi+1) == 0:    
        print("Você começa!\n")
        jogadaUsuario = usuario_escolhe_jogada(pecas,maxi)
        pecas = pecas - jogadaUsuario
    else:
         print("Computador começa!\n")
    while pecas > 0:
        jogadaComputador = computador_escolhe_jogada(pecas,maxi)
        pecas = pecas - jogadaComputador
        if  pecas == 0:
            print ("Fim do jogo! O computador ganhou!\n")
            resultado = 0
            break
        jogadaUsuario = usuario_escolhe_jogada(pecas,maxi)
        pecas = pecas - jogadaUsuario
        if pecas == 0:
            print ("Fim do jogo! Você ganhou!\n")
            resultado = 1
            break
    return resultado

### Função do campeonato
###
def campeonato():
    """"
funçãao campeonato 
    """
    computador = 0
    usuario = 0
    for i in range(0,3): #laço de contagem das chamadas das partidas do campeonato
        print("**** Rodada %d ****\n"%(i+1))
        placar = partida()  #chamando as partidas e recebebdo o placar do campeonato
        if placar == 1: 
                usuario = usuario +1  # somando placar do usuário
        else:
                computador = computador +1 # somando placar do computador
            
        i = i+1 # avançando as partidas
    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d X %d Computador" %(usuario,computador))
    return    

### Função do jogo
###
def jogo():
    """"
Jogo de tabuleiro nim.

Neste joogo o computador sempre ganha
    """
    valendo = False
    while not valendo: # validando se o usuário não está digitando valor diferente de inteiro
        print("Bem vindo ao jogo NIM! Escolha:\n")

        print("1 - para jogar uma partida isolada")
    
        tipo_torneio = (input("2 - para jogar um campeonato: "))
        if tipo_torneio.isdigit(): # testando se o valor recebido é um numero inteiro 
            print("")
            if tipo_torneio == "1": # testando se o valor corresponde a partida 
                print("Você escolheu uma partida! \n")
                partida() # chamada da partida
                valendo = True # se validado, sai do laço
            elif tipo_torneio == "2": # testando se o valor corresponde a campeonato 
                print("Você escolheu um campeonato! \n")
                campeonato() # chamada da partida
                valendo = True #se validado, sai do laço
            else:
                print("%s Não é uma opção válida, escolha novamente\n"%tipo_torneio)            
        else:
            print("%s Não é uma opção válida, escolha novamente\n"%tipo_torneio)         

### Chamada do jogo
###  
      
jogo()   ## Inicia o jogo
