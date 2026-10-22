# COMPLETAR LAS OPERACIONES
# Reemplazamos la función evaluar para incluir
# suma, resta, multiplicación y división.

def evaluar(nodo):
    operaciones = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    if isinstance(nodo, ast.Expression):
        return evaluar(nodo.body)

    if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
        return nodo.value

    if isinstance(nodo, ast.BinOp):
        tipo = type(nodo.op)

        if tipo not in operaciones:
            raise ValueError("Operación no permitida")

        a = evaluar(nodo.left)
        b = evaluar(nodo.right)

        if isinstance(nodo.op, ast.Div) and b == 0:
            raise ZeroDivisionError("No puedes dividir entre cero")

        return operaciones[tipo](a, b)

    if isinstance(nodo, ast.UnaryOp) and isinstance(
        nodo.op, (ast.UAdd, ast.USub)
    ):
        numero = evaluar(nodo.operand)
        return numero if isinstance(nodo.op, ast.UAdd) else -numero

    raise ValueError("Operación inválida")


# BOTÓN PARA CALCULAR
tk.Button(
    ventana,
    text="✧ CALCULAR ✧",
    command=resultado,
    font=("Arial", 14, "bold"),
    bg=ROSA_OSCURO,
    fg=BLANCO,
    activebackground=ROSA,
    relief="flat",
    cursor="hand2"
).pack(fill="x", padx=20, pady=(0, 10), ipady=9)

# TEXTO INFERIOR
tk.Label(
    ventana,
    text="made with ♡ just for you",
    font=("Arial", 9, "italic"),
    bg=FONDO,
    fg=ROSA_OSCURO
).pack(pady=(0, 12))

# ATAJOS DE TECLADO
ventana.bind("<Return>", lambda evento: resultado())
ventana.bind("<Escape>", lambda evento: borrar())

# INICIAR
ventana.mainloop()