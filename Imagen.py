class Image:

    def __init__(self, name, length, width, dimensions, color, weight, new_width,new_length,new_dimension):
        self.name =  name
        self.length = length
        self.width = width
        self.dimensions = dimensions
        self.color = color
        self.weight = weight
        self.new_width = new_width
        self.new_length = new_length
        self.new_dimension = new_dimension

    def draw(self):
        print(self.name, "esta dibujada a lapiz")

    def cut(self):
        pass
        self.new_dimension = self.new_width*self.new_length
        print("Nuevas dimensiones", self.new_dimension, "pixeles")

    def save(self):
        print("Nombre de archivo a guardar:",self.name,".png")

caricatura = Image("caricatura1",200,200,0,"blanco y negro","250kb",30,30,0)

caricatura.draw()
caricatura.dimensions = caricatura.length * caricatura.width
print("la caricatura tiene una dimension de",caricatura.dimensions, "pixeles")
print("la caricatura se dibuja a",caricatura.color)
print("el peso de la imagen es de", caricatura.weight)
caricatura.cut()
caricatura.save()