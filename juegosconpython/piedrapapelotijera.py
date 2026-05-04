"""""
tarea pa casa aparte debe programar y subir al git hub
debe programaruna barra  de carga que se ejecute durante 3 segundos

por medio de bucles inprime en la terminar las siguientes figuras geometricas
triangulo 
cuadrado 
rectangulo
circulo
pentagono

con caracteres ascci 
"""""

import random

# Encabezado decorativo
print("="*40)
print(" JUEGO: PIEDRA, PAPEL O TIJERA ".center(40, "="))
print("="*40)

# Opciones posibles
opciones = ["piedra", "papel", "tijera"]

while True:
    # Entrada del usuario
    jugador = input("\nElige Piedra, Papel o Tijera (o escribe 'Salir' para terminar): ").lower()
    
    if jugador == "salir":
        print("\nGracias por jugar. ¡Hasta pronto!")
        break
    
    if jugador not in opciones:
        print("Entrada inválida. Intenta de nuevo.")
        continue
    
    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora.capitalize()}")
    
    # Lógica de comparación
    if jugador == computadora:
        print("Resultado: ¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print("Resultado: ¡Ganaste!")
    else:
        print("Resultado: Perdiste :(")
