numbers_pares = 0
numbers_impar = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}º numero: "))

    if num % 2 == 0:
        numbers_pares += 1
    elif num % 2 > 0:
        numbers_impar += 1

print(f"A quantidade de numeros pares é: {numbers_pares}")
print(f"A quantidade de numeros impares é: {numbers_impar}")