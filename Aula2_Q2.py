numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []
impar = []

for item in numeros:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)
        
print('Esses são os números pares:', par)
print('Esses são os números pares:', impar)