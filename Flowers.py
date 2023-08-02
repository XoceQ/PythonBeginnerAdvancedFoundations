class Flower:

    def __init__(self, name, color, n_petals, type_petal, steam, scent):
        self.name = name
        self.color = color
        self.n_petals = n_petals
        self.type_petal = type_petal
        self.steam = steam
        self.scent = scent

    def greet(self):
        print("---------------Bienvenidos-----------------------------")

    def regar(self):
        print("¡regada!, recuerda regar agua sobre la flores 2 veces por semana")

    def cortar(self):
        print("usar una tijera")



flower1 = Flower("flor 1","blanca",6,"delgados","largo", "suave")
flower1.greet()
flower2 = Flower("flor 2","amarilla",5,"gruesos", "corto", "fuerte")
flower3 = Flower("flor 3","blanca",5, "gruesos", "corto", "fuerte")
flower4 = Flower("flor 4","amarilla y naranja",13,"gruesos y separados", "corto", "toxico")
flower5 = Flower("flor 5","azul",5, "puntiagudos","corto", "venenoso")
flower6 = Flower("flor 6","amarilla",5, "ovalados","largo", "suave")
flower7 = Flower("flor 7","rosada",5,"ondulados", "corto", "delcioso")
flower8 = Flower("flor 8","amarilla",25, "delgados","corto", "no se percibe")
flower9 = Flower("flor 9","violeta",5, "largos","corto", "fuerte")
flower10 = Flower("flor 10","blanca",5, "gruesos","corto", "suave")
flower11 = Flower("flor 11","morada",27,"delgados y separados", "corto", "toxico")
flower12 = Flower("flor 12","blanca",2, "compactos","largo", "inconfundible")





x = int(input("Ingrese el numero de flor (1-12): "))

if x == 1:
    print(f"la  {flower1.name}  es  {flower1.color}   tiene  {flower1.n_petals} petalos {flower1.type_petal}, su tallo es:  {flower1.steam} y su aroma es {flower1.scent}")

else:
    if x == 2:
        print(f"la  {flower2.name}  es  {flower2.color}   tiene  {flower2.n_petals} petalos {flower2.type_petal}, su tallo es:  {flower2.steam} y su aroma es {flower2.scent}")
    else:
        if x == 3:
            print(f"la  {flower3.name}  es  {flower3.color}   tiene  {flower3.n_petals} petalos {flower3.type_petal}, su tallo es:  {flower3.steam} y su aroma es {flower3.scent}")
        else:
            if x == 4:
                print(f"la  {flower4.name}  es  {flower4.color}   tiene  {flower4.n_petals} petalos {flower4.type_petal}, su tallo es:  {flower4.steam} y su aroma es {flower4.scent}")
            else:
                if x == 5:
                    print(f"la  {flower5.name}  es  {flower5.color}   tiene  {flower5.n_petals} petalos {flower5.type_petal}, su tallo es:  {flower5.steam} y su aroma es {flower5.scent}")
                else:
                    if x == 6:
                        print(f"la  {flower6.name}  es  {flower6.color}   tiene  {flower6.n_petals} petalos {flower6.type_petal}, su tallo es:  {flower6.steam} y su aroma es {flower6.scent}")
                    else:
                        if x == 7:
                            print(f"la  {flower7.name}  es  {flower7.color}   tiene  {flower7.n_petals} petalos {flower7.type_petal}, su tallo es:  {flower7.steam} y su aroma es {flower7.scent}")
                        else:
                            if x == 8:
                                print(f"la  {flower8.name}  es  {flower8.color}   tiene  {flower8.n_petals} petalos {flower8.type_petal}, su tallo es:  {flower8.steam} y su aroma es {flower8.scent}")
                            else:
                                if x == 9:
                                    print(f"la  {flower9.name}  es  {flower9.color}   tiene  {flower9.n_petals} petalos {flower9.type_petal}, su tallo es:  {flower9.steam} y su aroma es {flower9.scent}")
                                else:
                                    if x == 10:
                                        print(f"la  {flower10.name}  es  {flower10.color}   tiene  {flower10.n_petals} petalos {flower10.type_petal}, su tallo es:  {flower10.steam} y su aroma es {flower10.scent}")
                                    else:
                                        if x == 11:
                                            print(f"la  {flower11.name}  es  {flower11.color}   tiene  {flower11.n_petals} petalos {flower11.type_petal}, su tallo es:  {flower11.steam} y su aroma es {flower11.scent}")
                                        else:
                                            if x == 12:
                                                print(f"la  {flower12.name}  es  {flower12.color}   tiene  {flower12.n_petals} petalos {flower12.type_petal}, su tallo es:  {flower12.steam} y su aroma es {flower12.scent}")
                                            else:
                                                print("ingresa una opción valida")



accion = input("Ingresar alguna opción: regar flor - cortar - ninguna: ")

if accion == 'regar flor':
    print(flower1.regar())
else:
    if accion == 'cortar':
        print(flower1.cortar())
    else:
        if accion == 'ninguna':
           print("que tengas buen día")
        else:
            print("selecciona una opción correcta")