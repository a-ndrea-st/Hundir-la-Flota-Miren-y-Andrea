import numpy as np
import random 

#TABLEROS: 4 tableros: 2 de máquina y 2 de jugadorx

#FUNCIÓN PARA LA COLOCACIÓN ALEATORIA DE LOS BARCOS EN LOS TABLEROS (JUGADORX Y MÁQUINA)
lista_esloras = [1,1,1,1,2,2,2,3,3,4]
barcos_colocados=0

def colocar_barcos(tablero,lista_esloras):
    tablero= np.full((10, 10)," ")
    lista_esloras = [1,1,1,1,2,2,2,3,3,4]
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
    tablero


#Tableros de la máquina
tablero_maquina = np.full((10, 10)," ")    #Tablero inicial
colocar_barcos(tablero_maquina , [1,1,1,1,2,2,2,3,3,4] )   #Colocación aleatoria

tablero_vista_de_jugadorx_maquina= np.full((10, 10)," ")   #Tablero de vista PARA JUGADORX. Salen disparos
    #En este solamente se verán X y -

#Tableros jugadorx
tablero_jugadorx = np.full((10, 10)," ")
colocar_barcos(tablero_jugadorx, [1,1,1,1,2,2,2,3,3,4] )   #Colocación aleatoria

tablero_vista_de_jugadorx_maquina=np.full((10, 10)," ")     #en este se ve el avance de jugadorx en el de maquina
    #En este solamente se verán X y - (NO LO VE JUGADORX

#DURANTE EL JUEGO
Jugadorx va modificando el tablero de la máquina y el de su vista
La máquina va modificando el tablero de jugadorx y el de su vista



#FUNCIONES PARA CADA TURNO:
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

#FIN DE LA PARTIDA   (se puede hacer todo con un bucle while)
    
def fin_partida(tablero_jugadorx, tablero_maquina):
    if "O" not in tablero_jugadorx :
        print("¡Perdiste!")
    elif "O" not in tablero_maquina:   #Jugadorx gana cuando todos los "O" se han convertido en "X" en el tablero de la maquina
    print("¡Ganaste, humanx!")
    continue


#BUCLE PRINCIPAL:

while "O" in tablero_jugadorx or "O" in tablero_maquina:  

    turno_jugadorx(tablero_maquina)

    if fin_partida(tablero_jugadorx, tablero_maquina):
        break
 
    turno_maquina(tablero_jugadorx)

    if verificar_ganador(tablero_jugadorx, tablero_maquina)
        break

"O" not in tablero_jugadorx:
    print("¡Perdiste!")

"O" not in tablero_maquina:   #Jugadorx gana cuando todos los "O" se han convertido en "X" en el tablero de la maquina
    print("¡Ganaste!")


#DISPAROS

#En cada disparo se modifica tanto el tablero del contrario como la vista que yo tengo

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


#HUNDIR UN BARCO
Ver cómo hacer para que de hundido.


#BUCLE DE DISPAROS
if tablero[coordenada1,coordenada2]= "X":
    disparo(coordenada1,coordenada2)




