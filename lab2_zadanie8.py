import file_manager as man

a = open("plik.txt", "r")
plik = man.FileManager("plik.txt")


print(plik.read())

plik.update("teraz git")
print("po zmnianie :")
print(plik.read())
