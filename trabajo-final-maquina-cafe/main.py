
# Con esto nos encargamos de importar las funciones mostrar_menu(), pedir_cafe() y ver_historial() 
# desde los archivos menu.py, pedidos.py e historial.py respectivamente.
from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    # Utilizamos un bucle while True para que el programa se ejecute de manera continua hasta que el usuario decida salir.
    while True:
        # llamamos a la funcion mostrar_menu() desde el archivo menu.py para mostrar las opciones al usuario.
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        # Como creaomos las opciones del menu del 1 al 3, usamos un condicional if para verificar que la opcion ingresada sea valida y ejecutar la funcion correspondiente.
        if opcion == "1":
            # Llamamos a la funcion pedir_cafe() un modulo llamado pedidos.py, que se encarga de pedir el cafe al usuario y guardar el pedido en un archivo de texto.
            pedir_cafe()
        elif opcion == "2":
            # Llamamos a la funcion ver_historial() un modulo llamado historial.py, que se encarga de leer el archivo de texto donde se guardan los pedidos y mostrar el historial de pedidos al usuario.
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros riquísimos cafés")
            # Este break nos permite salir del bucle while True y finalizar el programa.
            break
        # Este else nos permite manejar el error en caso de que el usuario ingrese una opcion invalida, es decir, que no sea 1, 2 o 3.
        else:
            print("Opción inválida, por favor indique una de las opciones sugeridas")

# Python tiene una forma de identificar el pundo de inicio de un programa,
# que es el condicional if __name__ == "__main__":, que nos permite ejecutar el programa solo si se ejecuta directamente y no si se importa como un modulo en otro programa.
if __name__ == "__main__":
    main()
# Con esta linea hacemos que el programa inicies desde este archivo y no desde otro archivo que importe este archivo como un modulo.