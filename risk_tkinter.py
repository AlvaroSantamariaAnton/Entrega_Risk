import tkinter as tk
from tkinter import messagebox, simpledialog
from itertools import permutations

# Configuración inicial del juego
territorios = {
    "Territorio 1": {"Defensa": 10},
    "Territorio 2": {"Defensa": 15},
    "Territorio 3": {"Defensa": 12}
}

tropas = {
    "Infanteria": {"Fuerza": 1, "Costo": 1},
    "Caballeria": {"Fuerza": 3, "Costo": 3},
    "Artilleria": {"Fuerza": 5, "Costo": 5}
}

puntos_iniciales = 20
tablero = {}
combinaciones = []
permutaciones = []

# Funciones del juego
def inicializar_tablero():
    return {
        "Territorio 1": {"Defensa": 10, "Estado": "Disponible"},
        "Territorio 2": {"Defensa": 15, "Estado": "Disponible"},
        "Territorio 3": {"Defensa": 12, "Estado": "Disponible"}
    }

def mostrar_reglas():
    reglas = """
    ==================================
            REGLAS DEL JUEGO
    ==================================

    Tipos de Tropas Disponibles:
    a. Infanteria:
       - Soldados básicos, numerosos pero poco efectivos.
       - Costo: 1 punto por tropa.

    b. Caballeria:
       - Tropas rápidas y más fuertes.
       - Costo: 3 puntos por tropa.

    c. Artilleria:
       - Tropas costosas pero con gran impacto.
       - Costo: 5 puntos por tropa.

    Recursos Disponibles para Entrenar Tropas:
    - Dispones de 20 puntos en total para entrenar tus tropas.
    - El ejército debe contener al menos:
        1 unidad de infantería.
        1 unidad de caballería.
        1 unidad de artillería.

    Territorios Enemigos:
    - Hay 3 territorios enemigos que debes atacar en el orden indicado.
    - Cada territorio tiene una fuerza de defensa que debes superar con
      la fuerza combinada de tus tropas.

    ==================================
        ¡Buena suerte, estratega!
    ==================================
    """
    messagebox.showinfo("Reglas del Juego", reglas)

def mostrar_tablero():
    tablero_texto = "\n".join([f"{k}: Defensa {v['Defensa']}, Estado {v['Estado']}" for k, v in tablero.items()])
    messagebox.showinfo("Estado del Tablero", tablero_texto)

