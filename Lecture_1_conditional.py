
x = int (input("Ingrese valor para X "))
y = int (input ("Ingrese valor para Y "))

if x > y:
    print("X es mayor que Y")
elif x < y:
    print("X es menor que Y")
else:
    print("Son iguales")

#ejemplo con el or
if x < y or x > y:
    print("Los dos valores NO son iguales")
else: 
    print("Los valores SI son iguales")

#ejemplo con el AND
calificacion = int(input("Calificacion: "))

if calificacion >=90 and calificacion <= 100:
    print("Grado 1")
elif calificacion >=80 and calificacion <= 90:
    print("Grado 2")
elif calificacion >=70 and calificacion <=80:
    print("Grado 3")
else:
    print("Grado F")
#podemos simplificar esto de la siguiente forma:
if 90 <= calificacion <= 100:
    print("Grado 1")
elif 80 <= calificacion <= 90:
    print("Grado 2")
elif 70 <= calificacion <= 80:
    print("Grado 3")
else:
    print("Grado 4")
#si lo hacemos en el mismo orden, se lo puede simplificar aun mas:
if calificacion >=90:
    print("Grado 1")
elif calificacion >=80:
    print("Grado 2")
elif calificacion >=70:
    print("Grado 3")
else:
    print("Grado 4")

def main ():
    x = int(input("Ingrese un valor:"))
    if par_impar(x):
        print("par")
    else:
        print("impar")

def par_impar(_x):
    if _x % 2 == 0:
        return True
    else:
        return False

main()


def main():
    nombre = input("Ingrese su nombre: ")

    match nombre:
        case "Harry" | "Hermione" | "Ron":
            print("Griffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("???")
main()

