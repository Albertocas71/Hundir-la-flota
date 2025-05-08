import numpy as np
import random

def crear_tablero(tamaño=10):
    return np.full((tamaño, tamaño), "_")

def colocar_barco(barco, tablero):
    for fila, col in barco:
        tablero[fila, col] = "O"

def disparar(casilla, tablero):
    fila, col = casilla
    if tablero[fila, col] == "O":
        tablero[fila, col] = "X"
        print(f"¡Tocado en {casilla}!")
        return "Tocado"
    elif tablero[fila, col] == "_":
        tablero[fila, col] = "A"
        print(f"Agua en {casilla}.")
        return "Agua"
    else:
        print(f"Ya disparaste en {casilla}.")
        return "Repetido"

def crear_barco(eslora, tamaño=10):
    while True:
        orientacion = random.choice(["H", "V"])
        if orientacion == "H":
            fila = random.randint(0, tamaño - 1)
            col = random.randint(0, tamaño - eslora)
            barco = [(fila, col + i) for i in range(eslora)]
        else:
            fila = random.randint(0, tamaño - eslora)
            col = random.randint(0, tamaño - 1)
            barco = [(fila + i, col) for i in range(eslora)]
        return barco

def validar_barco(barco, tablero):
    for fila, col in barco:
        if tablero[fila, col] != "_":
            return False
    return True

def colocar_barcos(tablero):
    barcos_info = [2]*3 + [3]*2 + [4]
    barcos_colocados = []
    
    for eslora in barcos_info:
        while True:
            barco = crear_barco(eslora)
            if validar_barco(barco, tablero):
                colocar_barco(barco, tablero)
                barcos_colocados.append(barco)
                break
    return barcos_colocados

def tablero_visible(tablero):
    """Copia el tablero ocultando los barcos (O) como agua (_)."""
    visible = tablero.copy()
    visible[visible == "O"] = "_"
    return visible

def todos_barcos_hundidos(tablero):
    return not np.any(tablero == "O")

