# Esto es un programa de Referencia para el taller de Python
# Autor: Jose Ariel Fallas Pizarro
# Clase 2: Tipos de Datos


import math 			  # Estoy importando una libreria

Booleano = False	   	  # Creo una variable booleana

Entero = 10			  # Creo una variable tipo entera
Decimal = 10.45			  # Variable tipo flotante	
Texto = "Esto es un String"	  # Creo un String

Lista = [Booleano,Entero,Decimal,Texto] # Creo una lista de Elementos distintos


# Para acceder a los elementos necesito hacerlo mediante un ciclo for
# El for es un poco distinto a los otros lenguajes de programacion, aqui
# Se accede al elemento directamente, no tiene iterador.

print("Inicio el for \n")
for elemento in Lista:
	i = 0				
	print("Estoy en el elemento:",i ) 
	print("\n y accedo a un elemento de tipo: ",type(elemento))
	print("\n")							 # Esto es un Salto
	i = i+1	
print("Fin del for \n")

if(Booleano != True):							# Condicion de Entrada if
	Booleano = True		
else:									# Condicion default
	print("Estoy en la condicion por default")			

while(Booleano == True):						# Esta es la condicion del while
	print("Estoy dentro del While")
	Booleano = False
	print("Cambio el valor de Boleano")

print("Salgo del while")
print("Fin del Programa") 
				
	
