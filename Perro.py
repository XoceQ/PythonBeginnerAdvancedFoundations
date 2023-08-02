class Perro:
    
    def __init__(self, name, age, weight, breed): #breed = raza
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
        
    def greet(self):
        print("------Bienvenidos-----------")
        
    def eat(self):
        print(perro1.name + " come croquetas")
        
    def bark(self):
        print(perro1.name + " ladra cuando Susi llega")
        
    def petHead(self):
        print("cuando le acaricias la cabeza " + perro1.name + " mueve la cola")
    
    def goPoop(self):
        print("cuando Susy le da de comer muchas croquetas", perro1.name + " hace caca")
    
perro1 = Perro("Fido", 3, 20, "mediano")

print("El nombre del perro de Susi es: ", perro1.name,", tiene", perro1.age, "años",", pesa", perro1.weight, "kg", "y","es un perro ",perro1.breed)
        
accion = input("Escriber la acción que deseas que Fido realize: comer - ladrar - acariciar - hacer caca: ")
if accion == 'comer': 
    print(perro1.eat())
else:
    if accion == 'ladrar':
      print(perro1.bark())
    else:
        if accion == 'acariciar':
            print(perro1.petHead())
        else:
            if accion == 'hacer caca':
               print(perro1.goPoop())
            else:
                print("Ingresar una opcion correcta")