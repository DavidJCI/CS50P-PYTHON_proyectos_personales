def main():
    dificultad = input("Facil o Dificil").title().strip()
    jugadores = input("Solo o Multijugador").title().strip()
    """"
    if dificultad == "Facil":
        if jugadores == "Miltijugador":
            recomendar("Poker")
        elif jugadores == "Solo":
            recomendar("Klondike")
        else:
            print("Ingrese un valor valido")
    elif dificultad == "Dificil":
        if jugadores == "Solo":
            recomendar("Hearts")
        elif jugadores == "Multijugador":
            recomendar("Clock")
        else: 
            print("Ingrese un valor valido")
"""
    if dificultad == "Dificil" and jugadores == "Multijugador":
        recomendar("Poker")
    elif dificultad == "Dificil" and jugadores =="Solo":
        recomendar("klondike")
    elif dificultad == "Facil" and jugadores == "Multijugador":
        recomendar("Hearts")
    elif dificultad == "Facil" and jugadores == "SOlo":
        recomendar("clock")

def recomendar(_recomendar):
    print("Te podria gustar ", _recomendar, "Game")

main()

