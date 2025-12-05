"""
Juego del 3 en Raya
IES Zaidín-Vergeles
Autor: Hector Tudela Morales
"""

# Constantes para representar las fichas
CASILLA_VACIA = 0
FICHA_JUGADOR1 = 1  # Representará 'O'
FICHA_JUGADOR2 = 2  # Representará 'X'

def crear_tablero():
    """
    Crea y devuelve un tablero vacío de 3x3.
    
    Returns:
        list: Matriz 3x3 inicializada con casillas vacías
    """
    return [[CASILLA_VACIA for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    """
    Visualiza el tablero en pantalla de forma clara y comprensible.
    
    Args:
        tablero (list): Matriz 3x3 que representa el tablero
    """
    if not validar_tablero(tablero):
        print("Error: Tablero inválido")
        return
    
    print("\n" + "="*25)
    print("   TABLERO DEL 3 EN RAYA")
    print("="*25)
    print("     0   1   2")
    print("   " + "─"*13)
    
    for i in range(3):
        fila = f" {i} │"
        for j in range(3):
            if tablero[i][j] == CASILLA_VACIA:
                fila += "   │"
            elif tablero[i][j] == FICHA_JUGADOR1:
                fila += " O │"
            elif tablero[i][j] == FICHA_JUGADOR2:
                fila += " X │"
        print(fila)
        if i < 2:
            print("   " + "─"*13)
    print("   " + "─"*13)
    print()

def validar_tablero(tablero):
    """
    Valida que el tablero tenga el formato correcto.
    
    Args:
        tablero (list): Matriz a validar
        
    Returns:
        bool: True si el tablero es válido, False en caso contrario
    """
    if not isinstance(tablero, list) or len(tablero) != 3:
        return False
    
    for fila in tablero:
        if not isinstance(fila, list) or len(fila) != 3:
            return False
        for casilla in fila:
            if casilla not in [CASILLA_VACIA, FICHA_JUGADOR1, FICHA_JUGADOR2]:
                return False
    
    return True

def colocar_ficha(tablero, ficha, x, y):
    """
    Coloca una ficha en el tablero en la posición indicada.
    
    Args:
        tablero (list): Matriz 3x3 que representa el tablero
        ficha (int): Tipo de ficha a colocar (FICHA_JUGADOR1 o FICHA_JUGADOR2)
        x (int): Coordenada fila (0-2)
        y (int): Coordenada columna (0-2)
        
    Returns:
        bool: True si se colocó la ficha con éxito, False en caso contrario
    """
    # Validar tablero
    if not validar_tablero(tablero):
        return False
    
    # Validar ficha
    if ficha not in [FICHA_JUGADOR1, FICHA_JUGADOR2]:
        return False
    
    # Validar coordenadas
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False
    
    # Verificar si la casilla está vacía
    if tablero[x][y] != CASILLA_VACIA:
        return False
    
    # Colocar la ficha
    tablero[x][y] = ficha
    return True

def hay_ganador(tablero):
    """
    Verifica si hay un ganador en el tablero (tres fichas en línea).
    
    Args:
        tablero (list): Matriz 3x3 que representa el tablero
        
    Returns:
        bool: True si hay tres fichas en línea, False en caso contrario
    """
    if not validar_tablero(tablero):
        return False
    
    # Verificar filas
    for i in range(3):
        if (tablero[i][0] == tablero[i][1] == tablero[i][2] and 
            tablero[i][0] != CASILLA_VACIA):
            return True
    
    # Verificar columnas
    for j in range(3):
        if (tablero[0][j] == tablero[1][j] == tablero[2][j] and 
            tablero[0][j] != CASILLA_VACIA):
            return True
    
    # Verificar diagonal principal
    if (tablero[0][0] == tablero[1][1] == tablero[2][2] and 
        tablero[0][0] != CASILLA_VACIA):
        return True
    
    # Verificar diagonal secundaria
    if (tablero[0][2] == tablero[1][1] == tablero[2][0] and 
        tablero[0][2] != CASILLA_VACIA):
        return True
    
    return False

def juego_terminado(tablero):
    """
    Verifica si el juego ha terminado (tablero completo).
    
    Args:
        tablero (list): Matriz 3x3 que representa el tablero
        
    Returns:
        bool: True si el tablero está completo, False si quedan casillas vacías
    """
    if not validar_tablero(tablero):
        return True
    
    for fila in tablero:
        for casilla in fila:
            if casilla == CASILLA_VACIA:
                return False
    
    return True

def solicitar_coordenadas(nombre_jugador):
    """
    Solicita las coordenadas al jugador y las valida.
    
    Args:
        nombre_jugador (str): Nombre del jugador
        
    Returns:
        tuple: Tupla (x, y) con las coordenadas válidas
    """
    while True:
        try:
            print(f"\nTurno de {nombre_jugador}")
            x = int(input("Introduce la fila (0-2): "))
            y = int(input("Introduce la columna (0-2): "))
            
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("❌ Error: Las coordenadas deben estar entre 0 y 2")
                continue
            
            return (x, y)
        
        except ValueError:
            print("❌ Error: Debes introducir números enteros")

def mostrar_resultado(tablero, nombre_jugador1, nombre_jugador2, turno):
    """
    Muestra el resultado final de la partida.
    
    Args:
        tablero (list): Matriz 3x3 que representa el tablero
        nombre_jugador1 (str): Nombre del jugador 1
        nombre_jugador2 (str): Nombre del jugador 2
        turno (int): Turno actual (1 o 2)
    """
    mostrar_tablero(tablero)
    
    if hay_ganador(tablero):
        ganador = nombre_jugador1 if turno == 1 else nombre_jugador2
        print("="*25)
        print(f"🎉 ¡{ganador} HA GANADO! 🎉")
        print("="*25)
    else:
        print("="*25)
        print("🤝 ¡EMPATE! 🤝")
        print("="*25)

def jugar_partida():
    """
    Ejecuta una partida completa del juego.
    """
    # Solicitar nombres de los jugadores
    print("\n" + "="*40)
    print("   BIENVENIDO AL JUEGO DEL 3 EN RAYA")
    print("   REGLAS: DOS JUGADORES, UNO CON 'O' Y OTRO CON 'X'")
    print("   REALIZADO POR HECTOR TUDELA MORALES - IES ZAIDÍN-VERGELES")
    print("="*40)
    
    nombre_jugador1 = input("\nNombre del Jugador 1 (O): ").strip()
    while not nombre_jugador1:
        print("❌ El nombre no puede estar vacío")
        nombre_jugador1 = input("Nombre del Jugador 1 (O): ").strip()
    
    nombre_jugador2 = input("Nombre del Jugador 2 (X): ").strip()
    while not nombre_jugador2:
        print("❌ El nombre no puede estar vacío")
        nombre_jugador2 = input("Nombre del Jugador 2 (X): ").strip()
    
    # Crear e inicializar el tablero
    tablero = crear_tablero()
    turno = 1  # El jugador 1 empieza
    
    # Bucle principal del juego
    while True:
        # Mostrar el tablero
        mostrar_tablero(tablero)
        
        # Determinar jugador actual
        if turno == 1:
            nombre_actual = nombre_jugador1
            ficha_actual = FICHA_JUGADOR1
            simbolo = "O"
        else:
            nombre_actual = nombre_jugador2
            ficha_actual = FICHA_JUGADOR2
            simbolo = "X"
        
        # Solicitar coordenadas
        x, y = solicitar_coordenadas(f"{nombre_actual} ({simbolo})")
        
        # Intentar colocar la ficha
        if colocar_ficha(tablero, ficha_actual, x, y):
            # Verificar si hay ganador
            if hay_ganador(tablero):
                mostrar_resultado(tablero, nombre_jugador1, nombre_jugador2, turno)
                break
            
            # Verificar si el juego ha terminado (empate)
            if juego_terminado(tablero):
                mostrar_resultado(tablero, nombre_jugador1, nombre_jugador2, turno)
                break
            
            # Cambiar de turno
            turno = 2 if turno == 1 else 1
        else:
            print("❌ La casilla está ocupada. Intenta con otra posición.")

def main():
    """
    Función principal del programa.
    """
    while True:
        # Jugar una partida
        jugar_partida()
        
        # Preguntar si quiere jugar otra partida
        print("\n" + "="*40)
        respuesta = input("¿Deseas jugar otra partida? (s/n): ").strip().lower()
        
        while respuesta not in ['s', 'n', 'si', 'no']:
            print("❌ Respuesta no válida. Introduce 's' o 'n'")
            respuesta = input("¿Deseas jugar otra partida? (s/n): ").strip().lower()
        
        if respuesta in ['n', 'no']:
            print("\n" + "="*40)
            print("   ¡Gracias por jugar! ¡Hasta pronto!")
            print("="*40 + "\n")
            break

main()