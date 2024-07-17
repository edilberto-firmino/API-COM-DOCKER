# Valores dados
X = 10  # Número de casas à venda
I = 500000  # Valor total das casas em reais
B = 200000  # Orçamento disponível em reais

# Calcula o valor médio por casa
valor_medio_por_casa = I / X

# Calcula o número máximo de casas que podemos comprar
numero_maximo_de_casas = B // valor_medio_por_casa

print(f"Com um orçamento de R${B:.2f}, você pode comprar no máximo {numero_maximo_de_casas} casas.")
