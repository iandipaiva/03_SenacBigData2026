salario_atual = float(input('Digite o salário: '))
tempo_de_casa = float(input('Digite o tempo de casa: '))
setor = input('Digite o setor: ').upper()

if setor == 'A' and tempo_de_casa >= 3:
    aumento = salario_atual * 0.18
    reajuste = '18%'
    

else: 
    aumento = salario_atual * 0.9
    reajuste = '9%'

novo_salario = salario_atual + aumento

print('=-'*10)
print(f'Aumento de R${aumento}')
print(f'Salário reajustado R${novo_salario}')
print(f'reajuste de {reajuste}')