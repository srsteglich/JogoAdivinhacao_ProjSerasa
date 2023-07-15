
import os
import random
import time

def jogar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;30;46m     PROCESSANDO!!!....\033[m1️⃣')
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('\033[1;30;46m     PROCESSANDO!!!....\033[m2️⃣')
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('\033[1;30;46m     PROCESSANDO!!!....\033[m3️⃣')
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;34m-------------------------------------------------------------------------------")
    print("       Bem-vindo ao jogo de adivinhação de números, com pontuação do jogo!")  
    print("-------------------------------------------------------------------------------\033[m")    
    nivel = 0   
    ponto = 0    
    while nivel != 4:       
        print("  Qual o nível de dificuldade de tentativas? ")
        print("  1 - Fácil (20 Tentativas)")
        print("  2 - Médio (10 Tentativas)")
        print("  3 - Difícil (05 Tentativas)")
        print("  4 - Sair do Jogo")
        nivel = input("  Digite um número para nível de dificuldade: ")
        if nivel.isdigit():
            nivel = int(nivel)        
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
                print("\n\033[0;32m  Saiu...\033[m\n")
                print("\033[1;36m        Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')                         
                exit()
            else: 
               print("\n\033[1;31m  Opção inválida.... Escolha os números selecionados! \033[0;31m 👀\n")  
               time.sleep(1.5)
               os.system('cls' if os.name == 'nt' else 'clear')
               #continue  
            return jogar()                  
        else:
            print("\n\033[1;31m   Valor informado não é numérico. Favor execute e informe um número selecionado!\033[0;31m 👀")
            time.sleep(2)
            jogar()                  
    ## print(" quanto ponto", ponto)
    print("\n  Escolha os limites do Jogo de 1 a 100, o ideal é a diferença até 50 números. ")    
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
            ponto = ponto + 50            
            break   
        elif 51 <= quant <=100:             
            ponto = ponto + 80            
            break   
        else:       
            print("\033[0;31m  Valor invalido.\033[m") 
            print("\033[0;31m  O limite superior não pode ser menor ou igual que limite inferior....\033[m")                           
        continue                                
    ## print(" ponto2 linha 57", ponto)    
    print("\033[0;32m    O número foi gerado agora precisa adivinhar o número escolhido de",infer,"até",super,".")
    print("    E tem",vezes,"tentativas.\033[m")
    numCPU = random.randint(infer,super)    
    for vez in range(1, vezes + 1):
        print("\033[0;36m   A",vez,"tentativa.\033[m")
        plpt = int(input("   Digite o seu palpite: "))           
        if plpt < numCPU:
            print("        Tente um número\033[0;36m MAIOR!\033[m")
            ponto = ponto - 10
        elif plpt > numCPU:
            print("        Tente um número\033[0;36m MENOR!\033[m")
            ponto = ponto - 10
        else:
            break        
    ##print("  vezes:",vezes)     
    ##print("  vez:",vez)         
    ##print("  pontuacao:",ponto)   
    if plpt == numCPU:
        print("\n\033[0;36m  Uuuuhhhhh.... Você acertou o número ",numCPU," e foram ",vez,"vezes.")        
        print("  E a tua Pontuação do Jogo foi: ",ponto,"pontos.")
        if ponto >= 50:
            print("  A tua Pontuação do Jogo foi Muito Excelente!!!!! Parabéns...\033[m\n")
        else:    
            print("  A tua Pontuação do Jogo foi Bom!!!!! Parabéns...\033[m\n")            
    else:
        print("\n  Não foi desta vez.... O Número Secreto era",numCPU,".\n")
        print("  E a tua Pontuação do Jogo foi:",ponto,"pontos.\033[m\n")
        if ponto >= 5:
            print("  A tua Pontuação do Jogo foi Razoável...\033[m\n")
        else:    
            print("  A tua Pontuação do Jogo foi muito Baixo...\033[m\n")  
    resp = input("\033[0;33m  Deseja Jogar novamente[S/N]?\033[m]").upper()
    if resp == 'S':      
        jogar()
    else:    
        print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
        print("\n\033[1;31m   Encerrado, até próxima!!!\033[m\n") 
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')       
    exit()            
jogar()    
    
    

