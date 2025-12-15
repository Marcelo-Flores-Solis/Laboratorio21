# Paso 4:

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True  

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Se presto el libro '{self.titulo}'."
        else:
            return f"Error: El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        self.disponible = True
        return f"Has devuelto el libro '{self.titulo}'."

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} ({self.anio}) - [{estado}]"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamano_mb):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def prestar(self):
        return f"Éxito: Has accedido al libro digital '{self.titulo}' ({self.formato})."

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Formato: {self.formato} - {self.tamano_mb}MB"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def listar_libros(self):
        print("\n--- Catalogo de la Biblioteca ---")
        for libro in self.libros:
            print(libro)
        print("---------------------------------")

    def buscar_por_autor(self, autor_buscado):
        print(f"\n--- Buscando libros de: {autor_buscado} ---")
        encontrados = [lib for lib in self.libros if lib.autor.lower() == autor_buscado.lower()]
        
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros de este autor")

    def prestar_libro(self, titulo_buscado):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                print(libro.prestar())
                return
        print(f"Error: El libro '{titulo_buscado}' no existe en la biblioteca.")




mi_biblioteca = Biblioteca()

#libros
l1 = Libro("Cien años de soledad", "Garcia Marquez", 1967)
l2 = Libro("1984", "George Orwell", 1949)
l3 = Libro("El Principito", "Antoine ", 1943)

d1 = LibroDigital("Python Avanzado", "Guido van Rossum", 2023, "PDF", 5.2)
d2 = LibroDigital("Clean Code", "Robert C. Martin", 2008, "EPUB", 2.1)

print("--- Inicializando Biblioteca ---")
mi_biblioteca.agregar_libro(l1)
mi_biblioteca.agregar_libro(l2)
mi_biblioteca.agregar_libro(l3)
mi_biblioteca.agregar_libro(d1)
mi_biblioteca.agregar_libro(d2)

# listar
print("\n Listando libros")
mi_biblioteca.listar_libros()

# prestar
print("\n Prestando libro 1984")
mi_biblioteca.prestar_libro("1984")

# prestamo repetido
print("\n> Prestando libro 1984")
mi_biblioteca.prestar_libro("1984")

# Prestando python 5 veces
print("\n Prestando libro digital 'Python Avanzado' 5 veces...")
for i in range(1, 6):
    print(f"Intento {i}: ", end="")
    mi_biblioteca.prestar_libro("Python Avanzado")

# verificar estado
mi_biblioteca.listar_libros()

# buscando libros por autor 
mi_biblioteca.buscar_por_autor("Garcia Marquez")
mi_biblioteca.buscar_por_autor("JK Rowling") 