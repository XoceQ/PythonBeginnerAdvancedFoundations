# Among us, se trata de un juego multijugador online al que pueden jugar de 4 a 10 personas.
# Cuando te conectas, de 1 a 3 de ellos se les asigna el rol de impostores,
# y sólo ellos saben que han sido seleccionados para ello. El resto no tendrán ni idea de quién de los participantes es un jugador normal o un impostor.

# Los impostores tendrán que asesinar al resto de participantes sin ser descubiertos, pudiendo sabotear la nave para causar el caos y que así, entre la confusión,
# puedan intentar actuar. Mientras, el resto de integrantes de la nave tienen que intentar ganar completando todas las tareas que se les asignan o descubriendo y eyectando
# al impostor fuera de la nave al espacio exterior antes de que acabe con todos.



class Player:

    def __init__(self, name, color, rol, move_right, move_left,move_up, move_down):
        self.name = name
        self.color = color
        self.rol = rol
        self.move_right = move_right
        self.move_left = move_left
        self.move_up = move_up
        self.move_down = move_down

    def greet(self):
      print("-------------Bienvenidos-------------------------------------------")

    def right1(self):
        print(player1.name, "se ha movido", player1.move_right, "pasos a la derecha")

    def right2(self):
        print(player2.name, "se ha movido", player2.move_right, "pasos a la derecha")

    def right3(self):
        print(player3.name, "se ha movido", player3.move_right, "pasos a la derecha")

    def right4(self):
        print(player4.name, "se ha movido", player4.move_right, "pasos a la derecha")

    def right5(self):
        print(player5.name, "se ha movido", player5.move_right, "pasos a la derecha")

    def left1(self):
        print(player1.name, "se ha movido", player1.move_left, "pasos a la izquierda")

    def left2(self):
        print(player2.name, "se ha movido", player2.move_left, "pasos a la izquierda")

    def left3(self):
        print(player3.name, "se ha movido", player3.move_left, "pasos a la izquierda")

    def left4(self):
        print(player4.name, "se ha movido", player4.move_left, "pasos a la izquierda")

    def left5(self):
        print(player5.name, "se ha movido", player5.move_left, "pasos a la izquierda")

    def up1(self):
        print(player1.name, "se ha movido", player1.move_up, "pasos arriba")

    def up2(self):
        print(player2.name, "se ha movido", player2.move_up, "pasos arriba")

    def up3(self):
        print(player3.name, "se ha movido", player3.move_up, "pasos arriba")

    def up4(self):
        print(player4.name, "se ha movido", player4.move_up, "pasos arriba")

    def up5(self):
        print(player5.name, "se ha movido", player5.move_up, "pasos arriba")

    def down1(self):
        print(player1.name, "se ha movido", player1.move_down, "pasos abajo")

    def down2(self):
        print(player2.name, "se ha movido", player2.move_down, "pasos abajo")

    def down3(self):
        print(player3.name, "se ha movido", player3.move_down, "pasos abajo")

    def down4(self):
        print(player4.name, "se ha movido", player4.move_down, "pasos abajo")

    def down5(self):
        print(player5.name, "se ha movido", player5.move_down, "pasos abajo")




player1 = Player("Jose", "rojo","Ingeniero", 5,6,4,3)
player1.greet()
print(f"El nombre del jugador 1 es: {player1.name} y su rol es: {player1.rol}")
print("El color del traje de ", player1.name, "es ", player1.color)
player1.right1()
player1.left1()
player1.up1()
player1.down1()
if(player1.rol == "Impostor"):
        print("tendras que asesinar al resto de participantes")
else:
        print("intenta ganar completando todas las tareas")
print("-------------------------------------")


player2 = Player("Camilo", "azul","Cientifico", 2,8,7,5)
print(f"El nombre del jugador 2 es: {player2.name} y su rol es: {player2.rol}")
print("El color del traje de ", player2.name, "es ", player2.color)
player2.right2()
player2.left2()
player2.up2()
player2.down2()
if(player2.rol == "Impostor"):
        print("tendras que asesinar al resto de participantes")
else:
        print("intenta ganar completando todas las tareas")
print("-------------------------------------")

player3 = Player("Daniela", "Naranja","Angél guardián", 2,4,5,8)
print(f"El nombre del jugador 3 es: {player3.name} y su rol es: {player3.rol}")
print("El color del traje de ", player3.name, "es ", player3.color)
player3.right3()
player3.left3()
player3.up3()
player3.down3()
if(player3.rol == "Impostor"):
        print("tendras que asesinar al resto de participantes")
else:
        print("intenta ganar completando todas las tareas")
print("-------------------------------------")

player4 = Player("Natalia", "Rosado","Cambiaformas", 7,3,9,2)
print(f"El nombre del jugador 4 es: {player4.name} y su rol es: {player4.rol}")
print("El color del traje de ", player4.name, "es ", player4.color)
player4.right4()
player4.left4()
player4.up4()
player4.down4()
if(player4.rol == "Impostor"):
        print("tendras que asesinar al resto de participantes")
else:
        print("intenta ganar completando todas las tareas")
print("-------------------------------------")

player5 = Player("Juan", "Verde","Impostor", 2,6,4,5)
print(f"El nombre del jugador 5 es: {player5.name} y su rol es: {player5.rol} ")
print("El color del traje de ", player5.name, "es ", player5.color)
player5.right5()
player5.left5()
player5.up5()
player5.down5()
if(player5.rol == "Impostor"):
        print("tendras que asesinar al resto de participantes")
else:
        print("intenta ganar completando todas las tareas")
print("-------------------------------------")