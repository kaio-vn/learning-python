nota = int(input("Escolha uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota invalida. ")
    nota = int(input("Escolha uma nota de 0 a 10: "))

print(f"Sua nota foi {nota} ")