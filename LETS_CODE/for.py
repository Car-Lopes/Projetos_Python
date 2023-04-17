#ESTRUTURA FOR 
#FOR é para quando eu sei o numero de vezes que loop será executado

#Do 0 até 4
for variavel in range(5):
    print(variavel)

#Do 1 até 4 
for variavel in range(1,5):
    print(variavel)    

#Do 1 até 9 pulando de 2 em 2  
for variavel in range(1, 10, 2):
    print(variavel)      

#outra exemplo 
soma = 0
for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota
    media = soma / 3

print(f'Média do Aluno é {media}') 

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')    
else:
    print('Reprovado')    


for _ in "let's code":
  print("Olá, mundo!")