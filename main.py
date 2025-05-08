import numpy as np
import random
from utils import (
    crear_tablero, colocar_barcos, disparar, tablero_visible, todos_barcos_hundidos
)

def pedir_casilla():
    while True:
        try:
            fila = int(input("Introduce fila (0-9): "))
            col = int(input("Introduce columna (0-9): "))
            if 0 <= fila < 10 and 0 <= col < 10:
                return (fila, col)
            else:
                print("Coordenadas fuera de rango.")
        except ValueError:
            print("Entrada inválida.")

def main():
    print(" ¡Bienvenido a Batalla Naval!")
    
    jugador_tablero = crear_tablero()
    maquina_tablero = crear_tablero()
    
    colocar_barcos(jugador_tablero)
    colocar_barcos(maquina_tablero)

    turnos = 0
    while True:
        print("\nTu tablero:")
        print(jugador_tablero)

        print("\nTablero enemigo (visible):")
        print(tablero_visible(maquina_tablero))

        print("\n🔍 Tu turno:")
        casilla = pedir_casilla()
        disparar(casilla, maquina_tablero)

        if todos_barcos_hundidos(maquina_tablero):
            print("🎉 ¡Has ganado!")
            break

        print("\n🤖 Turno de la máquina...")
        while True:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            if jugador_tablero[fila, col] in ["_", "O"]:
                disparar((fila, col), jugador_tablero)
                break

        if todos_barcos_hundidos(jugador_tablero):
            print(" La máquina ha ganado...")
            break

        turnos += 1
        print(f"\n--- Fin del turno {turnos} ---")

if __name__ == "__main__":
    main
