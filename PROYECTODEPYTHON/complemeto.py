from tkinter import *
from tkinter import messagebox

# Variables
ingresos = 0
gastos = []

# Funciones
def agregar_ingreso():
    global ingresos
    try:
        monto = float(entrada_monto.get())
        ingresos += monto
        messagebox.showinfo("Éxito", "Ingreso registrado")
        entrada_monto.delete(0, END)
    except:
        messagebox.showerror("Error", "Ingresa un número válido")

def agregar_gasto():
    try:
        descripcion = entrada_descripcion.get()
        monto = float(entrada_monto.get())

        gastos.append((descripcion, monto))

        messagebox.showinfo("Éxito", "Gasto registrado")

        entrada_descripcion.delete(0, END)
        entrada_monto.delete(0, END)

    except:
        messagebox.showerror("Error", "Ingresa datos válidos")

def ver_balance():
    total_gastos = sum(gasto[1] for gasto in gastos)
    balance = ingresos - total_gastos

    texto = f"En Ingresos: ${ingresos:.3f}\n Pesos "
    texto += f"Gastados: ${total_gastos:.3f}\n Pesos "
    texto += f"En Balance: ${balance:.3f}\n Pesos "

    texto += "Lista de gastos:\n"

    for desc, monto in gastos:
        texto += f"- {desc}: ${monto:.3f}\n Pesos "

    resultado.config(text=texto)

# Ventana
ventana = Tk()
ventana.title("Control de Ahorros")
ventana.geometry("500x500")

# Título de la app
Label(
    ventana,
    text="CONTROL DE AHORROS",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Descripción
Label(ventana, text="Descripción del gasto").pack()

entrada_descripcion = Entry(ventana, width=30)
entrada_descripcion.pack(pady=5)

# Monto
Label(ventana, text="Monto").pack()

entrada_monto = Entry(ventana, width=30)
entrada_monto.pack(pady=5)

# Botones
Button(
    ventana,
    text="Agregar Ingreso",
    command=agregar_ingreso
).pack(pady=5)

Button(
    ventana,
    text="Agregar Gasto",
    command=agregar_gasto
).pack(pady=5)

Button(
    ventana,
    text="Ver Balance",
    command=ver_balance
).pack(pady=5)

# Resultado
resultado = Label(
    ventana,
    text="",
    justify=LEFT
)
resultado.pack(pady=20)

ventana.mainloop()