def fun(text, litera):
    zam = litera
    zam += zam.upper()
    for i in zam:
        if i in text:
            text = text.replace(i, '')

    print(text)


slowo = "AaHelalo awaaaoradaaaa"
litera = 'a'
fun(slowo, litera)
