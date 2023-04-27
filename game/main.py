'''
**********************************************
Juego:         Piedra, Papel o Tijeras v1.0 
**********************************************
Desarrollador: Andrés Felipe Jaramillo Osorio
Fecha:         Abril 26 de 2023
**********************************************
'''
import random

options = ['piedra','papel','tijeras']

def cabezote():
    print("**********************************")
    print("**** PIEDRA - PAPEL - TIJERAS ****")
    print("**********************************")
    return int(input('Número de rounds? => '))
    
def juego(n):
    print('\n')
    result = ''
    for i in range(n):
        print(f'ROUND {i+1}')
        print('********')
        user_option = input('Ingrese una opción: ')
        if user_option.lower() in options:
            computer_option = random.choice(options)
        else:
            print('Opción inválida...')
        print(f'User:     {user_option}')
        print(f'Computer: {computer_option}\n')
        result += ganador(user_option,computer_option)
    return result

def ganador(u,c):
    if u == c:
        return 'e' 
    else:
        if u == 'tijeras':
            if c == 'papel':
                return 'u'
            else:
                return 'c'
        elif u == 'piedra':
            if c == 'tijeras':
                return 'u'
            else:
                return 'c'
        else:
            if c == 'tijeras':
                return 'c'
            else:
                return 'u'

def final(tablero):
    u_score = tablero.count('u')
    c_score = tablero.count('c')
    if u_score > c_score:
        return 'User'
    elif u_score < c_score:
        return 'Computer'
    else:
        return 'Empate'

n = cabezote()
score = juego(n)
ganador = final(score)
print('GANADOR: ' + ganador)
print("**********************************")






