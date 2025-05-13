import random
import sys

OPCIONES = ["piedra", "papel", "tijera"]

def comparar(jugada1, jugada2):
    """Compara dos jugadas y devuelve el resultado."""
    if jugada1 == jugada2:
        return 0
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
        (jugada1 == "papel" and jugada2 == "piedra") or \
        (jugada1 == "tijera" and jugada2 == "papel"):
        return 1
    else:
        return -1

def validar_jugadas(jugadas):
    if len(jugadas) != 3:
        print("Error: Debes ingresar exactamente 3 jugadas.")
        return False
    
    for jugada in jugadas:
        if jugada not in OPCIONES:
            print(f"Error: '{jugada}' no es una opción válida. Debe ser 'piedra', 'papel' o 'tijera'.")
            return False
    
    return True

def main():
    if len(sys.argv) != 4:
        sys.exit(1)
    
    jugada_humano = sys.argv[1:4]
    
    if not validar_jugadas(jugada_humano):
        sys.exit(1)
    
    jugada_programa = [random.choice(OPCIONES) for _ in range(3)]
    print("\nEl programa elige:", " ".join(jugada_programa))
    
    puntaje_humano = 0
    puntaje_programa = 0
    
    for i, (humano, programa) in enumerate(zip(jugada_humano, jugada_programa), 1):
        resultado = comparar(humano, programa)
        print(f"\nRonda {i}: {humano} vs {programa}")
        if resultado == 1:
            print("  Ganaste esta ronda!")
            puntaje_humano += 1
        elif resultado == -1:
            print("  Perdiste esta ronda.")
            puntaje_programa += 1
        else:
            print("  Empate.")
    
    print(f"\nPuntuación final: Humano {puntaje_humano} - {puntaje_programa} Programa")
    
    if puntaje_humano > puntaje_programa:
        print("¡Felicidades! Ganaste el juego.")
    elif puntaje_programa > puntaje_humano:
        print("Lo siento, el programa ganó esta vez.")
    else:
        print("El juego terminó en empate.")

if __name__ == "__main__":
    main()