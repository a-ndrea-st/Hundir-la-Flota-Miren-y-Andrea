# Juego Hundir la Flota, de Miren y Andrea.

Este es el juego **Hundir la Flota** que hemos programado con Python, como ejercicio de clase del bootcamp de Data Analysis en The Bridge. \
Las autoras somos Miren García y Andrea Sancho.


## ¿Cómo funciona (por dentro) el juego?
Este es un juego en que unx jugadorx se enfrenta a una máquina, con el fin de descubrir las posiciones de los respectivos barcos.
Por turnos, jugadorx y máquina van disparando para intentar adivinar las posiciones de la flota de la oponente y hundirla mediante disparos.
Quien antes adivine las posiciones de todos los barcos de la oponente (es decir,los hunda), gana.

Para el desarrollo de la partida, necesitamos **4 tableros**:
  * Dos tableros que verá lx jugadorx:
    + Uno en que ve la posición de sus barcos (*tablero_jugadorx*)
    + Uno en que ve los disparos que va haciendo al tablero de la máquina (*tablero_vista_para_jugadorx_de_maquina*) 
  * Dos tableros para la máquina:
    + Uno con la posición de sus barcos, que no ve lx jugadorx. (*tablero_maquina*)
    + Uno en que se recogen los disparos de la máquina al tablero de lx jugadorx (*tablero_vista_para_maquina_de_jugadorx*) 

Hemos definido una función inicial para **distribuir aleatoriamente** los barcos tanto de la máquina como de lx jugadorx.

Funciones para cada **turno**:
En el turno de lx jugadorx, dispara al tablero de la máquina. Puede fallar y disparar al agua o tocar el barco. 

Función de **índice**
Dentro del turno de lx jugadorx, permite salir o imprimir el tablero para ver cómo va la partida. Esta opción solamente la tiene lx jugadorx.

Función de **disparar**:
Hemos definido dos funciones de disparar, una de lx jugadorx y otra de la máquina. Ambas tienen tres posibilidades: agua, tocar el barco y hundir un barco.

Función de **fin de partida**:
El juego acaba cuando todo sean barcos hundidos ("X") en uno de los tableros (jugadorx o máquina). Es decir, que no queden barcos ("O").

Para englobarlo todo, hemos definido una **función de iniciar juego** que recoge la distintas opciones que tiene lx jugadorx para iniciar/salir/ver tableros del juego. Dentro de esta función, se encuentra la colocación de los barcos y el juego por turnos, hasta el fin de la partida.
