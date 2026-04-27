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
