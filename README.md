# Risk en python

Este proyecto es un juego estratégico basado en Python, donde los jugadores pueden planificar y simular ataques contra territorios enemigos utilizando tropas con características específicas. El objetivo es conquistar todos los territorios optimizando los recursos disponibles.

## Requisitos

- Python 3.8 o superior.

## Cómo jugar

1. Ejecuta el archivo principal:
   ```bash
   python risk.py
   ```

2. Sigue las instrucciones del menú principal para:
   - Mostrar las reglas del juego.
   - Ver el estado del tablero.
   - Generar combinaciones posibles de tropas.
   - Generar permutaciones de ataque.
   - Simular un juego.
   - Optimizar estrategias de ataque.

## Características principales

1. **Selección de tropas**: Los jugadores tienen un presupuesto inicial y deben seleccionar combinaciones de tropas que maximicen su capacidad de ataque.

2. **Optimización de ataques**: Herramientas para calcular el mejor orden de ataque o el mejor ejército según los territorios seleccionados.

3. **Simulación**: Visualización del progreso del juego con detalles sobre las conquistas y resultados intermedios.

4. **Guardado de resultados**: Los resultados de las simulaciones y optimizaciones se guardan en archivos JSON para referencia futura.

## Estructura del proyecto

- `risk.py`: Archivo principal del juego.
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
