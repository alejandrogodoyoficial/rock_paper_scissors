import random

def play():
    player = 0
    python = 0
    replay = True
    while replay:

        print('Write an option between "rock" (1), "paper" (2) or "scissors" (3)')
        print('If you wanna leave to playing write "exit" or (0)')
        print('*****Remember write without quotes*****')

        option = input()

#Se pasan los numeron random a String

        auto_option = str(random.randint(1, 3))

#Se separan en corchete las condicinales segun los terminos a eleguir, en este caso para diferenciarlo entre Player y Python, se repite en todos los if de la funcion
        if (option == '1' or option.lower() == 'rock') and (auto_option == '1'):
            print('Your choice was...')
            print('rock')
            print('The choice of python was...')
            print('rock')
            print("It's a tie")
            print()

        elif (option == '1' or option.lower() == 'rock') and (auto_option == '2'):
            print('Your choice was...')
            print('rock')
            print('The choice of python was...')
            print('paper')
            print('Point for Python')
            python += 1
            print()

        elif (option == '1' or option.lower() == 'rock') and (auto_option == '3'):
            print('Your choice was...')
            print('rock')
            print('The choice of python was...')
            print('scissors')
            print('Point for Player')
            player += 1
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '1'):
            print('Your choice was...')
            print('paper')
            print('The choice of python was...')
            print('rock')
            print('Point for Player')
            player += 1
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '2'):
            print('Your choice was...')
            print('paper')
            print('The choice of python was...')
            print('paper')
            print("It's a tie")
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '3'):
            print('Your choice was...')
            print('paper')
            print('The choice of python was...')
            print('scissors')
            print('Point for Python')
            python += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '1'):
            print('Your choice was...')
            print('scissors')
            print('The choice of python was...')
            print('rock')
            print('Point for Python')
            python += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '2'):
            print('Your choice was...')
            print('scissors')
            print('The choice of python was...')
            print('paper')
            print('Point for Player')
            player += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '3'):
            print('Your choice was...')
            print('scissors')
            print('The choice of python was...')
            print('scissors')
            print("It's a tie")
            print()
        elif option == '0' or option.lower() == 'exit':
            replay = False
            print()
        else:
            print('Please write a correct answer')
            print()

#Se compraran las variables para determinar un output

    print('GAME OVER')
    if player == python:
        print("It's a tie")
    elif player > python:
        print('You won')
    elif player < python:
        print('Python won')
    print()
    
def jugar():
    player = 0
    python = 0
    replay = True
    while replay:

        print('Escribe "piedra" (1), "papel" (2) o "tijera" (3)')
        print('Si quieres dejar de jugar escribe "salir" o (0)')
        print('*****Recuerda "salir "escribir sin las comillas*****')

        option = input()

#Se pasan los numeron random a String
        
        auto_option = str(random.randint(1, 3))

#Se separan en corchete las condicinales segun los terminos a eleguir, en este caso para diferenciarlo entre Player y Python, se repite en todos los if de la funcion

        if (option == '1' or option.lower() == 'rock') and (auto_option == '1'):
            print('tu elegiste...')
            print('piedra')
            print('Python eligio...')
            print('piedra')
            print("Empate")
            print()

        elif (option == '1' or option.lower() == 'rock') and (auto_option == '2'):
            print('tu elegiste...')
            print('piedra')
            print('Python eligio...')
            print('papel')
            print('Punto para Python')
            python += 1
            print()

        elif (option == '1' or option.lower() == 'rock') and (auto_option == '3'):
            print('tu elegiste...')
            print('piedra')
            print('Python eligio...')
            print('tijera')
            print('Punto para el Jugador')
            player += 1
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '1'):
            print('tu elegiste...')
            print('papel')
            print('Python eligio...')
            print('piedra')
            print('Punto para el Jugador')
            player += 1
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '2'):
            print('tu elegiste...')
            print('papel')
            print('Python eligio...')
            print('papel')
            print("Empate")
            print()

        elif (option == '2' or option.lower() == 'paper') and (auto_option == '3'):
            print('tu elegiste...')
            print('papel')
            print('Python eligio...')
            print('tijera')
            print('Punto para Pathon')
            python += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '1'):
            print('tu elegiste...')
            print('tijera')
            print('Python eligio...')
            print('piedra')
            print('Punto para Python')
            python += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '2'):
            print('tu elegiste...')
            print('tijera')
            print('Python eligio...')
            print('papel')
            print('Punto para el Jugador')
            player += 1
            print()

        elif (option == '3' or option.lower() == 'scissors') and (auto_option == '3'):
            print('Tu elegiste...')
            print('tijera')
            print('Python eligio...')
            print('tijera')
            print("Empate")
            print()
        elif option == '0' or option.lower() == 'salir':
            replay = False
            print()
        else:
            print('Por favor elige correctamente')
            print()
    
#Se compraran las variables para determinar un output
    print('FIN DEL JUEGO')
    if player == python:
        print('Empate')
    elif player > python:
        print('Tu ganas')
    elif player < python:
        print('Python gana')
    print()


#Estado del loop inicial
loop = True


#Bucle principal donde corre el juego

while loop:
    
    print('Write your language...')
    print('Write 0 or "english" (without quotes) if your choice is English or...')
    print('write 1 or "spanish" (without quotes) if your choice is Spanish')
    print('Write exit if you wanna finish the game')

    print('')

    print('Escribe tu lenguajes...')
    print('Escribe 0 o "english" (sin comillas) si eliges Ingles o...')
    print('Escribe 1 o "spanish" (sin comillas) si eliges Spanish')
    print('Escribe salir si quieres finalizar la partida')


    choice = input()

    if len(choice) == 4 or len(choice) == 5:
        loop = False
    else:
        if choice == '0' or choice.lower() == 'english':
#Funcion con la logica del juego
            play()
        elif choice == '1' or choice.lower() == 'spanish':
#Funcion con la logica del juego pero en otro idioma, pero sigue siendo igual
            jugar()
        elif len(choice) == 4 or len(choice) == 5:
            loop = False
        else:
            print('Please write a correct answer')
            print('Por favor escribe una respuesta correcta')
            print('\n')