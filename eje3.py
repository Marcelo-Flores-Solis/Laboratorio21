#Paso 3: 
import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass  

    def perimetro(self):
        pass  

    def mostrar_datos(self):
        print(f"--- {self.nombre} ---")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base =  base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__("Triangulo")
        self.lado1 =  lado1
        self.lado2 = lado2
        self.lado3 =  lado3

    def area(self):
        s = self.perimetro() / 2
        try:
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        except ValueError:
            return 0.0

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


lista_figuras = [
    Rectangulo(base=10, altura=5),
    Triangulo(lado1=3, lado2=4, lado3=5), 
    Circulo(radio=7)
]


for figura in lista_figuras:
    figura.mostrar_datos()
    print() 