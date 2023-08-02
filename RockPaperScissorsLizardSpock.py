class Juego:
    
    
    def __init__(self):
        print("solo considera como entradas validas las siguientes: piedra, papel, tijera, lagarto, spock")

        
        
    def greet(self):
        print("-------Bienvenido al Juego piedra, papel, tijera, lagarto, spock--------------")

    def round(self):

        if player_1 == 'tijera' and player_2 == 'papel' or player_1 == 'papel' and player_2 == 'tijera':
            print("Tijera corta Papel")
        elif player_1 == 'papel' and player_2 == 'piedra' or player_1 == 'piedra' and player_2 == 'papel':
            print("Papel envuelve Piedra")
        elif player_1 == 'piedra' and player_2 == 'lagarto' or player_1 == 'lagarto' and player_2 == 'piedra':
            print("Piedra aplasta Lagarto")
        elif player_1 == 'lagarto' and player_2 == 'spock' or player_1 == 'spock' and player_2 == 'lagarto':
            print("Lagarto envenena Spock")
        elif player_1 == 'spock' and player_2 == 'tijera' or player_1 == 'tijera' and player_2 == 'spock':
            print("Spock rompe Tijera")
        elif player_1 == 'tijera' and player_2 == 'lagarto' or player_1 == 'lagarto' and player_2 == 'tijera':
            print("Tijera decapita Lagarto")
        elif player_1 == 'lagarto' and player_2 == 'papel' or player_1 == 'papel' and player_2 == 'lagarto' :
            print("Lagarto devora Papel")
        elif player_1 == 'papel' and player_2 == 'spock' or player_1 == 'spock' and player_2 == 'papel':
            print("Papel desautoriza Spock")
        elif player_1 == 'spock' and player_2 == 'piedra' or player_1 == 'piedra' and player_2 == 'spock':
            print("Spock vaporiza Piedra")
        elif player_1 == 'piedra' and player_2 == 'tijera' or player_1 == 'tijera' and player_2 == 'piedra':
            print("Piedra aplasta Tijera")
        else: 
            print("Ingresar una opción correcta")
            
rock_paper_scissors_lizard_spock = Juego()
rock_paper_scissors_lizard_spock.greet()


player_1 = input("Ingresa el valor que elije el jugador 1: ")
player_2 = input("Ingresa el valor que elije el jugador 2: ")
rock_paper_scissors_lizard_spock.round()



    