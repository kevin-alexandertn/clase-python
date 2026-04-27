#1. El saludo personalizado
#Enunciado: Pide al usuario su nombre y su edad. Muestra un mensaje de bienvenida y calcula en qué año nació aproximadamente (restando la edad al año actual)
#Conceptos: Variables, entrada/salida de datos, operaciones matemáticas básicas.

# El saludo personalizado

#  Pedir datos al usuario
nombre = input("Por favor, escribe tu nombre: ")
edad = int(input("¿Cuántos años tienes? "))

#  Calcular el año de nacimiento aproximado
año_actual = 2026   # Variable fija con el año actual
año_nacimiento = año_actual - edad   # Operación matemática básica

#  Mostrar mensaje de bienvenida
print("¡Bienvenido/a,", nombre + "!")
print("Tienes", edad, "años, así que naciste aproximadamente en el año", año_nacimiento)



#2. Par o Impar
#Enunciado: Escribe un programa que pida al usuario un número entero y le diga si es par o impar.
#Conceptos: Operador módulo (%), condicional if-else.

# Programa: Par o Impar

# Pedir un número entero al usuario
numero = int(input("Escribe un número entero: "))

#  Usar el operador módulo (%) para verificar si es par o impar
if numero % 2 == 0:
    print("El número", numero, "es PAR.")
else:
    print("El número", numero, "es IMPAR.")


 #3. El peaje
#Enunciado: Pregunta al usuario la edad. Si es mayor o igual a 18 años, muestra el mensaje "Puedes conducir", de lo contrario, muestra "Aún no tienes edad para conducir".
#Conceptos: Condicional if-else, operadores relacionales (>=).   

edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("puedes conducir")
else:
    print("no puedes conducir")

#4. El mayor de dos
#Enunciado: Pide al usuario dos números diferentes y muestra por pantalla cuál de los dos es el mayor.
#Conceptos: Variables, condicional if-else, comparación (>).

# Programa: El mayor de dos

#  Pedir dos números al usuario
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

#  Comparar los dos números usando condicional if-else
if num1 > num2:
    print("El mayor es:", num1)
else:
    print("El mayor es:", num2)


#5. Positivo, negativo o cero
#Enunciado: Solicita un número al usuario. El programa debe imprimir si el número es positivo, negativo o si es exactamente cero.
#Conceptos: Condicionales múltiples (if, elif, else).

# Programa: Positivo, negativo o cero

# Solicitar un número al usuario

numero = float(input("Escribe un número: "))

# Condicionales múltiples para evaluar el número
if numero > 0:
    print("El número es POSITIVO.")
elif numero < 0:
    print("El número es NEGATIVO.")
else:
    print("El número es CERO.")
