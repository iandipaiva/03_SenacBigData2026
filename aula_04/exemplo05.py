salario = float(input('Digite o salário: '))
valor_venda = float(input('Digite o valor da venda: '))

if valor_venda >= 5000:
    bonus = 500
    total = salario + bonus
    print(f'O salário é R${salario:.2f}\nO valor da venda foi R${valor_venda:.2f}\nO bônus foi de R${bonus}\nO total é de R${total:.2f}')

elif valor_venda >= 3000:
    bonus = 250
    total = salario + bonus
    print(f'O salário é R${salario:.2f}\nO valor da venda foi R${valor_venda:.2f}\nO bônus foi de R${bonus}\nO total é de R${total:.2f}')

else:
    print(f'O Valor da venda foi R${valor_venda:.2f}\nNão receberá bônus.')