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
  Dentro del turno de lx jugadorx, permite salir o imprimir el tablero para ver cómo va la partida.

Fundión de **disparar**:


Función de **fin de partida**:
  Acaba cuando todo sean barcos hundidos ("X") en uno de los tableros. Es decir, que no queden barcos ("O").
