import numpy as np
import random 

#TABLERO
tablero = np.full((10, 10)," ")
print(tablero)

#COLOCACIÓN ALEATORIA DE LOS BARCOS    (No acaba de funcionar)

lista_esloras = [1,1,1,1,2,2,2,3,3,4]
barcos_colocados=0

for eslora in lista_esloras:
    while barcos_colocados < len(lista_esloras):
        orientacion = random.choice(['E', 'O', 'N', 'S'])
        fila = np.random.randint(0,10)
        columna= np.random.randint(0,10)
        if orientacion == 'E' and 0 <= columna + eslora < 10 and 'O' not in tablero[fila, columna: columna + eslora]:
            tablero[fila, columna: columna + eslora] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'O' and 0 <= columna - eslora < 10 and 'O' not in tablero[fila, columna: columna - eslora:-1]:
            tablero[fila, columna - eslora + 1:columna + 1] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in tablero[fila - 1, columna:columna + 1]:
            tablero[fila - eslora + 1:fila + 1, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in tablero[fila:fila + eslora, columna]:
            tablero[fila:fila + eslora, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        else:
            continue
print(tablero)

