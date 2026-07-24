nome = input("Digite seu nome: ")
senha = input("Digita sua senha: ")

while nome == senha:
    print("Sua senha e nome nao podem ser os mesmos. ")
    nome = input("Digite seu nome: ")
    senha = input("Digita sua senha: ")

print(f"Sua senha é \"{senha}\"")
print(f"Seu nome e \"{nome}\"")