import random

#Lista que receberá os números aleatórios
lista_numeros = []

#chave para limitar o while
i=0

while i <= 20:

    #gerar número aleatório entre 1 e 100 e salvá-lo na lista
    numero = random.randrange(1,100)
    lista_numeros.append(numero)

#chave para limitar o while
    i = i + 1

maximo = max(lista_numeros)
minimo = min(lista_numeros)

print('Lista gerada aleatoriamente:', lista_numeros)
print('Esse foi o valor máximo encontrado na lista:', maximo)
print('Esse foi o valor minimo encontrado na lista:', minimo)