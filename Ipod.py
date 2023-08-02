class Ipod:
    
    def __init__(self, model, generation,max_capacity,color):
        self.model = model
        self.generation = generation
        self.max_capacity = max_capacity
        self.color = color
    
    def greet(self):
        print("------Bienvenidos-----------") 
    
    def ipod_classic(self):
        print("Todas las versiones de Ipod Classic son:")
        print(f"Ipod: {Ipodclassic1.model},  Generation: {Ipodclassic1.generation},  Max capacity: {Ipodclassic1.max_capacity} GB, Color: {Ipodclassic1.color}")
        print(f"Ipod: {Ipodclassic2.model},  Generation: {Ipodclassic2.generation},  Max capacity: {Ipodclassic2.max_capacity} GB, Color: {Ipodclassic2.color}")
        print(f"Ipod: {Ipodclassic3.model},  Generation: {Ipodclassic3.generation},  Max capacity: {Ipodclassic3.max_capacity} GB, Color: {Ipodclassic3.color}")
        print(f"Ipod: {Ipodclassic4.model},  Generation: {Ipodclassic4.generation},  Max capacity: {Ipodclassic4.max_capacity} GB, Color: {Ipodclassic4.color}")
        print(f"Ipod: {Ipodclassic5.model},  Generation: {Ipodclassic5.generation},  Max capacity: {Ipodclassic5.max_capacity} GB, Color: {Ipodclassic5.color}")
        print(f"Ipod: {Ipodclassic6.model},  Generation: {Ipodclassic6.generation},  Max capacity: {Ipodclassic6.max_capacity} GB, Color: {Ipodclassic6.color}")

    def ipod_mini(self):
        print("Todas las versiones de Ipod Mini son:")
        print(f"Ipod: {IpodMini1.model},  Generation: {IpodMini1.generation},  Max capacity: {IpodMini1.max_capacity} GB, Color: {IpodMini1.color}")
        print(f"Ipod: {IpodMini2.model},  Generation: {IpodMini2.generation},  Max capacity: {IpodMini2.max_capacity} GB, Color: {IpodMini2.color}")

    def ipod_nano(self):
        print("Todas las versiones de Ipod Nano son:")
        print(f"Ipod: {IpodNano1.model},  Generation: {IpodNano1.generation},  Max capacity: {IpodNano1.max_capacity} GB, Color: {IpodNano1.color}")
        print(f"Ipod: {IpodNano2.model},  Generation: {IpodNano2.generation},  Max capacity: {IpodNano2.max_capacity} GB, Color: {IpodNano2.color}")
        print(f"Ipod: {IpodNano3.model},  Generation: {IpodNano3.generation},  Max capacity: {IpodNano3.max_capacity} GB, Color: {IpodNano3.color}")
        print(f"Ipod: {IpodNano4.model},  Generation: {IpodNano4.generation},  Max capacity: {IpodNano4.max_capacity} GB, Color: {IpodNano4.color}")
        print(f"Ipod: {IpodNano5.model},  Generation: {IpodNano5.generation},  Max capacity: {IpodNano5.max_capacity} GB, Color: {IpodNano5.color}")
        print(f"Ipod: {IpodNano6.model},  Generation: {IpodNano6.generation},  Max capacity: {IpodNano6.max_capacity} GB, Color: {IpodNano6.color}")
        print(f"Ipod: {IpodNano7.model},  Generation: {IpodNano7.generation},  Max capacity: {IpodNano7.max_capacity} GB, Color: {IpodNano7.color}")
        
    def ipod_shuffle(self):
        print("Todas las versiones de Ipod Shuffle son:")
        print(f"Ipod: {IpodShuffle1.model},  Generation: {IpodShuffle1.generation},  Max capacity: {IpodShuffle1.max_capacity} GB, Color: {IpodShuffle1.color}")
        print(f"Ipod: {IpodShuffle2.model},  Generation: {IpodShuffle2.generation},  Max capacity: {IpodShuffle2.max_capacity} GB, Color: {IpodShuffle2.color}")
        print(f"Ipod: {IpodShuffle3.model},  Generation: {IpodShuffle3.generation},  Max capacity: {IpodShuffle3.max_capacity} GB, Color: {IpodShuffle3.color}")
        print(f"Ipod: {IpodShuffle4.model},  Generation: {IpodShuffle4.generation},  Max capacity: {IpodShuffle4.max_capacity} GB, Color: {IpodShuffle4.color}")

    def ipod_touch(self):
        print("Todas las versiones de Ipod Touch son:")
        print(f"Ipod: {IpodTouch1.model},  Generation: {IpodTouch1.generation},  Max capacity: {IpodTouch1.max_capacity} GB, Color: {IpodTouch1.color}")
        print(f"Ipod: {IpodTouch2.model},  Generation: {IpodTouch2.generation},  Max capacity: {IpodTouch2.max_capacity} GB, Color: {IpodTouch2.color}")
        print(f"Ipod: {IpodTouch3.model},  Generation: {IpodTouch3.generation},  Max capacity: {IpodTouch3.max_capacity} GB, Color: {IpodTouch3.color}")
        print(f"Ipod: {IpodTouch4.model},  Generation: {IpodTouch4.generation},  Max capacity: {IpodTouch4.max_capacity} GB, Color: {IpodTouch4.color}")
        print(f"Ipod: {IpodTouch5.model},  Generation: {IpodTouch5.generation},  Max capacity: {IpodTouch5.max_capacity} GB, Color: {IpodTouch5.color}")
        print(f"Ipod: {IpodTouch6.model},  Generation: {IpodTouch6.generation},  Max capacity: {IpodTouch6.max_capacity} GB, Color: {IpodTouch6.color}")
        print(f"Ipod: {IpodTouch7.model},  Generation: {IpodTouch7.generation},  Max capacity: {IpodTouch7.max_capacity} GB, Color: {IpodTouch7.color}")
        
        
    def play(self):
        print("la canción 1 se esta reproduciendo")
    
    def stop(self):
        print("la canción 1 se detuvo")
        
    def mode_right(self):
        print("la cancion se adelantó 5 seg")
    
    def mode_left(self):
        print("la cancion se retrasó 5 seg")
        
    def volup(self):
        print("subió el volumen")
    
    def voldown(self):
        print("bajó el volumen")
    
    def headphonesin(self):
        print("conectó los auriculares")
        
    def headphonesout(self):
        print("desconectó los auriculares")
    
    def chargein(self):
        print("conectó el cargador")
        
    def chargeout(self):
        print("desconectó el cargador")
    
    
