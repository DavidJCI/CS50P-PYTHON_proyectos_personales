carita = ":v"

def main():
    #variable global, se la puede usar no solo dentro de la funcion, sino en todo el programa
    global carita
    texto("Hola")
    carita = ":D"
    texto("como estas?")

def texto(_texto):
    print(_texto + " " + carita)

main()