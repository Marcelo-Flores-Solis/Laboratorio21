# Paso 5: 
class OperadorInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def procesar_operacion(expresion):
    print(f"\nProcesando: '{expresion}'")
    
    operadores = ['+', '-', '*', '/']
    operador_actual = None
    
    try:
        for op in operadores:
            if op in expresion:
                operador_actual = op
                break
        
        if operador_actual is None:
            raise OperadorInvalidoError(f"El operador en '{expresion}' no es válido o no existe.")
            
        
        partes = expresion.split(operador_actual)
        
        if len(partes) != 2:
             raise ValueError("Formato incorrecto.")

        num1 = float(partes[0].strip())
        num2 = float(partes[1].strip())
        
        resultado = 0
        
        if operador_actual == '+':
            resultado = num1 + num2
        elif operador_actual == '-':
            resultado = num1 - num2
        elif operador_actual == '*':
            resultado = num1 * num2
        elif operador_actual == '/':
            resultado = num1 / num2
            
        print(f"Resultado: {resultado}")

    
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero (Regla matemática).")
        
    except ValueError:
        print("Error: Los valores ingresados no son números válidos.")
        
    except OperadorInvalidoError as e:
        print(f"Error Personalizado: {e}")
        
    except Exception as e:
        print(f"Error inesperado: {e}")


# Caso 1: operacion correcta
procesar_operacion("10 / 2")

# Caso 2: operacion correcta sin espacio
procesar_operacion("50*2")

# Caso 3: divison entre 0
procesar_operacion("5 / 0")

# Caso 4: valor invalido
procesar_operacion("Diez - 5")

# Caso 5: operador invalido
procesar_operacion("10 ^ 2")