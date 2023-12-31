import numpy as np
import random 

#TABLEROS: 4 tableros: 2 de máquina y 2 de jugadorx

#FUNCIÓN PARA LA COLOCACIÓN ALEATORIA DE LOS BARCOS EN LOS TABLEROS (JUGADORX Y MÁQUINA)
lista_esloras = [1,1,1,1,2,2,2,3,3,4]
def colocar_barcos(tablero,lista_esloras):
    tablero= np.full((10, 10)," ")
    for eslora in lista_esloras:
        barcos_colocados = 0
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
    return tablero

#Tableros en que se ven barcos de jugadorx
tablero_jugadorx = np.full((10, 10)," ")
colocar_barcos(tablero_jugadorx, [1,1,1,1,2,2,2,3,3,4])   #Colocación aleatoria

tablero_vista_para_maquina_de_jugadorx=np.full((10, 10)," ")     #en este se ve el avance de jugadorx en el de maquina
    #En este solamente se verán X y - (NO LO VE JUGADORX)

#Tableros en que se ven barcos de máquina
tablero_maquina = np.full((10, 10)," ")    #Tablero inicial
colocar_barcos(tablero_maquina , [1,1,1,1,2,2,2,3,3,4] )   #Colocación aleatoria

tablero_vista_para_jugadorx_de_maquina= np.full((10, 10)," ")   #Tablero de vista PARA JUGADORX. Salen disparos
    #En este solamente se verán "X" y "-""


#DURANTE EL JUEGO
'''Jugadorx va modificando el tablero de la máquina y el de su vista
La máquina va modificando el tablero de jugadorx y el de su vista
'''

#ÍNDICE

def seguir_jugando():
    opcion = 0
    while opcion != 1:
        mensaje = """
            Recuerda que puedes:
            Insertar 1 para salir del juego
            Insertar 2 para ver tu tablero
            Insertar 3 para ver tu vista del tablero de la máquina (comprobar impactos)
            """
        print(mensaje)
        opcion=int(input("Inserta opción: "))
        if opcion ==2:
            print(tablero_jugadorx)
        if opcion ==3:
            print(tablero_vista_para_jugadorx_de_maquina)
    print("¡Hasta luego!")   #Salir

#FUNCIONES PARA CADA TURNO:
def turno_jugadorx(tablero_maquina):
    seguir_jugando()
    coordenada1= input("Introduce un numero de fila para tu coordenada",)
    coordenada2= input("Introduce un numero de columna para tu coordenada",)
    disparo_jugadorx (coordenada1,coordenada2,tablero_maquina)

def turno_maquina(tablero_jugadorx):
    coordenada1 = np.random.randint(0, 10)
    coordenada2 = np.random.randint(0, 10)
    disparo_maquina (coordenada1,coordenada2,tablero_jugadorx)

#FIN DE LA PARTIDA   (se puede hacer todo con un bucle while)
    
def fin_partida(tablero_jugadorx, tablero_maquina):
    if "O" not in tablero_jugadorx :
        print("¡Perdiste!")
        return True
    elif "O" not in tablero_maquina:   #Jugadorx gana cuando todos los "O" se han convertido en "X" en el tablero de la maquina
        print("¡Ganaste, humanx!")
        return True
    return False
 

#DISPAROS

'''En cada disparo se modifica tanto el tablero del contrario como la vista que yo tengo
Como jugadorx solamente veo mi tablero y la vista del tablero de la máquina con X y -
'''

#Disparo de persona
def disparo_jugadorx (coordenada1, coordenada2, tablero_maquina, tablero_vista_para_jugadorx_de_maquina):
    if tablero_maquina[coordenada1,coordenada2]== " ":
        tablero_maquina[coordenada1,coordenada2]= "_"
        tablero_vista_para_jugadorx_de_maquina=[coordenada1,coordenada2]= "_"
        print("¡Agua!")
        print(tablero_vista_para_jugadorx_de_maquina)
    elif tablero_maquina[coordenada1,coordenada2]== "O":
        tablero_maquina[coordenada1,coordenada2]= "X"
        tablero_vista_para_jugadorx_de_maquina[coordenada1,coordenada2]= "X"
        print("¡Tocado!")
        print(tablero_vista_para_jugadorx_de_maquina)
        if barco_hundido(coordenada1, coordenada2, tablero_maquina):
            print("...y hundido!")

#Disparo de la máquina
def disparo_maquina (coordenada1,coordenada2, tablero_jugadorx, tablero_vista_para_maquina_de_jugadorx):
    if tablero_jugadorx[coordenada1,coordenada2]== " ":
        tablero_jugadorx[coordenada1,coordenada2]= "_"
        tablero_vista_para_maquina_de_jugadorx[coordenada1,coordenada2]= "_"
        print("¡Agua!")
    elif tablero_jugadorx[coordenada1,coordenada2]== "O":
        tablero_jugadorx[coordenada1,coordenada2]= "X"
        tablero_vista_para_maquina_de_jugadorx[coordenada1,coordenada2]= "X"
        print("¡La máquina te ha tocado un barco!")
        if barco_hundido(coordenada1, coordenada2, tablero_jugadorx):
            print("...y te lo ha hundido!")

#HUNDIR UN BARCO   (Esto lo hemos copiado porque no había manera..)
def barco_hundido(coordenada1, coordenada2, tablero):
    dicc_esloras = {4: 1, 3: 2, 2: 3, 1: 4}  
    for cantidad, esloras in dicc_esloras.items():
        for _ in range(esloras):   
            for _ in range(cantidad):
                if all(tablero[coordenada1, coordenada2 + _] == "X"):   
                    return True 
    return False 



#ÍNDICE PRINCIPAL

def iniciar_juego():
    mensaje = """
    ¡Bienvenidx a Hundir la flota!
        Inserta 0 para INICIAR el juego.
        Durante el juego, podrás:
            Insertar 1 para salir del juego.
            Insertar 2 para ver tu tablero.
            Insertar 3 para ver tu vista del tablero de la máquina (comprobar impactos).
    """
    print(mensaje)
    opcion=int(input("Inserta opción: "))
    while opcion != 1:
        if opcion == 0:                                         #ESTE ES EL BUCLE PRINCIPAL
            tablero_maquina = np.full((10, 10), " ")                    #Aquí colocamos barcos
            colocar_barcos(tablero_maquina, [1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

            tablero_jugadorx = np.full((10, 10), " ")
            colocar_barcos(tablero_jugadorx, [1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

            while "O" in tablero_jugadorx or "O" in tablero_maquina:    #Aquí empieza el juego
                turno_jugadorx(tablero_maquina)
                if fin_partida(tablero_jugadorx, tablero_maquina):
                    break
                turno_maquina(tablero_jugadorx)
                if fin_partida(tablero_jugadorx, tablero_maquina):
                    break
        if opcion ==2:
            print(tablero_jugadorx)
        if opcion ==3:
            print(tablero_vista_para_jugadorx_de_maquina)
    print("¡Hasta luego!")


#########AQUÍ INICIAMOS EL JUEGO ###################

iniciar_juego()



