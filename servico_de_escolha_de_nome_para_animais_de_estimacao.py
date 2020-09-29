from random import *
executa=True
femea=["Amora","Belinha","Mel","Princesa","Estrela","Cacau","Bela","Cristal","Malu","Safira","Pantera","Sereia","Meg","Luma","Pipoca"]
macho=["Bolinha","Manteiga","Totó","Pipoca","Paçoca","Ozzy","Sanção","Thor","Zé","Duque","Pingo","Odin","Costelinha","Marley","Bolota"]
print("Serviço de escolha de nomes para pets")
print('-'*20)
print('''
Menu
    c = dar nome
    a = adicionar nome para macho
    f = adiconar nome para fêmea
    d = remover nome para macho
    t = remover nome para fêmea
    p = imprimir nomes
    q = sair
''')
while executa==True:
    menu=input("\n>_").lower()
#'c' para dar nome a um pet
    if menu=='c':
        qtd=int(input("de quantos nomes você precisa?:"))
        for w in range(qtd):
            print("Você pode chamar seu pet de ",choice(macho),"se for macho, ou ",choice(femea)," se for fêmea.")
#adiciona um nome a variável macho um nome para ser 
    elif menu=='a':
        adicionar=input("Adicionar nome para macho:")
        if adicionar not in macho:machos.append(adicionar)
        else:print("O nome já está na lista")
#'d' para remover um nome para macho
    elif menu=='d':
        deletar=input("Insira o nome a ser removido:")
        if deletar in macho:macho.remove(deletar)
        else:print("O nome não está na lista")
#'p' para imprimir a lista de nomes para machos e femeas
    elif menu=='p':print('Machos:',macho,'Fêmeas:',femea)
#'q' para sair
    elif menu=='q':executa=False
    else:print("Digite uma opção válida!")
