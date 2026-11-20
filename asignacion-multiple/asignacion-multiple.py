# Las variasbles se pueden declarar de varias formas, una de ellas es la asignación múltiple.
x,y,z = "Manzana", "Naranja", "Banana"

print(x,y,z) # Se imprimiria Manzana Naranja Banana

# En este caso, las variables a, b y c se les asigna el mismo valor "Mandarina" y tambien funciona
a = b = c = "Mandarina"

print(a,b,c) # Imprimiria Mandarina Mandarina Mandarina

# toma en cuenta como un operador sirve para concatenar cadenas de texto, en este caso se concatenan la cadena "Mi fruta favorita es " con el valor de la variable x
print("Mi fruta favorita es " + x)
print(a + z)

# En este caso, se asigna el valor 5 a la variable d y el valor 6 a la variable e, luego se imprime la suma de ambas variables.
d = 5 
e = 6
print(d + e)

# Ten cuidado de no mezclar tipos de datos, ya que si intentas sumar un número con una cadena de texto,
#  obtendrás un error. Por ejemplo, si intentas hacer print(d + x), obtendrás un error porque estás intentando sumar un número (d) con una cadena de texto (x).