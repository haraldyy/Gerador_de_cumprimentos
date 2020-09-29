from random import *
executa=True
adjetivos=["maravilhoso","acima da média","excelente"]
hobbies=["andar de bicicleta","programar","fazer chá"]
print("Gerador de cumprimentos")
print('-'*20)
nome=input("Qual é o seu nome?:")
print('''
Menu
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
''')
while executa==True:
    menu=input("\n>_").lower()
#'c' para um cumprimento
    if menu=='c':
        print("Aqui está o seu cumprimento ",nome,":")
#obtem um item aleatorio de ambas as listas e adiciona-os ao cumprimento
        print(nome," você é",choice(adjetivos)," em ",choice(hobbies))
        print("De nada!")
    elif menu=='a':
        adicionar=input("Adicione o hobby:")
        hobbies.append(adicionar)
#'d' para remover um hobby
    elif menu=='d':
        deletar=input("Insira o hobby a ser removido:")
        if deletar in hobbies:hobbies.remove(deletar)
        else:print("O hobby não está na lista")
#'p' para imprimir a lista de hobbies
    elif menu=='p':
        print(hobbies)
#'q' para sair
    elif menu=='q':
        executa=False
    else:
        print("Digite uma opção válida!")
