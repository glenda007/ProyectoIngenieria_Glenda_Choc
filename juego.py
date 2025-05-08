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
    entrada = input("Ingresa tus 3 jugadas separadas por espacio (piedra papel tijera): ").strip().lower()
    jugada_humano = entrada.split()

    if len(jugada_humano) != 3:
        print("Error: Debes ingresar exactamente 3 jugadas.")
        return

    if not all(j in opciones for j in jugada_humano):
        print("Error: Las jugadas deben ser 'piedra', 'papel' o 'tijera'.")
        return

    jugada_programa = [random.choice(opciones) for _ in range(3)]
    print("El programa elige:", " ".join(jugada_programa))

    puntaje_humano = 0
    puntaje_programa = 0

    for jugadas, programa in zip(jugada_humano, jugada_programa):
        resultado = comparar(jugadas, programa)
        if resultado == 1:
            puntaje_humano += 1
        elif resultado == -1:
            puntaje_programa += 1

    print(f"Punteo: {puntaje_humano} – {puntaje_programa}")

    if puntaje_humano > puntaje_programa:
        print("Ganador: Humano")
    elif puntaje_programa > puntaje_humano:
        print("Ganador: Programa")
    else:
        print("Resultado: Empate")

if __name__ == "__main__":
    main()