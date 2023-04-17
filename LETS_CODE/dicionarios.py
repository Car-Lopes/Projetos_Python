# DICIONARIO

#Criando um dicionario
dicionario = {}
dicionario = dict() 

dicionario = {'nome': 'Carlos', 'idade': 31, 'altura': 1.53}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionario
dicionario['programador'] = True

print(dicionario)

# sobrescrevendo a chave 
dicionario['altura'] = 1.65

print(dicionario)

# Iterando sobre um dicionario acessando as chaves 
for variavel in dicionario:
    print(variavel)

# Iterando sobre um dicionario acessando as chaves e o valor
for variavel in dicionario:
    print(variavel, dicionario[variavel])  

# Verificando a existencia de uma chave
print('peso' in dicionario)

print('altura' in dicionario)


