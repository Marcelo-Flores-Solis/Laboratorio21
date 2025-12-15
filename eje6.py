# Paso 6: 
import eje6Geometria 

def main():
    print("--- Probando el módulo geometria.py ---")
    

    r = eje6Geometria.Rectangulo(12, 4)
    c = eje6Geometria.Circulo(5)
    t = eje6Geometria.Triangulo(6, 6, 6) 

    lista_figuras = [r, c, t]

    for fig in lista_figuras:

        print(fig.mostrar_datos())


main()