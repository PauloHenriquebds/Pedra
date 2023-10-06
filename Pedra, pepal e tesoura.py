rept = 's'
while rept == 's':
    menu = '''
    1 - pedra
    2 - papel
    3 - tesoura
    '''
    print(menu)
    print('Selecione uma das opções dentro do menu')
    jogador1 = input("Jogador 1 qual a sua escolha?: ")
    jogador2 = input("jogador 2 qual a sua escolha?: ")

    if jogador1 in '123' and jogador2 in '123':
        if jogador1 == '1' and jogador2 == '2':
            print("Jogador 2 ganhou")
        elif jogador2 == '1' and jogador1 == '2':
            print("Jogador 1 ganhou")
        elif jogador1 == '2' and jogador2 == '3':
            print("joador 2 ganhou")
        elif jogador2 == '3' and jogador1 == '1':
            print("jogador 1 ganhou")
        elif jogador2 == '2' and jogador1 == '3':
            print("joador 1 ganhou")
        elif jogador2 == '1' and jogador1 == '3':
            print("jogador 2 ganhou")
        else:
            print("empate")
    else:
        print('Uma das opções invalida')
    rept = input("Deseja repetir?: ").lower()
print("Jogo finalizado")