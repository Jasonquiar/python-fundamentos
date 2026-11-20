# Un módulo es simplemente un archivo .py que contiene funciones, variables o clases
# que podemos reutilizar en otros archivos usando "import".
# Este archivo (operaciones.py) es nuestro módulo con operaciones matemáticas básicas.

# Recibe dos números y devuelve su suma
def sumar(a,b):
    return a + b

# Recibe dos números y devuelve la resta (a menos b)
def restar(a,b):
    return a - b

# Recibe dos números y devuelve su multiplicación
def multiplicar(a,b):
    return a * b

# Recibe dos números y devuelve la división (a entre b)
# Ojo: "/" siempre devuelve un float (ej: 10 / 5 = 2.0)
# y si b es 0 Python lanza un error ZeroDivisionError
def dividir(a,b):
    return a / b
