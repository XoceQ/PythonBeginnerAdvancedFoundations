#Andrew Tiene una heladeria que yo vendo 3 tipos de helados, uno de vainilla, otro durazno y otro maracuya cada semana
# compra dependiendo de la cantidad que tiene, por ejemplo digamos que el domingo que paso 
# compro 10 de vainilla 20 de durazno y 30 de maracuya porque es el helado que mas se vende, estas con las cantidades minimas que deberia tener en mi heladeria.
# Pero mis helados de vainilla tienen una fecha de vencimiento para el 29 de junio, los de durazno y de maracuya para el 30 de junio. 
# Estoy haciendo el inventario y quiero que me deje ingresar cuantos helados me sobran de vainilla, durazno y maracuya un vez que ingrese la cantidad quiero que me diga
# si necesito comprar mas helados, si mi cantidad que tengo actualmente es menor a la mitad del total que tenia y si la fecha esta cercana a la fecha de hoy o es igual entonces que me diga que tengo que comprar sino que me diga todavia no es necesario"

import datetime
from datetime import datetime

class Heladeria:
    
    def __init__(self):
        self.n_vanilla_ice = 10
        self.n_peach_ice =  20
        self.n_passion_fruit_ice = 30
        self.due_day_vanilla =  (29)
        self.due_day_peach =  (30)
        self.due_day_passion_fruit =  (30)
        self.due_month_vanilla = (6)
        self.due_month_peach = (6)
        self.due_month_passion_fruit = (6)
        self.due_year_vanilla = (2023)
        self.due_year_peach = (2023)
        self.due_year_passion_fruit = (2023)
    
    def greet(self):
        print("-------Bienvenido a la Heladeria-----------------------")

    
    def new_stock_vanilla(self):
        if  int(vanilla_icecream.n_vanilla_ice)/2 > new_vanilla_icecream and now > vanilla_date :
          print("es necesario comprar mas helados de Vainilla")
        
        else:
            print("todavia no es necesario comprar mas helados de Vainilla")
    
    def new_stock_peach(self):
        if int(peach_icecream.n_peach_ice)/2 > new_peach_icecream and now > peach_date:
            print("es necesario comprar mas helados de Durazno")
        else:
            print("todavia no es necesario comprar mas helados de Durazno")
        
    def new_stock_passion(self):
        if int(passionfruit_icecream.n_passion_fruit_ice)/2 > new_passionfruit_icecream and now > passion_fruit_date:
            print("es necesario comprar mas helados de Maracuya")
        else:
            print("todavia no es necesario comprar mas helados de Maracuya")
        
    

vanilla_icecream = Heladeria()
print(vanilla_icecream.greet())


print("Fecha actual:")
now = datetime.now()
print(now)


vanilla_date = datetime(2023, 6, 29)
print(f"fecha de vencimiento helado de Vainilla: {vanilla_date}")
peach_date = datetime(2023, 6, 30)
print(f"fecha de vencimiento helado de Durazno: {peach_date}")
passion_fruit_date = datetime(2023, 6, 30)
print(f"fecha de vencimiento helado de Maracuya: {passion_fruit_date}")



print("--------------Inventario Inicial--------------------------------")
print(f"Cantidad helados de Vainilla: {vanilla_icecream.n_vanilla_ice} ") 

peach_icecream = Heladeria()
print(f"Cantidad helados de Durazno: {peach_icecream.n_peach_ice} ")   

passionfruit_icecream = Heladeria()
print(f"Cantidad helados de Maracuya: {passionfruit_icecream.n_passion_fruit_ice} ")  




print("--------------Inventario actual---------------------------------")

new_vanilla_icecream = int(input("Cantidad de helados de vainilla sobrantes:\n"))
new_peach_icecream = int(input("Cantidad de helados de durazno sobrantes:\n"))
new_passionfruit_icecream = int(input("Cantidad de helados de maracuya sobrantes:\n"))

print(vanilla_icecream.new_stock_vanilla())
print(peach_icecream.new_stock_peach())
print(passionfruit_icecream.new_stock_passion())