def generar_combinaciones_tropas():
    global combinaciones
    combinaciones = []

    for infanteria in range(1, puntos_iniciales // tropas["Infanteria"]["Costo"] + 1):
        for caballeria in range(1, puntos_iniciales // tropas["Caballeria"]["Costo"] + 1):
            for artilleria in range(1, puntos_iniciales // tropas["Artilleria"]["Costo"] + 1):
                costo_total = (
                    infanteria * tropas["Infanteria"]["Costo"] +
                    caballeria * tropas["Caballeria"]["Costo"] +
                    artilleria * tropas["Artilleria"]["Costo"]
                )
                fuerza_total = (
                    infanteria * tropas["Infanteria"]["Fuerza"] +
                    caballeria * tropas["Caballeria"]["Fuerza"] +
                    artilleria * tropas["Artilleria"]["Fuerza"]
                )
                if costo_total <= puntos_iniciales:
                    combinaciones.append({
                        "Infanteria": infanteria,
                        "Caballeria": caballeria,
                        "Artilleria": artilleria,
                        "Costo Total": costo_total,
                        "Fuerza Total": fuerza_total
                    })

def mostrar_combinaciones():
    generar_combinaciones_tropas()
    combinaciones_texto = "\n".join(
        [f"Opción {i+1}: {c}" for i, c in enumerate(combinaciones)]
    )
    messagebox.showinfo("Combinaciones de Tropas", combinaciones_texto)

def generar_permutaciones_territorios():
    global permutaciones
    nombres_territorios = list(territorios.keys())
    permutaciones = list(permutations(nombres_territorios))

def mostrar_permutaciones():
    generar_permutaciones_territorios()
    permutaciones_texto = "\n".join(
        [f"Opción {i+1}: {p}" for i, p in enumerate(permutaciones)]
    )
    messagebox.showinfo("Permutaciones de Ataque", permutaciones_texto)

def simulacion():
    generar_combinaciones_tropas()
    generar_permutaciones_territorios()

    if not combinaciones or not permutaciones:
        messagebox.showerror("Error", "No hay combinaciones o permutaciones disponibles.")
        return

    seleccion_combinacion = simpledialog.askinteger(
        "Simulación", f"Selecciona el número de opción de ejército (1 a {len(combinaciones)}):")
    if seleccion_combinacion is None or not (1 <= seleccion_combinacion <= len(combinaciones)):
        messagebox.showerror("Error", "Selección inválida.")
        return
    ejercito = combinaciones[seleccion_combinacion - 1]

    seleccion_permutacion = simpledialog.askinteger(
        "Simulación", f"Selecciona el número de orden de ataque (1 a {len(permutaciones)}):")
    if seleccion_permutacion is None or not (1 <= seleccion_permutacion <= len(permutaciones)):
        messagebox.showerror("Error", "Selección inválida.")
        return
    orden_ataque = permutaciones[seleccion_permutacion - 1]

    resultados = []
    fuerza_total = ejercito["Fuerza Total"]

    for territorio in orden_ataque:
        defensa = territorios[territorio]["Defensa"]
        if fuerza_total >= defensa:
            resultados.append(f"{territorio}: Conquistado")
        else:
            resultados.append(f"{territorio}: No Conquistado")
            break

    resultados_texto = "\n".join(resultados)
    messagebox.showinfo("Resultados de la Simulación", resultados_texto)

def optimizar():
    generar_combinaciones_tropas()
    generar_permutaciones_territorios()

    if not combinaciones or not permutaciones:
        messagebox.showerror("Error", "No hay combinaciones o permutaciones disponibles.")
        return

    opcion = simpledialog.askinteger(
        "Optimización", "Selecciona una opción:\n1. Mejor orden de ataque para un ejército.\n2. Mejor ejército para un orden de ataque."
    )
    if opcion not in (1, 2):
        messagebox.showerror("Error", "Selección inválida.")
        return

    if opcion == 1:
        seleccion_combinacion = simpledialog.askinteger(
            "Optimización", f"Selecciona el número de opción de ejército (1 a {len(combinaciones)}):")
        if seleccion_combinacion is None or not (1 <= seleccion_combinacion <= len(combinaciones)):
            messagebox.showerror("Error", "Selección inválida.")
            return
        ejercito = combinaciones[seleccion_combinacion - 1]

        max_territorios = 0
        mejor_permutacion = None
        for permutacion in permutaciones:
            territorios_conquistados = 0
            fuerza_total = ejercito["Fuerza Total"]

            for territorio in permutacion:
                defensa = territorios[territorio]["Defensa"]
                if fuerza_total >= defensa:
                    territorios_conquistados += 1
                else:
                    break

            if territorios_conquistados > max_territorios:
                max_territorios = territorios_conquistados
                mejor_permutacion = permutacion

        messagebox.showinfo("Mejor Orden", f"Mejor orden de ataque: {mejor_permutacion}\nTerritorios conquistados: {max_territorios}")
    elif opcion == 2:
        seleccion_permutacion = simpledialog.askinteger(
            "Optimización", f"Selecciona el número de orden de ataque (1 a {len(permutaciones)}):")
        if seleccion_permutacion is None or not (1 <= seleccion_permutacion <= len(permutaciones)):
            messagebox.showerror("Error", "Selección inválida.")
            return
        orden_ataque = permutaciones[seleccion_permutacion - 1]

        max_territorios = 0
        mejor_ejercito = None
        for ejercito in combinaciones:
            territorios_conquistados = 0
            fuerza_total = ejercito["Fuerza Total"]

            for territorio in orden_ataque:
                defensa = territorios[territorio]["Defensa"]
                if fuerza_total >= defensa:
                    territorios_conquistados += 1
                else:
                    break

            if territorios_conquistados > max_territorios:
                max_territorios = territorios_conquistados
                mejor_ejercito = ejercito

        messagebox.showinfo("Mejor Ejército", f"Mejor ejército: {mejor_ejercito}\nTerritorios conquistados: {max_territorios}")

# Inicialización del tablero
tablero = inicializar_tablero()

# Interfaz con Tkinter
root = tk.Tk()
root.title("Juego de Estrategia")

# Crear botones
boton_reglas = tk.Button(root, text="Mostrar Reglas", command=mostrar_reglas, width=30, height=2)
boton_tablero = tk.Button(root, text="Mostrar Tablero", command=mostrar_tablero, width=30, height=2)
boton_combinaciones = tk.Button(root, text="Mostrar Combinaciones", command=mostrar_combinaciones, width=30, height=2)
boton_permutaciones = tk.Button(root, text="Mostrar Permutaciones", command=mostrar_permutaciones, width=30, height=2)
boton_simulacion = tk.Button(root, text="Simulación de Juego", command=simulacion, width=30, height=2)
boton_optimizar = tk.Button(root, text="Optimizar Ataques", command=optimizar, width=30, height=2)
boton_salir = tk.Button(root, text="Salir", command=root.quit, width=30, height=2)

# Posicionar botones
boton_reglas.pack(pady=10)
boton_tablero.pack(pady=10)
boton_combinaciones.pack(pady=10)
boton_permutaciones.pack(pady=10)
boton_simulacion.pack(pady=10)
boton_optimizar.pack(pady=10)
boton_salir.pack(pady=10)

# Ejecutar la ventana gráfica
root.mainloop()
