class Pelicula:
    def __init__(self, nombre, director, genero):
        self.__nombre = nombre
        self.director = director
        self.genero = genero

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

    def __str__(self):
        return f"Película: {self.__nombre} Dirigida por: {self.director} Género: {self.genero}"
    
import os


class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}"
        self.peliculas = self.cargar_peliculas()

    def cargar_peliculas(self):
        peliculas = []
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    nombre, director, genero = linea.strip().split(',')
                    peliculas.append(Pelicula(nombre, director, genero))
        except FileNotFoundError:
            print(f"El archivo '{self.ruta_archivo}' no existe. Se creará un nuevo catálogo.")
        return peliculas

    def guardar_peliculas(self):
        with open(self.ruta_archivo, 'w') as archivo:
            for pelicula in self.peliculas:
                archivo.write(f"{pelicula.nombre},{pelicula.director},{pelicula.genero}\n")

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_peliculas()

    def listar(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for pelicula in self.peliculas:
                print(pelicula)

    def eliminar(self):
        try:
            os.remove(self.ruta_archivo)
            self.peliculas = []
            print(f"El catálogo '{self.nombre}' fue eliminado.")
        except FileNotFoundError:
            print(f"El catálogo '{self.nombre}' no existe.")
            
            
def mostrar_menu():
    print("\nSelecciona una opción:")
    print("1. Agregar una película")
    print("2. Listado de películas")
    print("3. Eliminar el catálogo")
    print("4. Salir")

def main():
    nombre_catalogo = input("Por favor ingresa el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la película: ")
            director = input("Director: ")
            genero = input("Género: ")
            pelicula = Pelicula(nombre, director, genero)
            catalogo.agregar(pelicula)
        elif opcion == '2':
            catalogo.listar()
        elif opcion == '3':
            catalogo.eliminar()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("La opción no es válida. Intentalo nuevamente.")

if __name__ == "__main__":
    main()     
    
           