import os
import json
import time
from itertools import permutations

# Fuerza de los Territorios Enemigos
territorios = {
    "Territorio 1": {"Defensa": 10},
    "Territorio 2": {"Defensa": 15},
    "Territorio 3": {"Defensa": 12}
}

# Tropas y Recursos
tropas = {
    "Infantería": {"Fuerza": 1, "Costo": 1},
    "Caballería": {"Fuerza": 3, "Costo": 3},
    "Artillería": {"Fuerza": 5, "Costo": 5}
}

# Puntos iniciales disponibles
puntos_iniciales = 20

def mostrar_reglas():
    reglas = """
    ==================================
            REGLAS DEL JUEGO
    ==================================

    Tipos de Tropas Disponibles:
    a. Infantería:
       - Soldados básicos, numerosos pero poco efectivos.
       - Costo: 1 punto por tropa.

    b. Caballería:
       - Tropas rápidas y más fuertes.
       - Costo: 3 puntos por tropa.

    c. Artillería:
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
    print(reglas)

# Representación inicial del tablero
def inicializar_tablero():
    return {
        "Territorio 1": {"Defensa": 10, "Estado": "Disponible"},
        "Territorio 2": {"Defensa": 15, "Estado": "Disponible"},
        "Territorio 3": {"Defensa": 12, "Estado": "Disponible"}
    }

tablero = inicializar_tablero()

def mostrar_tablero(tablero):
    """
    Muestra el estado actual del tablero de juego.
    """
    print("\n==========================================")
    print("Estado actual del tablero:")
    print("==========================================")
    for territorio, info in tablero.items():
        print(f"{territorio} - Defensa: {info['Defensa']}, Estado: {info['Estado']}")
    print("==========================================")

def generar_combinaciones_tropas():
    """
    Genera todas las combinaciones posibles de tropas respetando los recursos disponibles
    y asegurando al menos una unidad de cada tipo de tropa.
    """
    combinaciones = []

    for infanteria in range(1, puntos_iniciales // tropas["Infantería"]["Costo"] + 1):
        for caballeria in range(1, puntos_iniciales // tropas["Caballería"]["Costo"] + 1):
            for artilleria in range(1, puntos_iniciales // tropas["Artillería"]["Costo"] + 1):
                costo_total = (
                    infanteria * tropas["Infantería"]["Costo"] +
                    caballeria * tropas["Caballería"]["Costo"] +
                    artilleria * tropas["Artillería"]["Costo"]
                )
                fuerza_total = (
                    infanteria * tropas["Infantería"]["Fuerza"] +
                    caballeria * tropas["Caballería"]["Fuerza"] +
                    artilleria * tropas["Artillería"]["Fuerza"]
                )
                if costo_total <= puntos_iniciales:
                    combinaciones.append({
                        "Infantería": infanteria,
                        "Caballería": caballeria,
                        "Artillería": artilleria,
                        "Costo Total": costo_total,
                        "Fuerza Total": fuerza_total
                    })

    print("\n==============================================")
    print("Posibles opciones de combinación de ejércitos:")
    print("==============================================")
    for i, combinacion in enumerate(combinaciones, start=1):
        print(f"Opción {i}: {combinacion}")
    print("===========================")
    print(f"Total de combinaciones: {len(combinaciones)}")
    print("===========================")
    return combinaciones

def generar_permutaciones_territorios(territorios):
    """
    Genera todas las permutaciones posibles del orden de ataque a los territorios enemigos.
    """
    nombres_territorios = list(territorios.keys())
    permutaciones = list(permutations(nombres_territorios))
    print("\n===========================================")
    print("Permutaciones posibles del orden de ataque:")
    print("===========================================")
    for i, permutacion in enumerate(permutaciones, start=1):
        print(f"Permutación {i}: {permutacion}")
    print("==========================")
    print(f"Total de permutaciones: {len(permutaciones)}")
    print("==========================")
    return permutaciones

def simulacion_juego():
    """
    Simula el juego con tiempos de espera y muestra el estado del tablero
    entre ataques. Reinicia el tablero al final.
    """
    global tablero
    combinaciones = generar_combinaciones_tropas()
    permutaciones = generar_permutaciones_territorios(territorios)

    # Selección de combinación de tropas
    while True:
        opcion_ejercito = input("\nSelecciona el número de opción de ejército (1 a {}): ".format(len(combinaciones)))
        if opcion_ejercito.isdigit() and 1 <= int(opcion_ejercito) <= len(combinaciones):
            opcion_ejercito = int(opcion_ejercito) - 1
            ejercito_seleccionado = combinaciones[opcion_ejercito]
            break
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

    # Selección de orden de ataque
    while True:
        opcion_ataque = input("\nSelecciona el número de orden de ataque (1 a {}): ".format(len(permutaciones)))
        if opcion_ataque.isdigit() and 1 <= int(opcion_ataque) <= len(permutaciones):
            opcion_ataque = int(opcion_ataque) - 1
            orden_ataque = permutaciones[opcion_ataque]
            break
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

    # Simulación del juego
    print("\n===========================================")
    print("Comienza la simulación del juego")
    print("===========================================")
    print(f"Ejército seleccionado: {ejercito_seleccionado}")
    print(f"Orden de ataque seleccionado: {orden_ataque}")

    resultado_simulacion = {
        "ejercito": ejercito_seleccionado,
        "orden_ataque": orden_ataque,
        "resultado": []
    }

    for territorio in orden_ataque:
        defensa_territorio = tablero[territorio]["Defensa"]
        fuerza_total = ejercito_seleccionado["Fuerza Total"]

        print(f"\nAtacando {territorio}...")
        time.sleep(2)

        if fuerza_total >= defensa_territorio:
            tablero[territorio]["Estado"] = "Conquistado"
            print(f"{territorio} ha sido conquistado.")
            resultado_simulacion["resultado"].append({"territorio": territorio, "estado": "Conquistado"})
        else:
            print(f"{territorio} no pudo ser conquistado. La defensa fue demasiado fuerte.")
            resultado_simulacion["resultado"].append({"territorio": territorio, "estado": "No Conquistado"})
            break

        mostrar_tablero(tablero)
        time.sleep(2)

    print("\n===========================================")
    print("Simulación terminada")
    print("===========================================")
    mostrar_tablero(tablero)

    # Guardar los resultados en JSON
    guardar_resultados(resultado_simulacion, "simulaciones.json")

    # Reiniciar el tablero al final
    tablero = inicializar_tablero()
    print("\nEl tablero ha sido reiniciado.")
    mostrar_tablero(tablero)

def optimizar_ataques():
    """
    Permite optimizar ataques según dos opciones:
    1. Seleccionar un ejército y determinar la mejor permutación de ataques.
    2. Seleccionar una permutación y determinar el mejor ejército.
    """
    combinaciones = generar_combinaciones_tropas()
    permutaciones = generar_permutaciones_territorios(territorios)

    print("\n============================================")
    print("            OPTIMIZAR ATAQUES")
    print("============================================")
    print("1. Seleccionar un ejército y determinar la mejor permutación de ataques.")
    print("2. Seleccionar una permutación y determinar el mejor ejército.")
    print("============================================")

    while True:
        opcion = input("Selecciona una opción (1-2): ")
        if opcion == "1":
            # Selección de un ejército
            while True:
                opcion_ejercito = input("\nSelecciona el número de opción de ejército (1 a {}): ".format(len(combinaciones)))
                if opcion_ejercito.isdigit() and 1 <= int(opcion_ejercito) <= len(combinaciones):
                    opcion_ejercito = int(opcion_ejercito) - 1
                    ejercito_seleccionado = combinaciones[opcion_ejercito]
                    break
                else:
                    print("Entrada inválida. Por favor, introduce un número válido.")

            # Determinar la mejor permutación de ataques
            mejor_permutacion = None
            max_territorios_conquistados = 0

            for permutacion in permutaciones:
                territorios_conquistados = 0
                fuerza_total = ejercito_seleccionado["Fuerza Total"]

                for territorio in permutacion:
                    defensa = territorios[territorio]["Defensa"]
                    if fuerza_total >= defensa:
                        territorios_conquistados += 1
                    else:
                        break

                if territorios_conquistados > max_territorios_conquistados:
                    max_territorios_conquistados = territorios_conquistados
                    mejor_permutacion = permutacion

            resultado_optimizacion = {
                "tipo": "Mejor permutación",
                "ejercito": ejercito_seleccionado,
                "mejor_permutacion": mejor_permutacion,
                "territorios_conquistados": max_territorios_conquistados
            }

            print("\nEl mejor orden de ataques para el ejército seleccionado es:")
            print(f"Permutación: {mejor_permutacion}")
            print(f"Territorios conquistados: {max_territorios_conquistados}")

            # Guardar resultados
            guardar_resultados(resultado_optimizacion, "optimizaciones.json")
            break

        elif opcion == "2":
            # Selección de una permutación
            while True:
                opcion_permutacion = input("\nSelecciona el número de permutación (1 a {}): ".format(len(permutaciones)))
                if opcion_permutacion.isdigit() and 1 <= int(opcion_permutacion) <= len(permutaciones):
                    opcion_permutacion = int(opcion_permutacion) - 1
                    permutacion_seleccionada = permutaciones[opcion_permutacion]
                    break
                else:
                    print("Entrada inválida. Por favor, introduce un número válido.")

            # Determinar el mejor ejército para la permutación
            mejor_ejercito = None
            max_territorios_conquistados = 0

            for ejercito in combinaciones:
                territorios_conquistados = 0
                fuerza_total = ejercito["Fuerza Total"]

                for territorio in permutacion_seleccionada:
                    defensa = territorios[territorio]["Defensa"]
                    if fuerza_total >= defensa:
                        territorios_conquistados += 1
                    else:
                        break

                if territorios_conquistados > max_territorios_conquistados:
                    max_territorios_conquistados = territorios_conquistados
                    mejor_ejercito = ejercito

            resultado_optimizacion = {
                "tipo": "Mejor ejército",
                "permutacion": permutacion_seleccionada,
                "mejor_ejercito": mejor_ejercito,
                "territorios_conquistados": max_territorios_conquistados
            }

            print("\nEl mejor ejército para la permutación seleccionada es:")
            print(f"Ejército: {mejor_ejercito}")
            print(f"Territorios conquistados: {max_territorios_conquistados}")

            # Guardar resultados
            guardar_resultados(resultado_optimizacion, "optimizaciones.json")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida (1 o 2).\n")

# Función para guardar los resultados en un archivo JSON
def guardar_resultados(data, filename):
    """
    Guarda los resultados en un archivo JSON en la misma carpeta que el archivo .py.

    :param data: Datos a guardar (puede ser simulaciones o optimizaciones).
    :param filename: Nombre del archivo JSON donde se guardarán los datos.
    """
    try:
        # Obtener la ruta completa en la misma carpeta que el archivo .py
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_json = os.path.join(ruta_actual, filename)

        # Leer el archivo si ya existe para añadir datos
        try:
            with open(ruta_json, "r") as file:
                contenido_actual = json.load(file)
        except FileNotFoundError:
            contenido_actual = []

        # Agregar los nuevos datos
        contenido_actual.append(data)

        # Guardar en el archivo
        with open(ruta_json, "w") as file:
            json.dump(contenido_actual, file, indent=4)
        print(f"\nLos resultados han sido guardados en {ruta_json}.")
    except Exception as e:
        print(f"\nError al guardar los resultados: {e}")

def menu_principal():
    while True:
        print("\n=======================================")
        print("            MENÚ PRINCIPAL")
        print("=======================================")
        print("1. Mostrar reglas")
        print("2. Mostrar estado del tablero")
        print("3. Mostrar combinaciones posibles de tropas")
        print("4. Mostrar permutaciones posibles de ataques")
        print("5. Simulación de juego")
        print("6. Optimizar ataques")
        print("7. Salir de la partida")
        print("=======================================")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            mostrar_reglas()
        elif opcion == "2":
            mostrar_tablero(tablero)
        elif opcion == "3":
            generar_combinaciones_tropas()
        elif opcion == "4":
            generar_permutaciones_territorios(territorios)
        elif opcion == "5":
            simulacion_juego()
        elif opcion == "6":
            optimizar_ataques()
        elif opcion == "7":
            print("\nSaliendo de la partida. ¡Gracias por jugar!")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 7.")

# Iniciar el menú principal
menu_principal()