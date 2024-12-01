total_gasto = 0.0
quantidade_acima_1000 = 0
produto_mais_barato = None
preco_produto_mais_barato = float("inf")

while True:

    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))

    total_gasto += preco_produto

    if preco_produto > 1000:
        quantidade_acima_1000 += 1

    if preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    continuar = input("Deseja adicionar mais produtos? (sim ou não): ")
    if continuar != 'sim':
        break

print("\nResumo da Compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$ 1000: {quantidade_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R$ {preco_produto_mais_barato:.2f})")