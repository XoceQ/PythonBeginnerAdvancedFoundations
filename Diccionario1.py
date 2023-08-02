class Juego:
    def __init__(self):
        print("solo considera como entradas validas las siguientes: piedra, papel, tijera, lagarto, spock")
        
        #se pasa el diccionario como un parametro

        self.game_rules = {1: "Tijera corta Papel",
                           2: "Papel envuelve Piedra",
                           3:"Piedra aplasta Lagarto",
                           4: "Lagarto envenena Spock",
                           5: "Spock rompe Tijera",
                           6: "Tijera decapita Lagarto",
                           7: "Lagarto devora Papel",
                           8: "Papel desautoriza Spock",
                           9: "Spock vaporiza Piedra",
                           10:"Piedra aplasta Tijera"}



    def greet(self):
        print("-------Bienvenido al Juego piedra, papel, tijera, lagarto, spock--------------")
        
    
    def round(self, player_1,  player_2):
        
        if player_1 == 'tijera' and player_2 == 'papel' or player_1 == 'papel' and player_2 == 'tijera':
            print(self.game_rules.get(1))
        elif player_1 == 'papel' and player_2 == 'piedra' or player_1 == 'piedra' and player_2 == 'papel': 
            print(self.game_rules.get(2))
        elif player_1 == 'piedra' and player_2 == 'lagarto' or player_1 == 'lagarto' and player_2 == 'piedra':
            print(self.game_rules.get(3))
        elif player_1 == 'lagarto' and player_2 == 'spock' or player_1 == 'spock' and player_2 == 'lagarto':
            print(self.game_rules.get(4))
        elif player_1 == 'spock' and player_2 == 'tijera' or player_1 == 'tijera' and player_2 == 'spock':
            print(self.game_rules.get(5))
        elif player_1 == 'tijera' and player_2 == 'lagarto' or player_1 == 'lagarto' and player_2 == 'tijera':
            print(self.game_rules.get(6))
        elif player_1 == 'lagarto' and player_2 == 'papel' or player_1 == 'papel' and player_2 == 'lagarto' :
            print(self.game_rules.get(7))
        elif player_1 == 'papel' and player_2 == 'spock' or player_1 == 'spock' and player_2 == 'papel':
            print(self.game_rules.get(8))
        elif player_1 == 'spock' and player_2 == 'piedra' or player_1 == 'piedra' and player_2 == 'spock':
            print(self.game_rules.get(9))
        elif player_1 == 'piedra' and player_2 == 'tijera' or player_1 == 'tijera' and player_2 == 'piedra':
            print(self.game_rules.get(10))
        else:
            print("Ingresar una opción correcta")



rock_paper_scissors_lizard_spock = Juego()
rock_paper_scissors_lizard_spock.greet()

while True:
  player_1 = input("Ingresa el valor que elije el jugador 1: ")
  player_2 = input("Ingresa el valor que elije el jugador 2: ")
  
  rock_paper_scissors_lizard_spock.round(player_1.lower(), player_2.lower())

  play_again = input("Quieres jugar de nuevo? (yes/no)").lower()
  if play_again != 'yes':
    break
