"""
i = 1
while i <= 3:
    print("Miau :3")
    # en otros lenguajes (Tmb funciona aqui)
    #i = i+1
    #aqui podemos hacerlo de la siguiente manera:
    i += 1

#ya hemos visto varios datos, pero en python, tmb existen las listas
"""
print("for")
for i in [1, 2, 3]:
    print("miau")
    """   
#en este caso, la lista (i) representa los valores 0, 1, 2
#simplifiquemos esto:
for i in range(3):
    print("miau c:")
#otra forma de hacerlo:

print ("miau .. \n"*3)

while True:
    n = int(input("Ingrese un valor: "))
    if n > 0:
        break

for _ in range(n):
    print("MIAU")

def main():
    number = get_number()
    miau(number)

def get_number():
    while True:
        n = int(input("Ingrese un valor: "))
        if n > 0:
            return n

def miau(n):
    for _ in range(n):
        print("miau")

main()

estudiantes = ["Hermione", "Harry", "Ron"]

for i in estudiantes:
    print(i)

#se puede hacer de otra forma
#usamos la funcion LEN, ya esta no toma los caracteres de la lista, sino q devuelve un valor numerico en base a ellas
for i in range(len(estudiantes)):
    #print(i)
    #si lo hacemos asi, nos mostrara los numeros, entonces debemos poner
    #estudiantes con respecto al numero obtenido (len) para que nos muestre los nombres
    # si ponemos para que se presente el valor de i + 1, se enumerara, se hace asi para que no parta de cero
    print(i +1, estudiantes[i])

#diccionarios
#una lista es un conjunto de multiples valores (uni dimensional)
#pero el diccionario, es bidimensional (como una matriz)
#estudiantes = ["Hermione", "Harry", "Ron", "Draco"]
#casa = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]
#pero podemos hacerlo mejor de esta manera:
estudiantes = {
    "Hermione" : "Griffindor",
    "Harry" : "Griffindor",
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
    }
#lo bueno de las listas, es q no necesitas mumeros, sino q puedes usar palabras claves
for i in estudiantes:
    print(i, estudiantes[i], sep=", ")

#escalamos el codigo
estudiantes = [
    {"Name": "Hermione", "House": "Gryffindor", "patronus": "Otro"},
    {"Name": "Harry", "House": "Griffindor", "patronus": "Stag"},
    {"Name": "Draco", "House": "Slytherin", "patronus": None}
]
for estudiantes in estudiantes:
    print(estudiantes["Name"], estudiantes["House"], estudiantes["patronus"], sep= ", ")
#mas adelante se podran buscar y filtrar datos, para cuando se trabajan con litas, diccionarios y listas 
#de diccionarios mas grandes
"""
#MARIO .PY
"""
print("#\n"*3)

for _ in range(3):
    print("#")

def main():
    print_columna(3)

def print_columna(altura):
    for _ in range(altura):
        print("#")

def main():
    print_fila(4)

def print_fila(ancho):
    print("?" * ancho)

main()
"""
def main():
    print_cuadrado(3)

def print_cuadrado(tamano):
    for i in range(tamano):
        for j in range(tamano):
            print("#", end=" " )
        print()

main()



