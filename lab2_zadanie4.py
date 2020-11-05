def fun(temperature_type, ile):
    if temperature_type == 'f' or temperature_type == 'F':
        print(ile, "stopni celsjsza to", (ile * 1.8) + 32, " stopni fahrenheit")
    elif temperature_type == 'k' or temperature_type == 'K':
        print(ile, "stopni celsjsza to", ile+273.15, " stopni Kelvin")
    elif temperature_type == 'r' or temperature_type == 'R':
        print(ile, "stopni celsjsza to", (ile+273.15)*1.8, " stopni Rankine")


liczba = 100
zakres = [x for x in range(-50, 70, 1)]
while liczba not in zakres:
    liczba = int(input("podaj liczbe stopni"))


typ = input("Na co chcesz zamienić (f-F , r-R, k-K)?")

fun(typ, liczba)

