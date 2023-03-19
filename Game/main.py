import random
#Selecionar PIEDRA PAPEL O TIJERA
def selec_options():
    options = ('piedra','papel','tijera')
    finish = False
    while finish == False:
        user_op = input('Pieda, Papel o Tijera: ')
        user_op = user_op.lower()
        computer_op = random.choice(options)
        if user_op not in options:
            print('Esa opción no es valida')
            continue
        print(f'Player: {user_op}')
        print(f'PC: {computer_op}')
        finish = True
        return user_op,computer_op
#Verificamos quien gano
def rulls_play(user_op,computer_op,computer_wins,user_wins,raund):
    if user_op == 'piedra':
        if computer_op == 'piedra':
            print('EMPATE')
            raund +=1 
        elif computer_op == 'papel':
            print('PC WIN')
            raund +=1 
            computer_wins += 1
        elif computer_op == 'tijera':
            print('Player WIN')
            raund +=1 
            user_wins += 1
    if user_op == 'papel':
        if computer_op == 'papel':
            print('EMPATE')
            raund +=1 
        elif computer_op == 'tijera':
            print('PC WIN')
            raund +=1 
            computer_wins += 1
        elif computer_op == 'piedra':
            print('Player WIN')
            raund +=1 
            user_wins += 1
    if user_op == 'tijera':
        if computer_op == 'tijera':
            print('EMPATE')
            raund +=1 
        elif computer_op == 'piedra':
            print('PC WIN')
            raund +=1 
            computer_wins += 1
        elif computer_op == 'papel':
            print('Player WIN')
            raund +=1 
            user_wins += 1
    return computer_wins,user_wins,raund
#Verificamos el marcador
def verifi_win(computer_wins,user_wins):
    if (computer_wins - user_wins) == 2:
        print('PC WINERS')
        return True
    elif (user_wins - computer_wins) == 2:
        print('Player WINERS')
        return True
    else:
        return False
#Ejecutamos todo el juego
def play_game():
    computer_wins = 0
    user_wins = 0
    raund = 1
    finis_game = False
    while finis_game == False:
        print('*'*10)
        print(f'RAUND {raund}')
        print('*'*10)
        print('MARCADOR')
        print(f'PC {computer_wins}')
        print(f'Player {user_wins}')
        
        user_op,computer_op = selec_options()
        computer_wins,user_wins,raund = rulls_play(user_op,computer_op,computer_wins,user_wins,raund)
        finis_game = verifi_win(computer_wins,user_wins)

play_game()


    

    