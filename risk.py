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
    "Infanteria": {"Fuerza": 1, "Costo": 1},
    "Caballeria": {"Fuerza": 3, "Costo": 3},
    "Artilleria": {"Fuerza": 5, "Costo": 5}
}

# Puntos iniciales disponibles
puntos_iniciales = 20

def mostrar_reglas():
    # Muestra las reglas del juego para el jugador.
    reglas = """
    ==================================
            REGLAS DEL JUEGO
    ==================================

    Tipos de Tropas Disponibles:
    a. Infanteria:
       - Soldados basicos, numerosos pero poco efectivos.
       - Costo: 1 punto por tropa.

    b. Caballeria:
       - Tropas rapidas y mas fuertes.
       - Costo: 3 puntos por tropa.

    c. Artilleria:
       - Tropas costosas pero con gran impacto.
       - Costo: 5 puntos por tropa.

    Recursos Disponibles para Entrenar Tropas:
    - Dispones de 20 puntos en total para entrenar tus tropas.
    - El ejercito debe contener al menos:
        1 unidad de infanteria.
        1 unidad de caballeria.
        1 unidad de artilleria.

    Territorios Enemigos:
    - Hay 3 territorios enemigos que debes atacar en el orden indicado.
    - Cada territorio tiene una fuerza de defensa que debes superar con
      la fuerza combinada de tus tropas.

    ==================================
        ¡Buena suerte, estratega!
    ==================================
    """
    print(reglas)

