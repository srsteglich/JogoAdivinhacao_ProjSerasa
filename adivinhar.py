import random

def jogar():
    print("\n       Bem-vindo ao jogo de adivinhação de números!\n")  
    nivel = 0   
    ponto = 0    
    while nivel != 4:       
        print("  Qual o nível de dificuldade de tentativas? ")
        print("  1 - Fácil (20 Tentativas)")
        print("  2 - Médio (10 Tentativas)")
        print("  3 - Difícil (05 Tentativas)")
        print("  4 - Sair do Jogo")
        nivel = int(input("  Digite um número:"))              
        if nivel == 1:
            ponto = 10                                
            break
        elif nivel == 2:
            ponto = 30              
            break            
        elif nivel == 3:
            ponto = 80            
            break
        elif nivel == 4:          
            exit(" \n  Saiu...\n")  
        else: 
           print("\n  Opcao invalida....\n")  
           #continue  
        return jogar()      
            
    ## print(" quanto ponto", ponto)
    print("\n  Escolha os limites do Jogo, dê diferença até 50 números ")    
    while True:    
        infer = int(input("  Digite o limite inferior: "))
        super = int(input("  Digite o limite superior: "))                          
        quant = super - infer       
        if 2 <= quant <= 9:
            ## print("estou linha 37")
            ponto = ponto + 5   
            break            
        elif 10 <= quant <= 19:
            ponto = ponto + 10                    
            break               
        elif 20 <= quant <= 29:
            ponto = ponto + 20
            break               
        elif 30 <= quant <= 39:
            ponto = ponto + 40            
            break              
        elif 40 <= quant <= 50:
            ## print("estou linha 50")
            ponto = ponto + 80            
            break               
        else:
            print("\n  Valor invalido.") 
            print("  O limite superior não pode ser menor ou igual que limite inferior....")                           
        continue                                
    ## print(" ponto 2 linha 57", ponto)
    numCPU = random.randint(infer,super)
    print(" o numero do CPU " , numCPU)
    vezes = 0
    
    while True:
        plpt = int(input("  Digite o seu palpite: "))   
        vezes += 1
        #### falta pontos e correto o numero CPU
        
        if plpt < numCPU:
            print("  Tente um número maior!")
        elif plpt < numCPU:
            print("  Tente um número menor!")
        else:
            print(f"  Uuuuhhhhh.... Você acertou o número {numCPU} e foram {vezes} vezes.\n")

            resp = input("Deseja jogar novamente[S/N]?").upper()
            if resp == 'S':      
                jogar()
            else:    
                print(" Encerrou") 
                exit()
jogar()    
    
    

