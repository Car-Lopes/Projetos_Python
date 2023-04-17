# > FUNÇÔES
"""
print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuario (entrada padrao) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho dessa lista
max() # - Retorna o maior valor de uma lista
"""
# - Criando Funções 
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Ola, é um prazer ter voçê por aqui!')

# chamando a funcao saudação 
saudacao()

# Função com parametros
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Ola, é um prazer ter voçê por aqui, no curso de {curso}!')

saudacao('Carlos', 'Python')

# Função com parametros default
def saudacao(nome, curso='Python'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Ola, é um prazer ter voçê por aqui, no curso de {curso}!')

saudacao('Carlos', 'C++')

# Funçoes com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20, '-')   
print(resultado) 

