# En Python, None es un valor especial que representa la ausencia de un valor o un valor nulo.
x = None 

print(x) # Imprime None, que nos indica que la variable x no tiene un valor asignado.
print(type(x)) # Imprime <class 'NoneType'>

# Esto es importante saberlo en Python porque hay funciones que pueden devolver None
# si no tienen un valor de retorno, asi en el codigo podemos hacer revisiones 
# para saber si una variable tiene un valor asignado o no.

print(type(""))
print(type(0))
print(type(False))
print(type([]))