# Uma loja estabeleceu uma meta de R$ 1.000 em vendas para o mês.
# Crie um algoritmo que solicite o valor total das vendas e informe, se a meta foi atingida ou não.

meta = 1000
valor_total = float(input('Digite o valor total da venda: '))
if valor_total >= meta:
    print(' A meta foi atingida')
else:
    print('A meta não foi atingida')