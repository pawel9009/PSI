list_b = [x for x in range(20)]
list_a = [x for x in range(20)]
nowa = []
dl = len(list_a) + len(list_b)


def fun(lista_a, lista_b):
    for x in range(len(list_a)):
        if list_a[x] % 2 == 0:
            nowa.append(lista_a[x])
    for y in range(len(list_b)):
        if list_b[y] % 2 == 1:
            nowa.append(lista_b[y])


fun(list_a, list_b)
print(nowa)
