"""

    #primer ejemplo
    name = input("Ingrese su Nombre: ")
    print("Bienvenido, ", name)
    #ahora lo mismo, pero modificando la funcion PRINT
   
    #viendo la documentacion oficial de python
    #el print --> contiene un espacio (SEP = ' ',) y un salto de linea (END = "\n")
    
    print("Bienvenido, ", end="")
    #ya con eso, se elimina el salto de linea y se muestra todo en una sola
    print (name)

    #con esto, podemos modificar practicamente las propias funciones de python, si usamos tipo:
    print("Bienvenido, ", end="$$$")
    print (name)
    #si quiero hacer esto:
    #   print ("Hola, "Amigo"") 
    #nos saldra error, se soluciona asi:
    print("Hola, \"Amigo\"")
    #F-STRING
    print("----------------------")
    #se puede presentar el primer problema todo dentro de la misma linea de caractrres (dentro de las "")
    #pero se debe poner una f al principio
    print(f"Hola, {name}")
    #metodos
    #usar una funcion de python en una funcion mia, ahi se convierte en un metodo
    alter_name = input("Ingrese otro nombre: ")
    #quitar espacios
    #alter_name = alter_name.strip()
    #poner la pimera letra de cada palabra en mayuscula
    #alter_name = alter_name.title()


    #puedo hacer esas dos en la misma
    alter_name = alter_name.strip().title()
    print(f"Hola, {alter_name}")

x=int(input("primer numer= "))
y=int(input("segundo numero"))
print(x+y)

#float
x=float(input("primer numer= "))
y=float(input("segundo numero"))
print(x+y)
#round
#este sirve pa redondear valores decimales
#   round(number[, ndigits])
#los corchetes aqui significan que es opcional, en este caso especificar la cantidad a redondear
z=round(x+y)

print(z)
#este es para que se muestra con una "," para la representacion de mil
print(f"{z:,}")
#ahora con una division con los mismos valores antes ingresados
print("div")
z = x/y
#de esta forma estamos limitando la cantidad de decimales que se mostraran
print(f"{z:0.2f}")
""" 
#FUNCION --> DEF
"""
def hola():
    print("Hola")

nombre=input("Ingrese su nombre: ")
hola()
print (nombre)
"""
# vamos a pasarle parametros
"""
def hola(_nombre):
    print("Hola, ", _nombre)

nombre = input("Ingrese su nombre: ")
hola(nombre)
"""
# vamos a asignar un valor por defecto para el parametro
# en este caso, si se llama a la funcion HOLA, pero no se usa el argumento, se presenta
#"Persona Anonima"

def hola(_nombre="Persona Anonima"):
    print("Hola, ", _nombre)
#LAS FUNCIONES, DEBEN ESTAR SIEMPRE EN LA PARTE SUPERIOR
#asi el programa las lee y ven que si estan definidas, para despues 
#poder trabajar con ellas
nombre = input("Ingrese su nombre: ")
hola()

#ahora usando una funcion principal

def main():
    nombre = input("Ingrese su nombre: ")
    hola(nombre)

def hola(_nombre="Persona Anonima"):
    print("Hola, ", _nombre)

#esto asi solo no hace nada, asi que debemos llamar a la funcion para que ejecute por asi decirlo
main()

#return
def main():
    x = int(input("Ingrese valor de X: "))
    print(calc_cuadrado(x))

def calc_cuadrado(_x):
    return(_x*_x) 

main()



