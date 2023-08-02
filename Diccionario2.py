from ast import Add

class Segip:
  def __init__(self):
    self.persons = {}

  def add_person(self, name, ci):
    if ci in self.persons.values(): #verificamos si el valor ci está presente en los valores del diccionario persons que es un atributo de la clase Segip.
        print(f"El numero de ci de {name} está repetido")
    elif len(ci) != 8:
        print(f"El carnet de {name} es invalido, debe tener 8 digitos")
    else:
        self.persons[name] = ci # accedemos a una entrada del diccionario persons utilizando "name" como clave .
        print(f"El nombre es: {name} y su ci es: {ci}")

segip = Segip()


segip.add_person("Andy", str(12345678))

## No debe agregar a sofia ya que es duplicado
segip.add_person("Sofia", str(12345678))
segip.add_person("Daniel", str(7311023))



#print(segip.persons)



