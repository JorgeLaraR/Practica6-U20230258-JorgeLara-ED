class Biblioteca:
    def __init__(self, _libros):
        self.libros = _libros
        
    #mostrar libros.
    def mostrarLibros(self):
        for libro in self.libros:
            print(libro)
            
    def prestarLibros(self, nombreLibros):
        #verificar si el libro existe
        for nombreLibros in self.libros:
            print("Se presto el libro", nombreLibros)
            self.libros.remove(nombreLibros)
        else:
            print("El libro no existe")
            
    def agregaLibro(self, nombreLibros):
        #verificar que no exista
        if nombreLibros not in self.libros:
            print("Se añadio el libro", nombreLibros)
            self.libros.append(nombreLibros)
        else:
            print("El libro ya esxiste")
            
            
            
libros = ["Clean code", "Java", "Analisis"]

biblioteca = Biblioteca(libros)

while True:
    print("1) Agregar Libro")
    print("2) Prestar Libro")
    print("3) Mostrar Libro")
    print("4) Salir")
    
    opcion = int(input("Ingresa un opcion (1-4)"))
    
    if opcion == 1:
        libro = input("\nIngresa el nombre del Libro:")
        biblioteca.agregaLibro(libro)
    elif opcion == 2:
        libro = input("\nIngresa el nombre del Libro:")
        biblioteca.prestarLibros(libro)
    elif opcion == 3:
        print("\nMis libros son")
        biblioteca.mostrarLibros()
    elif opcion == 4:
        break