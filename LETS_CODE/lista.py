# LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota = 8.2

#Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Carlos', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)
lista = [26, 'Carlos', 3.14159, False] 

print(lista[1])
print(lista[-1])#Ultimo elemento -2 o penultimo

# Slices

lista =[10, 50, 30, 50, 10, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2]) #pulando de dois em dois 

# Iteração com FOR
lista1 = [1, 3, 5, 7, 8, 10, 12, 14, 16, 18, 20]
for elemento in lista1:
    print(elemento)

# Utilizando os Indices
lista2 = [1, 3, 5, 7, 8, 10, 12, 14, 16, 18, 20]

print('Comprimento da lista:', len(lista2))

for i in range(len(lista2)):
    print(f'Indice {i} Valor Contido {lista2[i]}')

