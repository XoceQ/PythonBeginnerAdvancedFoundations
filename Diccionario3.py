class Tienda:
    
    def __init__(self):
        self.productos = {"Aceite": [5800,50], "Atún":[5000,65], "Café":[6350,100], "Azúcar":[4890,20]}
    
    def agregar_producto(self, nombre, precio, existencias):
        if nombre in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[nombre] = [precio, existencias]
            print(f"Producto '{nombre}' agregado al inventario.")
    
    def actualizar_precio(self, nombre, nuevo_precio):
        if nombre in self.productos:
            self.productos[nombre][0] = nuevo_precio #[0] se refiere al primer elemento de la lista, que es el precio actual del producto. Se asigna el nuevo_precio a esta posición, actualizando así el precio del producto en el inventario.
            print(f"Precio del producto '{nombre}' actualizado.")
        else:
            print("Producto no encontrado en el inventario.")
    
    def mostrar_inventario(self):
        print("Inventario:")
        for nombre, detalles in self.productos.items():#estamos iterando a través de los elementos del diccionario self.productos.
            precio, existencias = detalles #el método items() nos proporciona pares clave-valor durante la iteración.
            print(f"{nombre}: Precio: ${precio:}, Existencias: {existencias}")

    
    
tienda = Tienda()
tienda.mostrar_inventario()

tienda.agregar_producto("Leche",3500,25)

tienda.actualizar_precio("Café",7000)

tienda.mostrar_inventario()

