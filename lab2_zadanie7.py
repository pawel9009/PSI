def reverse(slowo):
    dl = len(slowo)-1
    for x in range(dl, -1, -1):
        print(slowo[x], end="")


wyraz = input("Podaj słowo :")

reverse(wyraz)
