def contar_caracteres(cadena):
    # Creamos un diccionario vacío para almacenar las apariciones de cada carácter
    contador = {}

    # Recorremos cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter ya está en el diccionario, aumentamos su contador
        if caracter in contador:
            contador[caracter] += 1
        # Si el carácter no está en el diccionario, lo agregamos con contador 1
        else:
            contador[caracter] = 1

    return contador

cadena = input("Ingresa una cadena: ")

# Llamamos a la función contar_caracteres para obtener el diccionario de apariciones
resultado = contar_caracteres(cadena)

print("Apariciones de cada carácter:")

# iteramos a través de los elementos del diccionario resultado. El método items() del diccionario nos da pares clave-valor durante la iteración. 
# En este caso, cada par clave-valor representa un carácter en la cadena (caracter) y el número de apariciones de ese carácter (apariciones).
for caracter, apariciones in resultado.items():
    print(f"'{caracter}': {apariciones}")