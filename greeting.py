def funcion(input):
    if "Hola" in input:
        return "Hola, Como estas? "
    else:
        return "No entendi "

def main():
    texto = funcion("Hola")
    print(texto + "David")

main()