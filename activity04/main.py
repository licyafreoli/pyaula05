zero_vinteecinco = 0
vinteeseis_cesenta = 0
maior_cesenta = 0

for i in range(10):
    idades = int(input(f"Digite a idade do {i + 1}º aluno: "))

    if idades > 0 and idades <= 25:
        zero_vinteecinco += 1
    elif idades >= 26 and idades <= 60:
        vinteeseis_cesenta += 1
    else:
        maior_cesenta += 1
    
    
if zero_vinteecinco > vinteeseis_cesenta and zero_vinteecinco > maior_cesenta:
    print("A turma é jovem!")
elif vinteeseis_cesenta > maior_cesenta and vinteeseis_cesenta > zero_vinteecinco:
    print("A turma é adulta!")
elif maior_cesenta > vinteeseis_cesenta and maior_cesenta > zero_vinteecinco:
    print("Aturma é idosa!")