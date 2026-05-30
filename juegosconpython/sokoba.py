import os

# =====================================================================
# R1 & R3 - BANCO COMPLETO DE 12 NIVELES (Dificultad Creciente)
# =====================================================================
NIVELES = [
    # Nivel 1: Mapa obligatorio del taller
    """#######
#     #
#  $  #
# .@  #
#     #
#######""",

    # Nivel 2: Pasillo básico y dos cajas
    """######
#@   #
# $$ #
# .. #
######""",

    # Nivel 3: El giro en L
    """#########
#@      #
# #.$$. #
# #     #
#########""",

    # Nivel 4: Columnas centrales
    """#######
#     #
# #$#.#
# .@$ #
#     #
#######""",

    # Nivel 5: Habitaciones conectadas
    """########
#  ..  #
#  $$  #
##@@####
#      #
########""",

    # Nivel 6: Gestión de espacio reducido
    """#######
# . . #
# $ $ #
#  @  #
#######""",

    # Nivel 7: El almacén dividido
    """#########
#@#     #
# # $.$ #
#   $.# #
#########""",

    # Nivel 8: El trébol (Cajas atrapadas en el centro)
    """#########
#  . .  #
#  $$$  #
#  .@.  #
#########""",

    # Nivel 9: El laberinto de zigzag
    """##########
#@ #     #
#  $ .#  #
#  # $ . #
##########""",

    # Nivel 10: Doble pasillo invertido
    """###########
# . .   $ #
# # #$# # #
#   @     #
###########""",

    # Nivel 11: Bloques en cruz
    """#########
#   .   #
#  $$$  #
# . @ . #
#########""",

    # Nivel 12: El gran desafío final
    """###########
# . . .   #
#  $ $ $  #
#   #@#   #
###########"""
]

# Variables globales para el control del juego
METAS = set()
nivel_actual = 0

def cargar_nivel(indice_nivel):
    """Convierte el string del nivel en una matriz de caracteres y registra las metas."""
    global METAS
    METAS.clear()  # Limpiar las metas del nivel anterior
    
    lineas = NIVELES[indice_nivel].split("\n")
    matriz = [list(linea) for linea in lineas]
    
    # Escanear la matriz para registrar las coordenadas de las metas (. o *)
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            if matriz[r][c] in [".", "*"]:
                METAS.add((r, c))
                
    return matriz

# =====================================================================
# 4. REQUERIMIENTOS NO FUNCIONALES: FUNCIONES OBLIGATORIAS
# =====================================================================

def dibujar_mapa(matriz):
    """R4 - Limpia la pantalla, dibuja el mapa actual y las instrucciones."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"=== SOKOBAN - NIVEL {nivel_actual + 1} de {len(NIVELES)} ===")
    print(f"Metas listas: {contar_cajas_en_meta(matriz)} de {len(METAS)}\n")
    
    # Imprimir el mapa fila por fila
    for fila in matriz:
        print("".join(fila))
    
    print("\n" + "="*35)
    print("="*35)
    print("  W : Arriba    |  S : Abajo")
    print("  A : Izquierda |  D : Derecha")
    print("  R : Reiniciar Nivel")
    print("  Q : Salir del juego")
    print("="*35)

def obtener_posicion_jugador(matriz):
    """Busca al jugador (@) en la matriz y retorna sus coordenadas (fila, columna)."""
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            if matriz[r][c] == "@":
                return r, c
    return None

def mover(direccion, matriz):
    """R3 - Lógica de movimiento, empuje de cajas y prevención de colisiones."""
    pos_actual = obtener_posicion_jugador(matriz)
    if not pos_actual:
        return
    r_act, c_act = pos_actual

    # Asignación de vectores de movimiento según la dirección dada
    dr, dc = 0, 0
    if direccion == "W": dr = -1
    elif direccion == "S": dr = 1
    elif direccion == "A": dc = -1
    elif direccion == "D": dc = 1
    else: return

    # Posiciones proyectadas (S1 = Destino jugador, S2 = Destino de caja)
    r_s1, c_s1 = r_act + dr, c_act + dc
    r_s2, c_s2 = r_s1 + dr, c_s1 + dc

    # Validación anti-IndexError: Asegurar que S1 esté dentro de la matriz
    if not (0 <= r_s1 < len(matriz) and 0 <= c_s1 < len(matriz[0])):
        return

    objeto_s1 = matriz[r_s1][c_s1]

    # CASO A: Caminar hacia un espacio vacío o meta desocupada
    if objeto_s1 in [" ", "."]:
        # Si el jugador estaba parado en una meta, al irse devuelve el "." de lo contrario deja espacio vacío
        matriz[r_act][c_act] = "." if (r_act, c_act) in METAS else " "
        matriz[r_s1][c_s1] = "@"

    # CASO B: Caminar hacia una caja ($ o *)
    elif objeto_s1 in ["$", "*"]:
        # Validación anti-IndexError: Asegurar que S2 esté dentro de la matriz antes de empujar
        if 0 <= r_s2 < len(matriz) and 0 <= c_s2 < len(matriz[0]):
            objeto_s2 = matriz[r_s2][c_s2]
            
            # La caja solo se puede empujar si detrás hay suelo limpio o una meta vacía
            if objeto_s2 in [" ", "."]:
                matriz[r_s2][c_s2] = "*" if (r_s2, c_s2) in METAS else "$"
                matriz[r_s1][c_s1] = "@"
                matriz[r_act][c_act] = "." if (r_act, c_act) in METAS else " "

# =====================================================================
# AUXILIARES Y BUCLE PRINCIPAL
# =====================================================================

def contar_cajas_en_meta(matriz):
    """Cuenta cuántas cajas (*) están posicionadas sobre metas en este turno."""
    return sum(1 for r, c in METAS if matriz[r][c] == "*")

def verificar_victoria(matriz):
    """Retorna True si todas las metas del mapa contienen una caja (*)."""
    if not METAS: 
        return False
    for r, c in METAS:
        if matriz[r][c] != "*":
            return False
    return True

def main():
    global nivel_actual
    
    # Cargar la matriz del primer nivel
    matriz_juego = cargar_nivel(nivel_actual)
    
    while True:
        dibujar_mapa(matriz_juego)
        
        # Evaluar si el usuario resolvió el mapa actual (todas las metas con '*')
        if verificar_victoria(matriz_juego):
            print("\n¡Nivel completado con éxito! 🎉")
            input("Presiona ENTER para pasar al siguiente nivel...")
            
            nivel_actual += 1
            # Si pasamos el límite de niveles del arreglo, termina el juego completo
            if nivel_actual >= len(NIVELES):
                print("\n¡Felicidades! Has completado los 12 niveles de Sokoban. ¡Eres un maestro! 🏆")
                break
            else:
                matriz_juego = cargar_nivel(nivel_actual)
                continue
                
        # Captura y formateo de entrada por teclado (R2)
        entrada = input("\nIntroduce tu movimiento: ").strip().upper()
        
        if entrada == "Q":
            print("\nJuego terminado de forma manual. ¡Hasta pronto!")
            break
            
        if entrada == "R":
            # Botón de emergencia si trabas una caja contra una esquina
            matriz_juego = cargar_nivel(nivel_actual)
            continue
            
        if entrada in ["W", "A", "S", "D"]:
            mover(entrada, matriz_juego)

if __name__ == "__main__":
    main()