import numpy as np
import random 

#TABLEROS



def colocar_barcos(tablero,lista_esloras):



#Tablero vacío
tablero = np.full((10, 10)," ")
print(tablero)

#Tablero de la máquina
tablero_maquina = np.full((10, 10)," ")

#Tablero jugadorx
tablero_jugadorx = np.full((10, 10)," ")

#COLOCACIÓN ALEATORIA DE LOS BARCOS EN EL TABLERO DE LA MÁQUINA 
lista_esloras = [1,1,1,1,2,2,2,3,3,4]
barcos_colocados=0

for eslora in lista_esloras:
    while barcos_colocados < len(lista_esloras):
        orientacion = random.choice(['E', 'O', 'N', 'S'])
        fila = np.random.randint(0,10)
        columna= np.random.randint(0,10)
        if orientacion == 'E' and 0 <= columna + eslora < 10 and 'O' not in tablero_maquina[fila, columna: columna + eslora]:
            tablero_maquina[fila, columna: columna + eslora] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'O' and 0 <= columna - eslora < 10 and 'O' not in tablero_maquina[fila, columna: columna - eslora:-1]:
            tablero_maquina[fila, columna - eslora + 1:columna + 1] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in tablero_maquina[fila - 1, columna:columna + 1]:
            tablero_maquina[fila - eslora + 1:fila + 1, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in tablero_maquina[fila:fila + eslora, columna]:
            tablero_maquinafila:fila + eslora, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        else:
            continue
tablero_maquina


#COLOCACIÓN ALEATORIA DE LOS BARCOS EN EL TABLERO DE JUGADORX
lista_esloras = [1,1,1,1,2,2,2,3,3,4]
barcos_colocados=0

for eslora in lista_esloras:
    while barcos_colocados < len(lista_esloras):
        orientacion = random.choice(['E', 'O', 'N', 'S'])
        fila = np.random.randint(0,10)
        columna= np.random.randint(0,10)
        if orientacion == 'E' and 0 <= columna + eslora < 10 and 'O' not in tablero_jugadorx[fila, columna: columna + eslora]:
            tablero_jugadorx[fila, columna: columna + eslora] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'O' and 0 <= columna - eslora < 10 and 'O' not in tablero_jugadorx[fila, columna: columna - eslora:-1]:
            tablero_jugadorx[fila, columna - eslora + 1:columna + 1] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in tablero_jugadorx[fila - 1, columna:columna + 1]:
            tablero_jugadorx[fila - eslora + 1:fila + 1, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in tablero_jugadorx[fila:fila + eslora, columna]:
            tablero_jugadorx[fila:fila + eslora, columna] = 'O'
            barcos_colocados = barcos_colocados +1
            break
        else:
            continue
tablero_jugadorx

#DURANTE EL JUEGO
Jugadorx va modificando el tablero de la máquina
La máquina va modificando el tablero de jugadorx



#BUCLE PRINCIPAL

while "O" in tablero_jugadorx or "O" in tablero_maquina:  

    turno_jugadorx(tablero_maquina)

    if fin_partida(tablero_jugadorx, tablero_maquina):
        break
 


 
    turno_maquina(tablero_jugadorx)

    if verificar_ganador(tablero_jugadorx, tablero_maquina)
        break

    

def turno_jugadorx(tablero_maquina):
    if turno_jugadorx:
        coordenada1= input("Dime un numero",)
        coordenada1= input("Dime un numero",)
        disparo (coordenada1,coordenada2)

def turno_maquina(tablero_jugadorx):
    if turno_maquina:
        coordenada1 = np.random.randint(0, 10)
        coordenada2 = np.random.randint(0, 10)
        disparo (coordenada1,coordenada2)



elif "O" not in tablero_jugadorx :
    print("¡Perdiste!")
    
elif "O" not in tablero_maquina:   #Jugadorx gana cuando todos los "O" se han convertido en "X" en el tablero de la maquina
    print("¡Ganaste!")







#DISPAROS
def disparo (coordenada1,coordenada2):
    if tablero[coordenada1,coordenada2]== " ":
        tablero[coordenada1,coordenada2]= "_"
        print("¡Agua!")
        print(tablero)
        break
    if tablero[coordenada1,coordenada2]== "O":
        tablero[coordenada1,coordenada2]= "X"
        print("¡Tocado!")
        print(tablero)
        continue


#BUCLE DE DISPAROS
if tablero[coordenada1,coordenada2]= "X":
    disparo(coordenada1,coordenada2)




#FIN DE LA PARTIDA   (se puede hacer todo con un bucle while)
    
def fin_partida(tablero_jugadorx, tablero_maquina):
    if "O" not in tablero_jugadorx :
        print("¡Perdiste!")
    elif "O" not in tablero_maquina:   #Jugadorx gana cuando todos los "O" se han convertido en "X" en el tablero de la maquina
    print("¡Ganaste, humanx!")