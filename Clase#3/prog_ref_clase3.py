import math
Var_Global = 0.0		# Variable globarl, cualquier funcion tiene acceso a los parametros de esta funcion
x = False				# Esto tambien es una variable global

def Function1(Parameter_a,Parameter_b):

	"""Funcion que calcula el coseno de la suma de dos parametros si la variable
	global x es true, si no retorna un 0"""
	
	global x			# utilizo la variable global aqui	
	if(x==True):
		n = Parameter_a+Parameter_b	
		result = math.cos(n)
	else:
		result = "Variable global x es False"   					


	return result

def Function2():	
	"""Esta funcion no recibe parametros"""
	local_var = 10		# Esto es una variable local 
						# Niniguna otra funcion tiene acceso a esta variables

	return local_var

def main():	
	a = 20			
	b = 10

	r=Function1(a,b)
	Valor_F2 = Function2()

	print("El valor de retorno de Function1 es:",r)
	print("El valor de retorno de Function2 es:",Valor_F2)


if __name__ == '__main__':		
	"""Esto equivale a la funcion principal
	en caso de que se requiera puedo detener la 
	ejecucion del programa mediante las teclas (ctrl+c)"""

	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
