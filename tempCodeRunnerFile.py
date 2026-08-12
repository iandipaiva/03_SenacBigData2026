quantidade = int(input("Quantos alunos serão avaliados? "))
i = 1

while i <= quantidade:
    print(f'Aluno {i}')

    teste = float(input('Digite a nota do Teste: '))
    prova = float(input('Digite a nota da Prova: '))

    media = (teste + prova) / 2

    print(f'Média bimestral: {media:.2f}')

    i += 1