# Representacion inicial del tablero
def inicializar_tablero():
    # Define el estado inicial de los territorios.
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

    # Iterar para calcular todas las posibles distribuciones de tropas.
    for infanteria in range(1, puntos_iniciales // tropas["Infanteria"]["Costo"] + 1):
        for caballeria in range(1, puntos_iniciales // tropas["Caballeria"]["Costo"] + 1):
            for artilleria in range(1, puntos_iniciales // tropas["Artilleria"]["Costo"] + 1):
                # Calcular el costo total de la combinacion.
                costo_total = (
                    infanteria * tropas["Infanteria"]["Costo"] +
                    caballeria * tropas["Caballeria"]["Costo"] +
                    artilleria * tropas["Artilleria"]["Costo"]
                )
                # Calcular la fuerza total de la combinacion.
                fuerza_total = (
                    infanteria * tropas["Infanteria"]["Fuerza"] +
                    caballeria * tropas["Caballeria"]["Fuerza"] +
                    artilleria * tropas["Artilleria"]["Fuerza"]
                )
                # Solo incluir combinaciones validas dentro del limite de puntos.
                if costo_total <= puntos_iniciales:
                    combinaciones.append({
                        "Infanteria": infanteria,
                        "Caballeria": caballeria,
                        "Artilleria": artilleria,
                        "Costo Total": costo_total,
                        "Fuerza Total": fuerza_total
                    })

    # Mostrar las combinaciones posibles.
    print("\n==============================================")
    print("Posibles opciones de combinacion de ejercitos:")
    print("==============================================")
    for i, combinacion in enumerate(combinaciones, start=1):
        print(f"Opcion {i}: {combinacion}")
    print("==========================")
    print(f"Total de combinaciones: {len(combinaciones)}")
    print("==========================")
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
        print(f"Permutacion {i}: {permutacion}")
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

    # Seleccion de combinacion de tropas por el jugador.
    while True:
        opcion_ejercito = input("\nSelecciona el numero de opcion de ejercito (1 a {}): ".format(len(combinaciones)))
        if opcion_ejercito.isdigit() and 1 <= int(opcion_ejercito) <= len(combinaciones):
            opcion_ejercito = int(opcion_ejercito) - 1
            ejercito_seleccionado = combinaciones[opcion_ejercito]
            break
        else:
            print("Entrada invalida. Intentalo de nuevo.")

    # Seleccion de orden de ataque por el jugador.
    while True:
        opcion_ataque = input("\nSelecciona el numero de orden de ataque (1 a {}): ".format(len(permutaciones)))
        if opcion_ataque.isdigit() and 1 <= int(opcion_ataque) <= len(permutaciones):
            opcion_ataque = int(opcion_ataque) - 1
            orden_ataque = permutaciones[opcion_ataque]
            break
        else:
            print("Entrada invalida. Intentalo de nuevo.")

    # Inicio de la simulacion del juego.
    print("\n===========================================")
    print("Comienza la simulacion del juego")
    print("===========================================")
    print(f"Ejercito seleccionado: {ejercito_seleccionado}")
    print(f"Orden de ataque seleccionado: {orden_ataque}")

    resultado_simulacion = {
        "ejercito": ejercito_seleccionado,
        "orden_ataque": orden_ataque,
        "resultado": []
    }

    # Iterar sobre cada territorio en el orden seleccionado.
    for territorio in orden_ataque:
        defensa_territorio = tablero[territorio]["Defensa"]
        fuerza_total = ejercito_seleccionado["Fuerza Total"]

        print(f"\nAtacando {territorio}...")
        time.sleep(2)  # Simular tiempo de ataque.

        # Verificar si el ejercito tiene suficiente fuerza para conquistar el territorio.
        if fuerza_total >= defensa_territorio:
            tablero[territorio]["Estado"] = "Conquistado"
            print(f"{territorio} ha sido conquistado.")
            resultado_simulacion["resultado"].append({"territorio": territorio, "estado": "Conquistado"})
        else:
            print(f"{territorio} no pudo ser conquistado. La defensa fue demasiado fuerte.")
            resultado_simulacion["resultado"].append({"territorio": territorio, "estado": "No Conquistado"})
            break

        # Mostrar el tablero despues de cada ataque.
        mostrar_tablero(tablero)
        time.sleep(2)

    # Finalizar simulacion y reiniciar el tablero.
    print("\n===========================================")
    print("Simulacion terminada")
    print("===========================================")
    mostrar_tablero(tablero)
    guardar_resultados(resultado_simulacion, "simulaciones.json")
    tablero = inicializar_tablero()
    print("\nEl tablero ha sido reiniciado.")
    mostrar_tablero(tablero)

def optimizar_ataques():
    """
    Permite optimizar ataques segun dos opciones:
    1. Seleccionar un ejercito y determinar la mejor permutacion de ataques.
    2. Seleccionar una permutacion y determinar el mejor ejercito.
    """
    combinaciones = generar_combinaciones_tropas()
    permutaciones = generar_permutaciones_territorios(territorios)

    print("\n============================================")
    print("            OPTIMIZAR ATAQUES")
    print("============================================")
    print("1. Seleccionar un ejercito y determinar la mejor permutacion de ataques.")
    print("2. Seleccionar una permutacion y determinar el mejor ejercito.")
    print("============================================")

    while True:
        opcion = input("Selecciona una opcion (1-2): ")
        if opcion == "1":
            while True:
                opcion_ejercito = input("\nSelecciona el numero de opcion de ejercito (1 a {}): ".format(len(combinaciones)))
                if opcion_ejercito.isdigit() and 1 <= int(opcion_ejercito) <= len(combinaciones):
                    opcion_ejercito = int(opcion_ejercito) - 1
                    ejercito_seleccionado = combinaciones[opcion_ejercito]
                    break
                else:
                    print("Entrada invalida. Por favor, introduce un numero valido.")

            # Buscar la mejor permutacion para el ejercito seleccionado.
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

            print("\nEl mejor orden de ataques para el ejercito seleccionado es:")
            print(f"Permutacion: {mejor_permutacion}")
            print(f"Territorios conquistados: {max_territorios_conquistados}")

            guardar_resultados({
                "tipo": "Mejor permutacion",
                "ejercito": ejercito_seleccionado,
                "mejor_permutacion": mejor_permutacion,
                "territorios_conquistados": max_territorios_conquistados
            }, "optimizaciones.json")
            break

        elif opcion == "2":
            while True:
                opcion_permutacion = input("\nSelecciona el numero de permutacion (1 a {}): ".format(len(permutaciones)))
                if opcion_permutacion.isdigit() and 1 <= int(opcion_permutacion) <= len(permutaciones):
                    opcion_permutacion = int(opcion_permutacion) - 1
                    permutacion_seleccionada = permutaciones[opcion_permutacion]
                    break
                else:
                    print("Entrada invalida. Por favor, introduce un numero valido.")

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

            print("\nEl mejor ejercito para la permutacion seleccionada es:")
            print(f"Ejercito: {mejor_ejercito}")
            print(f"Territorios conquistados: {max_territorios_conquistados}")

            guardar_resultados({
                "tipo": "Mejor ejercito",
                "permutacion": permutacion_seleccionada,
                "mejor_ejercito": mejor_ejercito,
                "territorios_conquistados": max_territorios_conquistados
            }, "optimizaciones.json")
            break
        else:
            print("Opcion invalida. Por favor, selecciona una opcion valida (1 o 2).\n")

def guardar_resultados(data, filename):
    """
    Guarda los resultados en un archivo JSON en la misma carpeta que el archivo .py.
    """
    try:
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_json = os.path.join(ruta_actual, filename)

        try:
            with open(ruta_json, "r") as file:
                contenido_actual = json.load(file)
        except FileNotFoundError:
            contenido_actual = []

        contenido_actual.append(data)

        with open(ruta_json, "w") as file:
            json.dump(contenido_actual, file, indent=4)
        print(f"\nLos resultados han sido guardados en {ruta_json}.")
    except Exception as e:
        print(f"\nError al guardar los resultados: {e}")

def menu_principal():
    while True:
        print("\n=======================================")
        print("            MENU PRINCIPAL")
        print("=======================================")
        print("1. Mostrar reglas")
        print("2. Mostrar estado del tablero")
        print("3. Mostrar combinaciones posibles de tropas")
        print("4. Mostrar permutaciones posibles de ataques")
        print("5. Simulacion de juego")
        print("6. Optimizar ataques")
        print("7. Salir de la partida")
        print("=======================================")

        opcion = input("Selecciona una opcion (1-7): ")

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
            print("\nOpcion no valida. Por favor, selecciona una opcion del 1 al 7.")

menu_principal()
