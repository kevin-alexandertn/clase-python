#16. Adivina el número (con intentos)
#Enunciado: El programa define un número secreto entre 1 y 20. El usuario tiene 5 intentos para adivinarlo (usando un bucle while o for). En cada intento, el programa debe decirle si el número ingresado es mayor o menor al número secreto. Si acierta, el bucle se detiene.
#Conceptos: Bucle con límite, if-elif-else, interrupción de bucles (break).

# Programa: Adivina el número (con intentos)

# Definir el número secreto
numero_secreto = 13   #def

#  intentospermitidos
intentos = 5

# Bucle para pedir intentos al usuario
for i in range(intentos):
    numero = int(input("Adivina el número (entre 1 y 20): "))

    if numero == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break   # Sale del bucle si acierta
    elif numero < numero_secreto:
        print("El número secreto es MAYOR.")
    else:
        print("El número secreto es MENOR.")

# Mensaje final si no lo adivinó
else:
    print("Se acabaron los intentos. El número secreto era:", numero_secreto)


#17. Validador de números primos
#Enunciado: Pide un número al usuario y determina si es primo (solo divisible por 1 y por sí mismo). Usa un bucle para intentar dividir el número por todos los números anteriores a él y un condicional para verificar el residuo.
#Conceptos: Bucle for, operador módulo (%), uso de variables booleanas (banderas/flags).

# Programa: Validador de números primos

# Solicitar un número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Inicializar una bandera (variable booleana)
es_primo = True


if numero <= 1:
    es_primo = False
else:
    #  Probar divisiones desde 2 hasta numero-1
    for i in range(2, numero):
        if numero % i == 0:   # Si el residuo es 0, no es primo
            es_primo = False
            break   # Se interrumpe el bucle porque ya se encontró un divisor

# 5. Mostrar resultado
if es_primo:
    print("El número", numero, "es PRIMO.")
else:
    print("El número", numero, "NO es primo.")



"""18. Cajero Automático Básico
Enunciado: Simula un cajero. El saldo inicial es $1000. Usa un bucle while para mostrar un menú con tres opciones: 
1. Consultar saldo
2. Retirar dinero
3. Ingresar dinero
4. Salir. 
Si el usuario elige retirar, verifica que la cantidad sea menor o igual al saldo disponible antes de restar. El bucle termina solo cuando elige "Salir".
Conceptos: Menús interactivos con while, condicionales anidados, actualización de variables.
"""
print("\nEjercicio 18: Cajero Automático Básico")
saldo = 1000
while True:
    print("================================")
    print("   MENÚ DEL CAJERO AUTOMÁTICO")
    print("================================")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    print("--------------------------------")
    opcion = input("Elige una opción (1, 2, 3 o 4): ")
    
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")
    elif opcion == "2":
        cantidad = float(input("¿Cuánto dinero deseas retirar? $"))
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == "3":
        cantidad = float(input("¿Cuánto dinero deseas ingresar? $"))
        saldo += cantidad
        print(f"Has ingresado ${cantidad:.2f}. Tu nuevo saldo es: ${saldo:.2f}")
    elif opcion == "4":     
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")




"""19. La caja registradora
Enunciado: Crea un programa que permita al usuario ingresar los precios de varios productos uno por uno. El programa debe seguir pidiendo precios 
usando un while hasta que el usuario ingrese un "0" para indicar que terminó. 
Al finalizar, si el total de la compra supera los $100, aplica un 10% de descuento. Muestra el total a pagar.
Conceptos: Bucle while con condición de salida, acumuladores, condicional al final.
"""
print("\nEjercicio 19: La caja registradora")
# Inicializamos el acumulador del total
total = 0
print("--- Caja Registradora ---")
print("Introduce los precios de los productos (Escribe 0 para terminar):")
# Bucle while con condición de salida
while True:
    precio = float(input("Precio del producto: $"))
    # Condición para romper el bucle
    if precio == 0:
        break
    # Acumulamos el valor
    total += precio
# Aplicamos el descuento si el total supera los $100
if total > 100:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Descuento aplicado (10%): -${descuento:.2f}")
else:
    total_final = total
    print(f"\nSubtotal: ${total:.2f}")
    print("No se aplicó descuento (compra menor o igual a $100).")
# Resultado final
print(f"Total a pagar: ${total_final:.2f}")


"""
20. Sucesión de Fibonacci
Enunciado: Pide al usuario cuántos términos de la sucesión de Fibonacci quiere generar. La sucesión comienza con 0 y 1, y 
cada número siguiente es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8...). Usa un bucle for para calcular y mostrar la serie.
Conceptos: Intercambio de variables temporales, lógica algorítmica, bucle for.
"""
print ("\nEjercicio 20: Sucesión de Fibonacci")
# Pedimos al usuario la cantidad de términos
n = int(input("¿Cuántos términos de la sucesión de Fibonacci quieres ver? "))
# Inicializamos los dos primeros términos
a = 0
b = 1
print("Sucesión de Fibonacci:")
for i in range(n):
    print(a, end=" ")
    
    # Lógica de intercambio:
    # Calculamos el siguiente sumando los dos actuales
    # y actualizamos los valores para la próxima vuelta.
    suma = a + b
    a = b
    b = sum