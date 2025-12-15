# Paso 9: 

import time
import random
import threading
import multiprocessing
import asyncio

def obtener_tiempo_aleatorio():
    """Retorna un tiempo aleatorio entre 1 y 5 segundos."""
    return random.uniform(1, 5)

def consulta_db(nombre):
    espera = obtener_tiempo_aleatorio()
    print(f"[{nombre}] Iniciando consulta... (tardará {espera:.2f}s)")
    time.sleep(espera) 
    print(f"[{nombre}] Terminó.")

# ASYNCIO
async def consulta_db_async(nombre):
    espera = obtener_tiempo_aleatorio()
    print(f"[{nombre}] Iniciando consulta... (tardará {espera:.2f}s)")
    await asyncio.sleep(espera) 
    print(f"[{nombre}] Terminó.")

def ejecutar_hilos():
    print("\n--- THREADING ---")
    inicio = time.time()
    hilos = []
    
    for i in range(3):
        t = threading.Thread(target=consulta_db, args=(f"Hilo-{i+1}",))
        hilos.append(t)
        t.start()
    
    for t in hilos:
        t.join()
        
    fin = time.time()
    print(f"Tiempo total Hilos: {fin - inicio:.2f} segundos")

def ejecutar_procesos():
    print("\n MULTIPROCESSING ---")
    inicio = time.time()
    procesos = []
    
    for i in range(3):
        p = multiprocessing.Process(target=consulta_db, args=(f"Proceso-{i+1}",))
        procesos.append(p)
        p.start()
    
    for p in procesos:
        p.join()
        
    fin = time.time()
    print(f"Tiempo total Procesos: {fin - inicio:.2f} segundos")

async def ejecutar_async():
    print("\n--- EJECUCIÓN ASÍNCRONA (ASYNCIO) ---")
    inicio = time.time()
    

    await asyncio.gather(
        consulta_db_async("Async-1"),
        consulta_db_async("Async-2"),
        consulta_db_async("Async-3")
    )
        
    fin = time.time()
    print(f"Tiempo total Asyncio: {fin - inicio:.2f} segundos")


if __name__ == "__main__":
    
    # 1. HILOS
    ejecutar_hilos()
    
    # 2. PROCESOS
    ejecutar_procesos()
    
    # 3. ASYNCIO
    asyncio.run(ejecutar_async())

    print("\n--- CONCLUSIÓN ---")
    print("Observarás que el tiempo total NO es la suma de los tiempos individuales,")
    print("sino que es aproximadamente igual al tiempo de la consulta más larga.")