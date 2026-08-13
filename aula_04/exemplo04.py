pontos = int(input('Informe o numero de pontos: '))

if pontos >= 100:
    bonus = 10
    total_pontos = pontos + bonus
    print(f'A pontuação foi de: {pontos}\nO bônus é de {bonus}\nO total de pontos é: {total_pontos}')  

elif pontos >= 50:
    bonus = 5
    total_pontos = pontos + bonus
    print(f'A pontuação foi de:{pontos}\nO bônus é de {bonus}\nO total de pontos é: {total_pontos}')

elif pontos >= 30:
    bonus = 2
    total_pontos = pontos + bonus
    print(f'A pontuação foi de:{pontos}\nO bônus é de {bonus}\nO total de pontos é: {total_pontos}')

else:
    print(f'Não ganhou bonus!') 