from random import *
print("Gerador de cumprimentos")
print("-"*20)
adjetivos=['maravilhoso', 'acima da média', 'excelente', 'excepcional','único','incrível','ótimo']
hobbies=['andar de bicicleta', 'programar', 'fazer chá','natação','interpretação de texto','Python','Ruby']
nome=input('Qual é seu nome?:')
print("Aqui está o seu cumprimento",nome,":")
#obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, ", voce é",choice(adjetivos)," em ",choice(hobbies),'!')
print('De nada!')
