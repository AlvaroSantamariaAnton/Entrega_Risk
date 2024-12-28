# Risk en python

Este proyecto es un juego estratégico basado en Python, donde los jugadores pueden planificar y simular ataques contra territorios enemigos utilizando tropas con características específicas. El objetivo es conquistar todos los territorios optimizando los recursos disponibles.

## Requisitos

- Python 3.8 o superior.
- Tkinter (generalmente incluido con Python)

## Ejecución

1. Ejecuta el archivo desde la terminal:

   ### `risk.py`
   ```bash
   python risk.py
   ```

   ### `risk_tkinter.py`
   ```bash
   python risk_tkinter.py
   ```

2. Sigue las instrucciones del menú principal para:
   - Mostrar las reglas del juego.
   - Ver el estado del tablero.
   - Generar combinaciones posibles de tropas.
   - Generar permutaciones de ataque.
   - Simular un juego.
   - Optimizar estrategias de ataque.

## Archivos disponibles

### 1. `risk.py`
Este archivo contiene la lógica principal del juego y se ejecuta en la consola. Los jugadores pueden interactuar con el sistema mediante un menú de texto.

### 2. `risk_tkinter.py`
Este nuevo archivo implementa la misma funcionalidad que `risk.py`, pero con una interfaz gráfica creada utilizando la librería **Tkinter**. Ahora, los jugadores pueden interactuar con el juego a través de botones y cuadros de diálogo, lo que hace que la experiencia sea más intuitiva y visual.

## Funcionalidades y características principales

### Comunes a ambos archivos:

- **Configuración inicial:** Define territorios enemigos con diferentes niveles de defensa y un sistema de tropas con características específicas.
- **Selección de tropas**: Los jugadores tienen un presupuesto inicial y deben seleccionar combinaciones de tropas que maximicen su capacidad de ataque.
- **Generación de combinaciones:** Calcula todas las posibles combinaciones de tropas dentro del límite de puntos disponibles.
- **Generación de permutaciones:** Calcula todas las posibles permutaciones del orden de ataque a los territorios enemigos.
- **Simulación de juego:** Permite seleccionar un ejército y un orden de ataque para intentar conquistar los territorios.
- **Optimización de estrategias:** Encuentra el mejor orden de ataque para un ejército seleccionado o el mejor ejército para un orden de ataque específico.

### Exclusivo de `risk.py`:
- **Guardado de resultados**: Los resultados de las simulaciones y optimizaciones se guardan en archivos JSON para referencia futura.

### Exclusivo de `risk_tkinter.py`:
- **Interfaz gráfica:** Una ventana interactiva con botones que reemplaza el menú de texto.
- **Cuadros de diálogo:** Los mensajes de estado y opciones se muestran en cuadros emergentes en lugar de texto en consola.

## Estructura del proyecto

- `risk.py`: Archivo principal del juego.
- `risk_tkinter.py`: Archivo gráfico del juego.
- `simulaciones.json`: Archivo donde se guardan los resultados de las simulaciones.
- `optimizaciones.json`: Archivo donde se guardan las optimizaciones calculadas.

## Reglas del juego

- Cada territorio tiene un nivel de defensa.
- Los jugadores deben formar un ejército que supere la defensa de los territorios en el orden seleccionado.
- Tipos de tropas disponibles:
  - **Infantería**: Tropas básicas con bajo costo y fuerza.
  - **Caballería**: Tropas más fuertes con un costo moderado.
  - **Artillería**: Tropas de alto impacto pero costosas.
- Recursos iniciales: 20 puntos para asignar a las tropas.

## Link del repositorio

https://github.com/AlvaroSantamariaAnton/Entrega_Risk.git
