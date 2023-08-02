class Figuras:

    def __init__(self, lado,v_lado, color, angulos,angulosagudos,angulosobtusos,base, altura,area,perimetro,radio,diagonalmayor,diagonalmenor):
       self.lado = lado
       self.v_lado = v_lado
       self.color = color
       self.angulos = angulos
       self.angulosagudos = angulosagudos
       self.angulosobtusos = angulosobtusos
       self.base = base
       self.altura = altura
       self.area = area
       self.perimetro = perimetro
       self.radio = radio
       self.diagonalmayor = diagonalmayor
       self.diagonalmenor = diagonalmenor

cuadrado = Figuras(4,5,"Azul",90,0,0,0,0,0,0,0,0,0)
print(f"El Cuadrado tiene {cuadrado.lado} lados")
print(f"es de color {cuadrado.color}")
print(f"tiene {cuadrado.lado} angulos de {cuadrado.angulos} grados")
cuadrado.area = cuadrado.lado* cuadrado.lado
print(f"el area del cuadrado es: {cuadrado.area} cm2")
cuadrado.perimetro = cuadrado.v_lado+cuadrado.v_lado+cuadrado.v_lado+cuadrado.v_lado
print(f"el perimetro es: {cuadrado.perimetro} cm")
print("------------------------------")

circulo = Figuras(0,0,"Rojo",0,0,0,0,0,0,0,9,0,0)
print(f"el Circulo es de color {circulo.color}")
circulo.area = 3.14*(circulo.radio*circulo.radio)
print(f"el area es: {circulo.area} cm2" )
circulo.perimetro = 2*3.14*circulo.radio
print(f"el perimetro es: {circulo.perimetro} cm")
print("------------------------------")

triangulo = Figuras(3,0,"Amarillo",60,0,0,10,7,0,0,0,0,0)
print(f"el Triangulo tiene {triangulo.lado} lados")
print(f"es de color {triangulo.color}")
print(f"tiene 3 angulos de {triangulo.angulos} grados")
triangulo.area = (triangulo.base * triangulo.altura)/2
print(f"el area es: {triangulo.area} cm2")
triangulo.perimetro = triangulo.lado+triangulo.lado+triangulo.lado
print(f"el perimetro es: {triangulo.perimetro} cm")
print("------------------------------")

rectangulo = Figuras(4,0,"Verde",90,0,0,3,8,0,0,0,0,0)
print(f"el Rectangulo tiene {rectangulo.lado} lados")
print(f"es de color {rectangulo.color}")
print(f"tiene 4 angulos de {rectangulo.angulos} grados")
rectangulo.area = rectangulo.base*rectangulo.altura
print(f"el area es: {rectangulo.area} cm2")
rectangulo.perimetro = rectangulo.base*rectangulo.base + rectangulo.altura*rectangulo.altura
print(f"el perimetro del rectangulo es: {rectangulo.perimetro} cm")
print("------------------------------")

rombo = Figuras(4,10,"Morado",0,70,110,0,0,0,0,0,16,12)
print(f"el Rombo tiene {rombo.lado} lados")
print(f"es de color {rombo.color}")
print(f"tiene 2 angulos agudos de {rombo.angulosagudos} grados")
print(f"tiene 2 angulos obtusos de {rombo.angulosobtusos} grados")
rombo.area = (rombo.diagonalmayor*rombo.diagonalmenor)/2
print(f"el area es: {rombo.area} cm2" )
rombo.perimetro = rombo.v_lado+rombo.v_lado+rombo.v_lado+rombo.v_lado
print(f"el perimetro es: {rombo.perimetro} cm")

