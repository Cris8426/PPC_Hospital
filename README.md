# Simulación de Sistema Hospitalario de Urgencias con Programación Paralela y Concurrente

Este proyecto simula el flujo de pacientes a través de un sistema hospitalario de urgencias, aplicando y diferenciando los paradigmas de programación paralela, concurrente y asíncrona.

## Objetivo

Demostrar la aplicación y diferenciación de los paradigmas de programación paralela, concurrente y asíncrona mediante la simulación de un sistema realista que requiere procesamiento distribuido de tareas en distintos tiempos y recursos.

## Contexto de la Simulación

La simulación modela el proceso que siguen los pacientes que llegan a urgencias, el cual consta de las siguientes etapas:

* **Registro**
* **Diagnóstico automatizado** (simulando el uso de modelos de IA preentrenados)
* **Asignación de recursos** (camas, doctores)
* **Seguimiento y alta**

La simulación implementa procesos concurrentes para manejar múltiples pacientes, paralelismo para simular procesamiento intensivo (análisis de datos del diagnóstico) y tareas asíncronas para simular interacciones con latencia (diagnóstico de IA).

## Requisitos de Implementación

El proyecto implementa:

* **Procesos concurrentes** utilizando la librería `threading` de Python para simular múltiples pacientes interactuando con el sistema simultáneamente.
* **Procesamiento paralelo** utilizando la librería `multiprocessing` de Python para simular el análisis intensivo de los datos del diagnóstico en un proceso separado.
* **Tareas asíncronas** utilizando la librería `asyncio` de Python para simular la latencia en la interacción con un modelo de diagnóstico de IA (mockeado).
* **Control de concurrencia** mediante el uso de `threading.Lock` para proteger el acceso a los recursos compartidos (camas y doctores).

## Lenguaje de Programación

El proyecto está implementado en **Python**.

## Cómo Ejecutar la Simulación

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Clona este repositorio a tu máquina local.
3.  Navega al directorio del repositorio desde tu terminal.
4.  Ejecuta el script principal de la simulación:

    ```bash
    python hospital.py
    ```

5.  Observa la salida en la terminal, que mostrará el progreso de los diferentes pacientes a través del sistema simulado.

## Notas

* La llegada de los pacientes al sistema es simulada de forma aleatoria.
* Los tiempos de procesamiento en cada etapa son simulados con valores aleatorios.
* El número de camas y doctores disponibles es limitado, lo que puede llevar a que algunos pacientes esperen por recursos.

## Autor

Castro López Cristian Alberto
