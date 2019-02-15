##################################################################
#                                                                #
#      En este programa se estudian algunos tipos de Datos       #
#        asi como algunas operaciones basicas con ellos          #
#                                                                #
##################################################################

# Filename: DataTypes.py
# Author : Jose Ariel Fallas Pizarro
# Este programa esta hecho para correr en python 3

""" Es importante notar que en python no se necesita declarar las variables
	antes de ser inicializadas, esto se refiere a que no necesito definir el
	tipo de variable que va a ser (por ejemplo: String, integer, float, etc) """



# Strings: Se refiere a cadenas de Texto
""" Para definir un string es necesario el uso de doble comilla al inicio y al 
    final de este, tal y como lo muestran el siguiente ejemplo"""

text_1 = "\n Este texto se encuentra almacenado en la variable llamada text_1. "
text_2 = " Este texto esta almacenado en text_2 y tiene un salto de linea al final \n"
text_3 = text_1 + text_2

print(text_1 + text_2)

# Algunas funciones que se pueden realizar con el texto

print(text_1.upper())       # Escribe todos los caracteres en mayuscula
print(text_2.lower())       # Escribe todos los caracteres en minuscula

print(" El tamano del Texto 1 es de " + str(len(text_1)) + " caracteres \n") # len() da como resultado el largo total
                                                                             # del string mientras str lo convierte a
                                                                             # texto.
# Que otras funciones puedo utilizar con strings ? Investigue !


#-----------------------------------------------------------------------------------------------------------------------

# Numeros
""" Existen 3 tipos de numeros: 
    - int (Enteros)
    - float (Decimales)
    - complex (complejos) 
    Se pueden realizar las operaciones tipicas de suma, divisio, multiplicacion, etc. Tambien existen operaciones 
    matematicas mas avanzadas, sin embargo para esto se necesita importar una libreria. Esto lo veremos mas adelante
    """

num1 = 10
num2 = 3

print("Num1 es: "+ str(num1) + "\n Num2 es: " + str(num2))
print(" El resultado de num1 + num2 = " + str(num1 + num2))
print(" El resultado de num1 - num2 = " + str(num1 - num2))
print(" El resultado de num1 * num2 = " + str(num1 * num2))
print(" El resultado de num1 / num2 = " + str(num1 / num2))
print(" El resultado de num1 // num2 = " + str(num1 // num2)) # Se obtiene el cosciente de la division
print(" El resultado de num1 % num2 = " + str(num1 % num2) + " \n \n ")   # Se utiliza para obtener el residuo de la division

# Existe alguna otra funcion integrada ? Investigue sobre las funciones **, pow() y round()
#-----------------------------------------------------------------------------------------------------------------------
# Listas
"""Las Listas en python son muy comunes de utilizar, por ello es importante conocer a que se refieren estas.
    Basicamente una lista es un conjunto de datos (no necesariamente del mismo tipo), los cuales se encuentran
    organizados de alguna manera, y pueden ser modificados por el usuario u otra funcion.
    Estas se denotan con parentesis cuadrados []"""

lista_est = ["Andrea", "Carlos", "Cesar", "Maria", "Jorge", "Marco", "Ericka", "Daniela", "Isabel"]
lista_datos = ["Esto es un str",  10, True]
lista_listas = [lista_datos,lista_est]
print("La lista de estudiantes del curso es: "+ str(lista_est))
print("\n La persona 4 de la lista es " + lista_est[3])
print(" El resultado de num1 * num2 = " + str(num1 * num2))
lista_est.append("Josue")
print("La nueva lista es: " + lista_est.__str__())
print("Esto es otra lista con distintos datos: " + str(lista_datos))

# Cuales otras funciones puedo realizar con una lista ? Investigue !

# Booleanos

""" Los booleanos son variables lque tiene dos unicos posibles valores (True, False), estos son utilizados generalmente
    como banderas para comprobar alguna condicion que se desea revisar. """

Major_Age = True
contidion = False
