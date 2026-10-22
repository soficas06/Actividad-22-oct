
import tkinter as tk
import ast
import operator

# COLORES
FONDO = "#FFF0F5"
ROSA = "#F7B6D2"
ROSA_OSCURO = "#E78FB3"
BLANCO = "#FFFFFF"
TEXTO = "#75445B"
LILA = "#E8DDF8"

ventana = tk.Tk()
ventana.title("♡ Mi calculadora ♡")
ventana.geometry("350x510")
ventana.resizable(False, False)
ventana.configure(bg=FONDO)

expresion = tk.StringVar(value="")

# TITULO
tk.Label(
    ventana,
    text="୨୧ MY CUTE CALCULATOR ୨୧",
    font=("Arial", 15, "bold"),
    bg=FONDO,
    fg=TEXTO
).pack(pady=(18, 5))

tk.Label(
    ventana,
    text="✧ haz tus cuentas bonitas ✧",
    font=("Arial", 10),
    bg=FONDO,
    fg=ROSA_OSCURO
).pack(pady=(0, 12))

# PANTALLA
pantalla = tk.Entry(
    ventana,
    textvariable=expresion,
    font=("Arial", 23),
    justify="right",
    bg=BLANCO,
    fg=TEXTO,
    relief="flat",
    bd=0
)
pantalla.pack(fill="x", padx=20, ipady=16)

# FUNCIONES
def agregar(valor):
    expresion.set(expresion.get() + str(valor))

def borrar():
    expresion.set("")

def borrar_ultimo():
    expresion.set(expresion.get()[:-1])

# EVALUAR OPERACIONES
def evaluar(nodo):
    operaciones = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
    }

    if isinstance(nodo, ast.Expression):
        return evaluar(nodo.body)

    if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
        return nodo.value

    if isinstance(nodo, ast.BinOp):
        tipo = type(nodo.op)

        if tipo not in operaciones:
            # La segunda parte agregará
            # multiplicación y división.
            raise ValueError("Operación no disponible")

        a = evaluar(nodo.left)
        b = evaluar(nodo.right)

        return operaciones[tipo](a, b)

    if isinstance(nodo, ast.UnaryOp) and isinstance(
        nodo.op, (ast.UAdd, ast.USub)
    ):
        numero = evaluar(nodo.operand)
        return numero if isinstance(nodo.op, ast.UAdd) else -numero

    raise ValueError("Operación inválida")

def resultado():
    try:
        arbol = ast.parse(expresion.get(), mode="eval")
        valor = evaluar(arbol)
        expresion.set(f"{valor:.10g}" if isinstance(valor, float) else str(valor))
    except Exception:
        expresion.set("Operación inválida")

# BOTONES
marco = tk.Frame(ventana, bg=FONDO)
marco.pack(padx=16, pady=18, fill="both", expand=True)

botones = [
    ("C", borrar, ROSA_OSCURO),
    ("⌫", borrar_ultimo, LILA),
    ("(", lambda: agregar("("), LILA),
    (")", lambda: agregar(")"), LILA),

    ("7", lambda: agregar("7"), BLANCO),
    ("8", lambda: agregar("8"), BLANCO),
    ("9", lambda: agregar("9"), BLANCO),
    ("÷", lambda: agregar("/"), ROSA),

    ("4", lambda: agregar("4"), BLANCO),
    ("5", lambda: agregar("5"), BLANCO),
    ("6", lambda: agregar("6"), BLANCO),
    ("×", lambda: agregar("*"), ROSA),

    ("1", lambda: agregar("1"), BLANCO),
    ("2", lambda: agregar("2"), BLANCO),
    ("3", lambda: agregar("3"), BLANCO),
    ("−", lambda: agregar("-"), ROSA),

    ("♡", lambda: agregar("0"), LILA),
    ("0", lambda: agregar("0"), BLANCO),
    (".", lambda: agregar("."), BLANCO),
    ("+", lambda: agregar("+"), ROSA),
]

for i, (texto, funcion, color) in enumerate(botones):
    boton = tk.Button(
        marco,
        text=texto,
        command=funcion,
        font=("Arial", 15, "bold"),
        bg=color,
        fg=TEXTO,
        activebackground=ROSA_OSCURO,
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    boton.grid(
        row=i // 4,
        column=i % 4,
        padx=4,
        pady=4,
        sticky="nsew",
        ipadx=2,
        ipady=9
    )

for columna in range(4):
    marco.grid_columnconfigure(columna, weight=1)

for fila in range(5):
    marco.grid_rowconfigure(fila, weight=1)
