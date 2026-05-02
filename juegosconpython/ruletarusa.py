
"""
hasd
reto de programacion simulador de probabilidad: ruleta rusa
1. descripcion del problema
se requiere desarrollar un programa que simule el sistema de azar
basado en un revolver de 6 recamaras.el programa debe gestionar eventos
aleatorios,pausas de ejecucion para mejorar la experiencia de usuario
y control del flujo basado en condiciones de victoria o derrota


2. requerimientos tecnicos:
el algoritmo debe cumplir con los siguientes requisitos:

*imicializacion: definir una recamara ganadora (bala) de forma aleatoria de 1 a 6 (random)

*bucle de juego: el usuario debe actuar manualmente para girar el tambor manualmente (while) (time)

*mecanica de azar: en cada turno la pocicion de la recamara que queda al frente
al percutor debe ser aleatoria, simulando el giro del tambor

*condicion de derrrota: si la recamara seleccionada coincide con la de la bala, el programa (if)
termina inmediatamente

*condicion de victoria: el jugador gana si logra sobrevivir a 5 intentos    (else)
(ya que el sexto intento sera fatal)
"""
import random, time
print("="*50)
print ("bienvenido al simulador de la ruleta rusa")
print("="*50)

input("poner bala en el tambor(presione enter)")

bala= random.randint(1,6)
print("gira el tambor...")
time.sleep (0.5)

disparos= 0 #variable para contar los disparos realizados
while True:
    input("girar el tambor(precionar enter)")
    recamara= random.randint(1,6)
    input("apuntar y disparar(precione enter)")
    time.sleep(1)

    if recamara== bala:
        print("bang has perdido la bala estaba en la recamara"/
        "numero", bala)
        break
    else:
        disparos+= 1
        print("has sobrevivido a este intento.")
        print("intento de disparo", disparos)
        break
    if disparos== 5:
        print("!felicidades! has ganado al sobrevivir a 5 intentos.")
        break

print("="*50)
print("fin del juago-gracias por jugar")
print("="*50)

