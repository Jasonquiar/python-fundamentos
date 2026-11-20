# Colocamos como constante el nombre del archivo donde se guardaran los pedidos, para que si en algun momento queremos cambiar el nombre del archivo, 
# solo tengamos que cambiarlo en un solo lugar y no en todo el codigo.
ARCHIVO_PEDIDOS = "pedidos.txt"

# Este modulo contiene la funcion pedir_cafe() que se encarga de pedir el cafe al usuario y guardar el pedido en un archivo de texto.
def pedir_cafe():
    print("\n Elige el café que prefieras: ")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Opción: ")

    cafes = {
        "1": "Espresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    # Creamos un condicional if para verificar que la opcion ingresada sea valida y ejecutar la funcion correspondiente.
    # Comparamos la opcion del usuario contra la biblioteca de cafes
    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + ". ¡Preparando tu café!")

        # Aca guardamos el historia de pedidos en un archivo de texto llamado pedidos.txt, que se encuentra en la misma carpeta que este archivo.
        # El modo "a" nos permite abrir el archivo en modo append, es decir, que si el archivo ya existe, se agregara el nuevo pedido al final del archivo sin borrar los pedidos anteriores.
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción no es válida por favor intenta de nuevo")