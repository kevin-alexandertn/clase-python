#11. Cuenta regresiva
#Enunciado: Pide al usuario un número entero positivo. Usa un bucle while para mostrar una cuenta regresiva desde ese número hasta 0, y al final imprime "¡Despegue!".
#Conceptos: Bucle while, decremento de variables.

# Programa: Cuenta regresiva

#  Pedir un número entero positivo al usuario
numero = int(input("Escribe un número entero positivo: "))

# Usar un bucle while para la cuenta regresiva
while numero >= 0:
    print(numero)
    numero -= 1   # Decremento de la variable en cada iteración

# Mensaje final
print("¡Despegue!")


#12. Suma de los primeros N números
#Enunciado: Solicita un número N. Usa un bucle for para sumar todos los números desde el 1 hasta N y muestra el resultado final.
#Conceptos: Bucle for con range(), variable acumuladora.
# Programa: Suma de los primeros N números

#  Solicitar el número N
N = int(input("Ingrese un número entero positivo: "))

#  Inicializar variable acumuladora
suma = 0

#  Usar un bucle for con range para sumar desde 1 hasta N
for i in range(1, N + 1):
    suma += i   # Acumula la suma

#  Mostrar el resultado final
print("La suma de los primeros", N, "números es:", suma)


#13. La tabla de multiplicar
#Enunciado: Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 utilizando un bucle for.
#Conceptos: Bucle for, formato de cadenas (f-strings).

# Programa: La tabla de multiplicar

#  Solicitar un número al usuario
numero = int(input("Ingrese un número entero: "))

#  Usar un bucle for para generar la tabla del 1 al 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#14. Adivina el PIN
#Enunciado: Define una variable con un PIN secreto (ej. "1234"). Usa un bucle while para pedirle al usuario que ingrese el PIN. El programa no debe dejarlo avanzar hasta que ingrese el PIN correcto.
#Conceptos: Bucle while, comparación de cadenas.

# Programa: Adivina el PIN

#  Definir el PIN secreto
pin_secreto = "1234"

#  Pedir al usuario que ingrese el PIN
pin_ingresado = input("Ingrese el PIN: ")

#  Usar un bucle while para repetir hasta que sea correcto
while pin_ingresado != pin_secreto:
    print("PIN incorrecto. Intente nuevamente.")
    pin_ingresado = input("Ingrese el PIN: ")

#  Mensaje final cuando el PIN es correcto
print("¡Acceso concedido!")


#15. Contador de vocales
#Enunciado: Pide al usuario que ingrese una frase. Utiliza un bucle for para recorrer cada letra de la frase y cuenta cuántas vocales (a, e, i, o, u) tiene. Imprime el total.
#Conceptos: Bucle for sobre una cadena (string), condicionales dentro de un bucle, variable contador.

# Programa: Contador de vocales

#  Solicitar una frase al usuario
frase = input("Ingrese una frase: ")

#  Inicializar contador
contador = 0

#  Recorrer cada letra de la frase
for letra in frase:
    # Convertir a minúscula para evitar problemas con mayúsculas
    if letra.lower() in "aeiou":
        contador += 1   # Sumar 1 al contador si es vocal

# 4. Mostrar el resultado
print("La frase tiene", contador, "vocal(es).")
