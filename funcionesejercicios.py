
'''
EJERCICIO DE PROGRAMACIÓN INTERMEDIA - FUNCIONES

El ejercicio consite en la implementación de una calculadora que permita realizar las siguientes 
operaciones: 

1. Sumar Dos Números
2. Restar Dos Números
3. Multiplicar Dos Números
4. Dividir Dos Números
5. Calcular el factorial de un número
6. Calcular la potencia de un número elevado a otro

Para la implementación del ejercicio vamos a utilizar las siguientes funciones:

Función Sumar: se encargará de realizar todo el proceso de suma, incluyendo la solicitud de los 
dos números al usuario que se van a sumar.

Función Restar: se encargará de realizar todo el proceso de resta, incluyendo la solicitud del minuendo
y el sustraendo al usuario.

Función Multiplicar: se encargará de realizar todo el proceso de multiplicación, incluyendo la solicitud
de los factores al usuario.

Función Dividir: se encargará de realizar todo el proceso de división, incluyendo la solicitud del dividendo
y el divisor al usuario. Validar que no se realice una división por cero.

Función Factorial: Se encargará de solicitar el número del que se quiere calcular el factorial.
Una Vez tenga el numero invocará a la función de calcular factorial, validar que el número sea positivo 
y entero.

Función FactorialCalculo: función recursiva que se realiza en el cálculo del factorial del número que 
recibe por parámetro.

Función Potencia: se encargará de solicitar la base y el exponente al usuario e invocará a la 
función de calcular potencia,validar que el exponente sea un número entero.

Función PotenciaCalculo: función recursiva que se realiza en el cálculo de la potencia de los números
pasados como parámetros.

Función Calculadora: función principal que se encargará de mostrar el menú de opciones al usuario, 
solicitar la opción deseada y llamar a la función correspondiente según la opción seleccionada. 
La función debe continuar mostrando el menú hasta que el usuario decida salir.

Importante: tanto el menú como los mensajes de solicitud de datos y resultados deben ser claros 
y amigables para el usuario, y se deben manejar adecuadamente los casos de error, como la división 
por cero o la entrada de datos no válidos.

Utilizar diseño de Interfaz de Usuario mediante la consola utilizando ASCII Art para hacer el menú 
más atractivo visualmente.
'''
def sumar():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print(f"Resultado: {a + b}")

def restar():
    c = int(input("Ingrese el minuendo: "))
    d = int(input("Ingrese el sustraendo: "))
    print(f"Resultado: {c - d}")

def multiplicar():
    a = int(input("Ingrese el primer factor: "))
    b = int(input("Ingrese el segundo factor: "))
    print(f"Resultado: {a * b}")

def dividir():
    a = float(input("Ingrese el dividendo: "))
    b = float(input("Ingrese el divisor: "))
    if b == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {a / b}")

def potencia():
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    print(f"Resultado: {base ** exponente}")

# --- Funciones para el Factorial ---

def factorial_calculo(n):
    # Función recursiva
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calculo(n - 1)

def factorial():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num < 0:
            print("Error: El número debe ser positivo.")
        else:
            resultado = factorial_calculo(num)
            print(f"El factorial de {num} es: {resultado}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# --- Menú Principal ---

def menu():
    while True:
        print("\n--- CALCULADORA ---")
        print("="*50)
        print("1. Sumar") 
        print("2. Restar")  
        print("3. Multiplicar")
        print("4. Dividir")    
        print("5. Factorial")
        print("6. Potencia")  
        print("7. Salir")   
        print("="*50)
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1': sumar()
        elif opcion == '2': restar()
        elif opcion == '3': multiplicar()
        elif opcion == '4': dividir()
        elif opcion == '5': factorial()
        elif opcion == '6': potencia()
        elif opcion == '7': 
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
    