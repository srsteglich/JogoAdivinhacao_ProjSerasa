import random

def jogar():
    print("-------------------------------------------------------------------------------")
    print("       Bem-vindo ao jogo de adivinhação de números, com pontuação do jogo!")  
    print("-------------------------------------------------------------------------------")    
    nivel = 0   
    ponto = 0    
    while nivel != 4:       
        print("  Qual o nível de dificuldade de tentativas? ")
        print("  1 - Fácil (20 Tentativas)")
        print("  2 - Médio (10 Tentativas)")
        print("  3 - Difícil (05 Tentativas)")
        print("  4 - Sair do Jogo")
        nivel = int(input("  Digite um número para nível de dificuldade: "))              
        if nivel == 1:
            ponto = 5
            vezes = 20                                
            break
        elif nivel == 2:
            ponto = 10
            vezes = 10                                              
            break            
        elif nivel == 3:
            ponto = 30            
            vezes = 5                                
            break
        elif nivel == 4:          
            exit(" \n  Saiu...\n")  
        else: 
           print("\n  Opção inválida....\n")  
           #continue  
        return jogar()                  
    ## print(" quanto ponto", ponto)
    print("\n  Escolha os limites do Jogo, ideal é a diferença até 50 números. ")    
    while True:    
        infer = int(input("  Digite o limite inferior: "))
        super = int(input("  Digite o limite superior: "))                          
        quant = super - infer       
        if 2 <= quant <= 9:
            ## print("estou linha 41")
            ponto = ponto + 5   
            break            
        elif 10 <= quant <= 19:
            ponto = ponto + 10                    
            break               
        elif 20 <= quant <= 29:
            ponto = ponto + 20
            break               
        elif 30 <= quant <= 39:
            ponto = ponto + 30            
            break              
        elif 40 <= quant <= 50:
            ## print("estou linha 54")
            ponto = ponto + 50            
            break               
        else:
            print("\n  Valor invalido.") 
            print("  O limite superior não pode ser menor ou igual que limite inferior....")                           
        continue                                
    ## print(" ponto2 linha 57", ponto)    
    print("\n  Os números escolhido foi",infer,"à",super,".")
    print("  E tem",vezes,"tentativas.\n")
    numCPU = random.randint(infer,super)    
    for vez in range(1, vezes + 1):
        print("\n  Tentativa número:",vez)
        plpt = int(input("  Digite o seu palpite: "))           
        if plpt < numCPU:
            print("\n  Tente um número maior!")
            ponto = ponto - 10
        elif plpt > numCPU:
            print("\n  Tente um número menor!")
            ponto = ponto - 10
        else:
            break        
    ##print("  vezes:",vezes)     
    ##print("  vez:",vez)         
    ##print("  pontuacao:",ponto)   
    if plpt == numCPU:
        print("\n  Uuuuhhhhh.... Você acertou o número ",numCPU," e foram ",vez,"vezes.")        
        print("  E a tua Pontuação do Jogo foi: ",ponto,"pontos.\n")
        if ponto >= 50:
            print("  A tua Pontuação do Jogo foi Muito Excelente!!!!! Parabéns...\n")
        else:    
            print("  A tua Pontuação do Jogo foi Bom!!!!! Parabéns...\n")            
    else:
        print("\n  Não foi desta vez.... O Número Secreto era",numCPU,".\n")
        print("  E a tua Pontuação do Jogo foi:",ponto,"pontos.\n")
        if ponto >= 5:
            print("  A tua Pontuação do Jogo foi Razoável...\n")
        else:    
            print("  A tua Pontuação do Jogo foi muito Baixo...\n")  
    resp = input("  Deseja Jogar novamente[S/N]?").upper()
    if resp == 'S':      
        jogar()
    else:    
        print("\n  Encerrado, até próxima!!!\n") 
    exit()    
        
jogar()    
    
    

