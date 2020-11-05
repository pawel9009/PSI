def fun(text):
    dict = {"lenght": len(text), "letters": [letter for letter in text], "big_letters": text.upper(),
            "small_letters": text.lower()}

    print(dict["lenght"], end="\n")
    print(dict["letters"], end="\n")
    print(dict["big_letters"], end="\n")
    print(dict["small_letters"], end="\n")


slowo = "Hello word"

fun(slowo)
