# ESTRUTURAS CONDICIONAIS 

idade = int(input('Digite sua idade: '))
if idade >= 18: 
    print("Voçê é maior de idade")
else:
    print('Voçê é menor de idade')

"""
    Imprimir Aprovado ou Reprovado a aprtir da media do aluno
"""    

media = float(input('Informe a média do aluno: '))

if media >= 7:
    print('Voçê foi Aprovado(a)!')
elif media >= 5:
    print('Aluno em Recuperação')
else:
    print('Voçê foi Reprovado(a)!')

