lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = lista[5:]
del lista[5:]

print(lista)
print(lista2)

suma = lista + lista2
suma.insert(0, 0)
print(suma)
posortowana = suma
print(posortowana[::-1])



