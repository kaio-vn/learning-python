salario = float(input("Insira seu salario: "))
total = 0.00
percentual_aumento = 0.00
diferenca = 0 

if salario <= 280:
    total = (salario * 0.20) + salario
    percentual_aumento = 20
    diferenca = total - salario
elif salario > 280 and salario <= 700:
    total = (salario * 0.15) + salario
    percentual_aumento = 15
    diferenca = total - salario
elif salario > 700 and salario <= 1500:
    total = (salario * 0.10) + salario
    percentual_aumento = 10
    diferenca = total - salario
else:
    total = (salario * 0.05) + salario
    percentual_aumento = 5
    diferenca = total - salario

print(f"Salario inicial {salario} ")
print(f"Percentual {percentual_aumento}% ")
print(f"Valor do aumento: {diferenca} ")
print(f"Total: {total} ")