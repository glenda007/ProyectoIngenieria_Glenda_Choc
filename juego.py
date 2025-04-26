import random

def menu():
    opciones = ["piedra", "papel", "tijera", "salir"]
    partidas = 0
    nombre = input("Ingrese su nombre: ")
    computadora = "computadora"
    empates = 0
    ganador_final = ""

    while partidas < 3 and empates < 2:
        usuario = input("Elige piedra, papel, tijera").lower()

        if usuario == 'salir':  
            print("Estas salidendo del programa")
            break 

        compu = random.choice(opciones)

        if usuario in opciones:
            print(f"{nombre} eligió: {usuario}")
            print(f"{computadora} eligió: {compu}")

            if usuario == compu:
                print("Empate!")
                empates = empates + 1
            elif (usuario == "piedra" and compu == "tijera") or (usuario == "papel" and compu == "piedra") or (usuario == "tijera" and compu == "papel"):
                print(f"!{nombre} gana esta ronda¡")
            else:
                print(f"!{computadora} gana esta ronda¡")

            partidas = partidas + 1

        if empates == 2:
            print("Se han jugado 3 partidas y ha habido empate en todas. Se jugará una partida adicional para determinar al ganador definitivo.")
        while ganador_final == "":
            usuario = input("Elige piedra, papel, tijera o salir: ").lower()
            compu = random.choice(opciones)

            if usuario in opciones:
                print(f"{nombre} eligió: {usuario}")
                print(f"{computadora} eligió: {compu}")

                if usuario == compu:
                    print("Empate!")
                elif (usuario == "piedra" and compu == "tijera") or (usuario == "papel" and compu == "piedra") or (usuario == "tijera" and compu == "papel"):
                    print(f"!{nombre} gana esta ronda¡")
                    ganador_final = nombre
                else:
                    print(f"!{computadora} gana esta ronda¡")
                    ganador_final = computadora

    print(f"Se han jugado {partidas} partidas.")
    if ganador_final:
        print(f"El ganador definitivo es: {ganador_final}")
    else:
        print("No hay un ganador definitivo aún. ¡Sigue jugando!")

menu()