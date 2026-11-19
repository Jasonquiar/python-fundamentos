# Asi puedes crear una variable en python, recuerda que no es 
# necesario declarar el tipo de dato de la variable ya que python es un lenguaje de tipado dinamico.
x = "Esta es una variable"

# Podriamos imprimir la variable de la siguiente manera 👇
print("Esta es una viariable")
# la variable nos es util porque podemos reutilizarla
#  en cualquier parte de nuestro código, por ejemplo 👇
print(x)

# Si por alguna razon sobreescribes en la variable, python tomará el nuevo valor de la variable, por ejemplo 👇
x = "Esta es otra variable"

# Debes tener cuidaddo de reescribir y obtener un resultado no deseado

# Si se utiliza una variable en minusculas y otra en mayusculas, python las considerará como variables diferentes, por ejemplo 👇
# ya que Python es Case Sensitive, es decir, distingue entre mayúsculas y minúsculas.
X = "Esta es OTRA variable"
print(x)

#Esta es la forma en que se recomienda nombrar las variables en python, es decir, en minusculas y si es necesario separar palabras se utiliza el guión bajo "_", por ejemplo 👇
mivariable = "Esta es una variable"
mi_variable = "Esta es una variable con guión bajo"
_mi_variable = "Esta variable comienza con un guión bajo"
miVariable = "Otra varible"
MIVARIABLE = "Todo mayus"
mivariable2 = "Otra variable más"

#Esta es la forma en que NO se recomienda nombrar las variables en python, ya que no es legible y puede causar errores, por ejemplo 👇
2variable = "No se puede utilizar esta forma"
mi-variable = "No se puede utilizar guión medio"
mi variable = "No se puede utilizar espacios"


#Estos son los estilos de nombramiento de variables que se utilizan en python, por ejemplo 👇
camelCase = "Comienza con minúscula y el resto de las palabras con mayúscula"
PascalCase = "Comienza con mayúscula y el resto de las palabras también siguen en mayúscula"
snake_case = "Se separan las palabras con guiones bajos"