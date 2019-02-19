#####################################################
#   En este programa veremos algunas generalidades  #
#   sobre las funciones en python                   #
#####################################################

# filename: Functions.py
# author : Ariel Fallas Pizarro


def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3.5))

""" Para definir una funcion se debe utilizar el acronimo "def" seguido del nombre de la funcion y dos puntos como se
    presenta en el siguiente ejemplo. Es muy importante seguir la indentacion ya que lo que se encuentre en un
    nivel menor significa que es parte de la funcion """

def GetUserData():
    name = input("Digite el nombre del usuario: ")
    age = int(input("Digite la edad del usuario: "))
    id = input("Digite el ID del usuario: ")
    return [name,age,id]

#-----------------------------------------------------------------------------------------------------------------------
usersList = []                                  # Se crea una lista vacia la cual contendra los datos del usuario
userData1 = GetUserData()                       # Se pide que ingrese el usuario 1
userData2 = GetUserData()                       # Se pide que ingrese el usuario 2
usersList.append(userData1)                     # Se ingresa el usuario 1 a la lista
usersList.append(userData2)                     # Se ingresa el usuario 2 a la lista

print(usersList)
#-----------------------------------------------------------------------------------------------------------------------

""" Esta es una manera mas eficiente de hacer el codigo anterior. Aqui unicamente se debe modificar la variable n para
    ingresar el numero de usuarios que desee"""

n = 2
usersList = [None]*n
for i in range(n):
    usersList[i] = GetUserData()
    print("")

ls