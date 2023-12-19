# Tamaño del tablero
tamano_tablero = 10
# Crear el tablero
tablero = []
for _ in range(tamano_tablero):
    tablero.append(['O'] * tamano_tablero)
# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para colocar los barcos en posiciones aleatorias
from random import randint
def colocar_barcos(tablero, num_barcos):
    for _ in range(num_barcos):
        fila_barcos = randint(0, tamano_tablero-1)
        columna_barcos = randint(0, tamano_tablero-1)
        if tablero[fila_barcos][columna_barcos] == "B":
            continue
        tablero[fila_barcos][columna_barcos] = "B"

# Función para pedir al jugador que elija una fila y columna
def elegir_posicion():
    fila = int(input("Elige una fila (0-10): "))
    columna = int(input("Elige una columna (0-10): "))
    return fila, columna

def jugar(tablero):
    num_barcos = int(input("¿Cuántos barcos quieres en el tablero? "))
    colocar_barcos(tablero, num_barcos)
    mostrar_tablero(tablero)
    num_intentos = 0
    num_barcos_hundidos = 0
    while num_barcos_hundidos < num_barcos:
        print(f"Intento #{num_intentos+1}")
        fila, columna = elegir_posicion()
        if tablero[fila][columna] == "B":
            print("¡Hundiste un barco!")
            tablero[fila][columna] = "X"
            num_barcos_hundidos += 1
    else:
        print("Agua")
        num_intentos += 1
        mostrar_tablero(tablero)
        print("¡Ganaste!")

# Jugar al juego
jugar(tablero)