Ipodclassic1 = Ipod("Classic", "First", 5.10,"blanco")
Ipodclassic2 = Ipod("Classic", "Second", 10.20, "blanco")
Ipodclassic3 = Ipod("Classic", "Third", 40, "blanco")
Ipodclassic4 = Ipod("Classic", "Fourth", 60, "blanco")
Ipodclassic5 = Ipod("Classic", "Fifth", 80, "blanco")
Ipodclassic6 = Ipod("Classic", "Sixth", 120, "gris")

IpodMini1 = Ipod("Mini", "First", 4, "verde")
IpodMini2 = Ipod("Mini", "Second", 6, "verde")

IpodNano1 = Ipod("Nano", "First", 4, "blanco")
IpodNano2 = Ipod("Nano", "Second", 8, "gris")
IpodNano3 = Ipod("Nano", "Third", 8, "gris")
IpodNano4 = Ipod("Nano", "Fourth", 16, "negro")
IpodNano5 = Ipod("Nano", "Fifth", 16, "negro")
IpodNano6 = Ipod("Nano", "Sixth", 16, "negro")
IpodNano7 = Ipod("Nano", "Seventh", 16, "negro")

IpodShuffle1 = Ipod("Shuffle", "First", 1, "blanco")
IpodShuffle2 = Ipod("Shuffle", "Second", 2, "blanco")
IpodShuffle3 = Ipod("Shuffle", "Third", 4, "blanco")
IpodShuffle4 = Ipod("Shuffle", "Fourth", 2, "gris")

IpodTouch1 = Ipod("Touch", "First", 32, "negro")
IpodTouch2 = Ipod("Touch", "Second", 32, "negro")
IpodTouch3 = Ipod("Touch", "Third", 64, "negro")
IpodTouch4 = Ipod("Touch", "Fourth", 64, "negro")
IpodTouch5 = Ipod("Touch", "Fifth", 64, "negro")
IpodTouch6 = Ipod("Touch", "Sixth", 128, "negro")
IpodTouch7 = Ipod("Touch", "Seventh", 256, "negro")


print(Ipodclassic1.greet())
tipo = int(input("Ver información de Ipod, selecciona entre (1-5): 1.Classic 2.Mini 3.Nano 4.Shuffle 5.Touch: \n"))
if tipo == 1:
    print(Ipodclassic1.ipod_classic())
else:
    if tipo == 2:
      print(IpodMini1.ipod_mini())
    else:
        if tipo == 3:
          print(IpodNano1.ipod_nano())
        else:
            if tipo == 4:
              print(IpodShuffle1.ipod_shuffle())
            else:
                if tipo == 5:
                  print(IpodShuffle1.ipod_touch())
    



x = int(input("Selecciona una opción (1-9): 1. Reproducir 2. Detener 3. Adelantar 4. Retrasar 5. Subir volumen 6. Bajar volumen 7. Conectar auriculares 8. Desconectar auriculares 9. Conectar cargardor 10. Desconectar cargardor: " ))
if x == 1:
  print(Ipodclassic1.play())
else:
    if x == 2:
      print(Ipodclassic1.stop())
    else:
        if x == 3:
            print(Ipodclassic1.mode_right())
        else:
            if x == 4:
                print(Ipodclassic1.mode_left())
            else:
                if x == 5:
                    print(Ipodclassic1.volup())
                else:
                    if x == 6:
                        print(Ipodclassic1.voldown())
                    else:
                        if x == 7:
                            print(Ipodclassic1.headphonesin())
                        else:
                            if x == 8:
                                print(Ipodclassic1.headphonesout())
                            else:
                                if x == 9:
                                    print(Ipodclassic1.chargein())
                                else:
                                    if x == 10:
                                        print(Ipodclassic1.chargeout())
                                    else:
                                        print("Ingrese un valor correcto")



