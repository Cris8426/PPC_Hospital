import threading
import time
import random
import asyncio
import multiprocessing

class Paciente:
    def __init__(self, paciente_id, nombre):
        self.paciente_id = paciente_id
        self.nombre = nombre
        self.hora_entrada = None
        self.hora_salida = None
        self.cama_asignada = None
        self.doctor_asignado = None
        self.resultado_diagnostico_ia = None
        self.resultado_analisis_paralelo = None

# Recursos compartidos
camas_disponibles = ["Cama_1", "Cama_2", "Cama_3", "Cama_4", "Cama_5"]
doctores_disponibles = ["Dr. Smith", "Dra. Jones", "Dr. Brown"]

# Locks para controlar el acceso a los recursos compartidos
lock_camas = threading.Lock()
lock_doctores = threading.Lock()

async def simular_diagnostico_ia(paciente):
    print(f"\nPaciente {paciente.nombre} (ID: {paciente.paciente_id}) enviando datos para el Diagnóstico de IA...")
    await asyncio.sleep(random.uniform(1, 3))  # Simula la latencia de la IA
    resultado = f"Diagnóstico IA para {paciente.nombre}: {random.choice(['Normal', 'Grave', 'Moderado'])}"
    print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) recibió el resultado del Diagnóstico de IA: {resultado}")
    paciente.resultado_diagnostico_ia = resultado
    return resultado

def analizar_datos_diagnostico(paciente_info, resultado_ia, resultado_queue):
    print(f"\n[PROCESO PARALELO] Analizando datos del paciente {paciente_info['nombre']} (ID: {paciente_info['id']}) con resultado IA: {resultado_ia}...")
    time.sleep(random.uniform(2, 5))  # Simula un procesamiento intensivo
    resultado_analisis = f"Análisis avanzado para {paciente_info['nombre']}: Encontrados patrones complejos basados en {resultado_ia}."
    print(f"[PROCESO PARALELO] Análisis completado para el paciente {paciente_info['nombre']}. Resultado: {resultado_analisis}")
    resultado_queue.put(resultado_analisis)

def registrar_paciente(paciente):
    paciente.hora_entrada = time.time()
    print(f"\nPaciente {paciente.nombre} (ID: {paciente.paciente_id}) entrando al Registro a las {time.strftime('%H:%M:%S', time.localtime(paciente.hora_entrada))}...")
    time.sleep(random.uniform(0.5, 1.5))  # Simulando tiempo de registro
    print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) registrado.")

def realizar_diagnostico(paciente):
    resultado_ia = asyncio.run(simular_diagnostico_ia(paciente))
    paciente_info = {"id": paciente.paciente_id, "nombre": paciente.nombre}
    resultado_queue = multiprocessing.Queue()
    proceso_paralelo = multiprocessing.Process(target=analizar_datos_diagnostico, args=(paciente_info, resultado_ia, resultado_queue))
    proceso_paralelo.start()
    print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) ha iniciado el análisis de datos en paralelo.")
    proceso_paralelo.join()  # Esperar a que termine el proceso paralelo
    paciente.resultado_analisis_paralelo = resultado_queue.get() # Obtener el resultado del análisis
    print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) ha completado el análisis de datos avanzado.")

def asignar_recursos(paciente):
    print(f"\nPaciente {paciente.nombre} (ID: {paciente.paciente_id}) intentando asignar recursos...")
    while paciente.cama_asignada is None:
        with lock_camas:
            if camas_disponibles:
                paciente.cama_asignada = camas_disponibles.pop(0)
                print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) asignado a la cama {paciente.cama_asignada}.")
            else:
                print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) esperando por una cama...")
        if paciente.cama_asignada is None:
            time.sleep(1)  # Esperar un poco antes de volver a intentar

    while paciente.doctor_asignado is None:
        with lock_doctores:
            if doctores_disponibles:
                paciente.doctor_asignado = doctores_disponibles.pop(0)
                print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) asignado al doctor {paciente.doctor_asignado}.")
            else:
                print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) esperando por un doctor...")
        if paciente.doctor_asignado is None:
            time.sleep(1)  # Esperar un poco antes de volver a intentar

    time.sleep(random.uniform(0.8, 2))  # Simulando el tiempo que toma la asignación en completarse

def realizar_seguimiento(paciente):
    print(f"\nPaciente {paciente.nombre} (ID: {paciente.paciente_id}) en Seguimiento en la cama {paciente.cama_asignada} con el doctor {paciente.doctor_asignado}. Resultado IA: {paciente.resultado_diagnostico_ia}, Análisis Paralelo: {paciente.resultado_analisis_paralelo}...")
    time.sleep(random.uniform(2, 4))  # Simulando tiempo de seguimiento
    paciente.hora_salida = time.time()
    tiempo_en_consultorio = paciente.hora_salida - paciente.hora_entrada
    print(f"Paciente {paciente.nombre} (ID: {paciente.paciente_id}) ha sido dado de alta a las {time.strftime('%H:%M:%S', time.localtime(paciente.hora_salida))} después de estar {tiempo_en_consultorio:.2f} segundos en el consultorio.")
    # Liberar los recursos al dar de alta al paciente
    with lock_camas:
        camas_disponibles.append(paciente.cama_asignada)
        print(f"Cama {paciente.cama_asignada} liberada por el paciente {paciente.nombre}.")
        paciente.cama_asignada = None
    with lock_doctores:
        doctores_disponibles.append(paciente.doctor_asignado)
        print(f"Doctor {paciente.doctor_asignado} disponible nuevamente después de atender a {paciente.nombre}.")
        paciente.doctor_asignado = None

def proceso_paciente(paciente):
    registrar_paciente(paciente)
    realizar_diagnostico(paciente)
    asignar_recursos(paciente)
    realizar_seguimiento(paciente)

if __name__ == "__main__":
    num_total_pacientes = 50
    pacientes_creados = 0
    hilos = []
    tiempo_simulacion = 30  # Simular durante 30 segundos (simulados)
    tiempo_inicio = time.time()

    while pacientes_creados < num_total_pacientes and (time.time() - tiempo_inicio) < tiempo_simulacion:
        # Simular una probabilidad de llegada de un paciente (ajusta la probabilidad según desees)
        if random.random() < 0.4:  # Mayor probabilidad de llegada
            paciente = Paciente(pacientes_creados + 1, f"Paciente_{pacientes_creados + 1}")
            hilo = threading.Thread(target=proceso_paciente, args=(paciente,))
            hilos.append(hilo)
            hilo.start()
            pacientes_creados += 1
            print(f"\n--- Nuevo paciente llegando: {paciente.nombre} (ID: {paciente.paciente_id}) a las {time.strftime('%H:%M:%S', time.localtime())} ---")

        time.sleep(random.uniform(0.3, 1.0))  # Esperar un tiempo aleatorio entre posibles llegadas

    # Esperar a que todos los hilos de los pacientes terminen
    for hilo in hilos:
        hilo.join()

    print("\nSimulación completada.")