# Uma instituição de ensino precisa calcular a média bimestral dos alunos. A avaliação é
# composta por Teste e Prova. Crie um algoritmo que solicite as duas notas ao usuário, calcule a média e imprima o resultado no final.

teste = float(input('Digite a nota do Teste: '))
prova = float(input('Digite a nota da Prova: '))
media_bimestral = (teste + prova) / 2
print(f'A média bimestral é : {media_bimestral}')