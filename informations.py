nome = input("Digite seu nome: ")

while  len(nome) < 3:
    print("Seu nome precisa ter mais que 3 caracteres")
    nome = input("Digite seu nome: ")

idade = int(input("Digite seu idade: "))

while idade < 0 or idade > 150:
    print("Voce precisa ter entre 0 e 150 anos.")
    idade = int(input("Digite seu idade: "))

salario = int(input("Digite seu salario: "))

while salario <= 0:
    print("Seu salario precisa ser maior que 0. ")
    salario = int(input("Digite seu salario: "))

sexo = input("Digite seu sexo: ")

while not sexo != "f" or sexo != "m":
    print("Seu sexo precisa ser f ou m. ")
    sexo = input("Digite seu sexo: ")

estado_civil = input("Digite seu estado civil:")

while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    print("Digite s, c, v ou d.")
    estado_civil = input("Digite seu estado civil: ")
