import random

opciones = ["piedra", "papel", "tijera"]

def comparar(jugada1, jugada2):
    if jugada1 == jugada2:
        return 0
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
        (jugada1 == "papel" and jugada2 == "piedra") or \
        (jugada1 == "tijera" and jugada2 == "papel"):
        return 1
    else:
        return -1

def main():
    puntaje_humano = 0
    puntaje_programa = 0

    print("PIEDRA, PAPEL Y TIJERA") 
    print("Se jugarán 3 partidas. Escribe 'piedra', 'papel' o 'tijera' en cada una.\n")

    for ronda in range(1, 4):
        while True:
            jugada_humano = input(f"Partida {ronda} - Tu jugada: ").strip().lower()
            if jugada_humano in opciones:
                break
            else:
                print("Error: Entrada inválida. Solo se permite: piedra, papel o tijera.")

        jugada_programa = random.choice(opciones)
        print(f"Partida {ronda} - El programa juega: {jugada_programa}")

        resultado = comparar(jugada_humano, jugada_programa)
        if resultado == 1:
            puntaje_humano += 1
            print("Resultado: Gana el Humano")
        elif resultado == -1:
            puntaje_programa += 1
            print("Resultado: Gana el Programa")
        else:
            print("Resultado: Empate")

        print(f"Puntaje hasta ahora -> Humano: {puntaje_humano}, Programa: {puntaje_programa}\n")

    print("***** RESULTADO FINAL *****")
    print(f"Punteo final: Humano {puntaje_humano} - Programa {puntaje_programa}")
    if puntaje_humano > puntaje_programa:
        print("Ganador final: Humano")
    elif puntaje_programa > puntaje_humano:
        print("Ganador final: Programa")
    else:
        print("Resultado final: Empate")

if __name__ == "__main__":
    main()