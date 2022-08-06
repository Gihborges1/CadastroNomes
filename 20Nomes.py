def Arrumador_Nomes(Nomes):
    Erro = True
    LI = [] 
    LF = [] 
     
    while True:
        try:
            var1  = int(input("Digite um número de 0 a 20 para organizar a ordem anterior ao nome: "))
            var2  = int(input("Digite um segundo valor, maior que o valor anterior, para organizar a ordem posterior ao Respectivo Nome: "))
            if var1 > var2:
                raise
            else:
                break
        except KeyboardInterrupt:
            print("Programa fechando...")
            Erro = False
        except:
            print("Entrada Inválida, Tente Novamente.")
    if Erro:
        if var1 == var2:
            Nomes.sort()
        else:
            LO = Nomes[var1:var2]
            LO.sort()
        print("Lista Organizada!\n")
        print(LO)
    print("\nFim do Programa!")

QN=20
Nomes=[]
for i in range(QN):
    Nm=input("Insira o nome a ser cadastrado: ")
    Nomes.append(Nm)
P = input("Digite Sim para continuar: ")
if (P == 'Sim') or (P == 'sim') or (P == 'SIM') or (P =='s') or (P =='S'):
    Arrumador_Nomes(Nomes)


