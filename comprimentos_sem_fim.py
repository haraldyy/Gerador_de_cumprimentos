from random import *
#o programa continua em execução enquanto a variável for verdadeira 'True'
executa=True
adjetivos=['maravilhoso','acima da média','excelente']
hobbies=['andar de bicicleta','programar','fazer chá']
print("Gerador de Cumprimentos")
print('-'*20)
nome=input("Qual é o seu nome?:")
print('''
Menu
    c = Obter cumprimento
    q = sair
''')
while executa == True:
    menu=input("\n>_").lower()
#'c' para um comprimento
    if menu == 'c':
        print("Aqui está o seu cumprimento",nome,":")
#Obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
        print(nome,", você é ",choice(adjetivos)," em ",choice(hobbies))
    elif menu=='q':executa=False
    elif menu!='q' or menuchoice!='c':print("Digite uma opção válida!")
