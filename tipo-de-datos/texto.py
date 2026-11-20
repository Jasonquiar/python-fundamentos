# Esta libreria nos permite usar funciones matematicas como sin(), cos(), tan(), etc.
# La matematica empieza a ser util con estas librerias, ya que nos permiten hacer calculos mas complejos y precisos.
from math import sin

# Si queremos usar comillas dentro de un texto, podemos usar comillas simples o dobles para definir el texto.
# Si usamos inicialmente comillas simples, podemos usar comillas dobles dentro del texto y viceversa.
print('Hola "Mundo"')

# Para el ingles que suele usar comillas simples, podemos usar comillas dobles para definir el texto y comillas simples dentro del texto.
ingles = "I'm Sergie"

# Usando comillas triples podemos definir un texto que ocupe varias lineas y que contenga comillas simples y dobles sin problemas.
multiples = """Hola
Mundo
desde
las
comillas
triples"""

print(ingles) #imprime: I'm Sergie
print(multiples) #imprime respetando los saltos de linea y las comillas simples y dobles.

# METODOS
# Los Metodos nos permiten manipular los textos de diferentes maneras, como convertir a mayusculas, minusculas, eliminar espacios, etc.
# 👇 Con len() podemos obtener la longitud de un texto, es decir, el numero de caracteres que contiene.
palabra = "Murciélago"
print(len(palabra)) #imprime: 10, ya que la palabra "Murciélago" tiene 10 caracteres.

# 👇 Metodo para saber si un texto contiene una palabra o no, usando in y not in.
# 👁️ Los metodos son sensible a mayusculas y minusculas, por lo que "python" no es igual a "Python".
texto = "Este curso es de Fundamentos de Python"

# El metodo "in" nos permite saber si un texto contiene una palabra o no, devolviendo True o False.
estaIncluda = "Python" in texto 
print(estaIncluda) # imprime: True, ya que "Python" está en el texto.

# El metodo "not in" nos permite saber si un texto no contiene una palabra o no, devolviendo True o False.
noEstaIncluida = "Javascript" not in texto
print(noEstaIncluida) #imprime: True, ya que "Javascript" no está en el texto.

 # 👇 Metodos para convertir un texto a mayusculas y minusculas.
# Usamos la variable para asignar el texto a una nueva variable y luego usamos los metodos upper() y lower() para convertir el texto a mayusculas y minusculas respectivamente.
mayuscula = texto.upper() # Metodo para convertir un texto a mayusculas.
minuscula = texto.lower() # Metodo para convertir un texto a minusculas.

# 👁️ Si no diferenciamos la variable podriamos estar sobre escribiendo sobre la variable original y perder el valor original del texto, por lo que es recomendable usar una nueva variable para almacenar el resultado de los metodos.
texto2 = texto.upper()
texto2 = texto.lower()

print(texto2) # En este caso imprimira la ultima asignacion, que es el texto en minusculas.

# 👇 Metodo para eliminar los espacios al inicio y al final de un texto.
# strip() nos permite eliminar los espacios al inicio y al final de un texto, pero no elimina los espacios entre palabras.
espacios = "        Este es el texto         "
sinEspacios = espacios.strip()

print(sinEspacios) # Imprime: "Este es el texto"

# Se usa en el caso de password donde el usuario puede ingresar espacios al inicio o al final del password y no queremos que eso afecte la validacion del password.