#LAÇO DE REPETIÇÃO
numero_sorteado = 15

numero_digitado = int(input("Informe um numero entre 1 e 20: "))

while numero_digitado != numero_sorteado: 
    print('Voçê Errou, Tente Novamente...')

    numero_digitado = int(input("Informe um numero entre 1 e 20: "))

print('Parabens! Voçê Acertou!')


#Outro Exemplo 
contador = 0 

while contador < 5:
    print(contador)
    contador = contador +1

print("Vamos comecar15")
cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(cont)
print(resultado)
