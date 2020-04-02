import random

lista1 = [1, 2, 3]
type(lista1)

lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista1)
print(lista2[0][1])


# Randomico
cidades = ['Taquara', 'Igrejinha', 'Campo Bom', 'Nova Hartz']
escolha = random.choice(cidades)
print(escolha)

# Add elemento no final da lista
cidades.append('Novo Hamburgo')
print(cidades)

for number in lista2:
    lista1.append(number)

print(lista1)
print(lista1[4][2])
print(float(lista1[4][2]))

lista1[4][1] = 0
print(lista1)

# Deleta o valor da lista na posição 1
del cidades[1]
print(cidades)

# Tuplas sao listas que nao podem ser alteradas
tupla = (2, 3, 4)
print(tupla)
