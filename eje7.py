# Paso 7: 

def copiar_archivo_texto(origen, destino):
    
    try:
        with open(origen, 'r', encoding='utf-8') as f_origen, open(destino, 'w', encoding='utf-8') as f_destino:
            contenido = f_origen.read()
            f_destino.write(contenido)
        print(f"Se copió el texto de '{origen}' a '{destino}'.")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def copiar_archivo_binario(origen, destino):
    
    try:
        with open(origen, 'rb') as f_origen, open(destino, 'wb') as f_destino:
            chunk = f_origen.read(1024) # Leer 1KB a la vez
            while chunk:
                f_destino.write(chunk)
                chunk = f_origen.read(1024)
                
        print(f"Se copio el archivo binario de '{origen}' a '{destino}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")



if __name__ == "__main__":

    # 1. Prueba de TEXTO
    with open("nota.txt", "w", encoding='utf-8') as f:
        f.write("Prueba pruebita pruebota .\nLaboratorio 21.")
    
    # Ejecutamos la copia
    copiar_archivo_texto("nota.txt", "nota_copia.txt")
    copiar_archivo_binario("prueba.pdf", "prueba_copia.pdf") 