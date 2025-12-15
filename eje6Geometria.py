# Paso 6 geometria.py:

import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def mostrar_datos(self):
        return f"{self.nombre} -> Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__("Triángulo")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        s = self.perimetro() / 2
        try:
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        except ValueError:
            return 0.0

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3