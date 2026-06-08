def main():
    ingresos = 0
    gastos = []

    while True:
        def mostrar_bienvenida():
            print("|================================|")
            print("|      🏦 ServiBanca JK 📋       |")       
            print("|================================|")
        mostrar_bienvenida()
        print("|1. Ingresar ingreso             |")
        print("|2. Registrar gasto              |")
        print("|3. Ver balance                  |")
        print("|4. Salir                        |")
        
        opcion = input("|Elige una opción (1-4):         |")

        if opcion == '1':
            monto = float(input("|Ingresa el monto del ingreso:   |"))
            ingresos += monto
            print("--- Ingreso registrado. ---")
        
        elif opcion == '2':
            descripcion = input("|Describe el gasto:          |")
            monto = float(input("|Ingresa el monto del gasto: |"))
            gastos.append((descripcion, monto))
            print("--- Gasto registrado. ---")
        
        elif opcion == '3':
            total_gastos = sum(m[1] for m in gastos)
            balance = ingresos - total_gastos
            print(f"\nBalance total: {balance:.3f} Pesos")
            print(f"Ingresos: {ingresos:.3f} Pesos")
            print("Gastos: ")
            for desc, monto in gastos:
                print(f"  - {desc}: {monto:.3f} Pesos")
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()