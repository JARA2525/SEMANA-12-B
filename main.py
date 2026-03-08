from servicios.biblioteca_servicio import BibliotecaServicio
from modelos.libro import Libro
from modelos.usuario import Usuario

biblioteca = BibliotecaServicio()

while True:

    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        id_usuario = input("ID usuario: ")

        usuario = Usuario(nombre, id_usuario)

        biblioteca.registrar_usuario(usuario)

    elif opcion == "2":

        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, categoria, isbn)

        biblioteca.agregar_libro(libro)

    elif opcion == "3":

        isbn = input("ISBN libro: ")
        id_usuario = input("ID usuario: ")

        biblioteca.prestar_libro(isbn, id_usuario)

    elif opcion == "4":
        print("Saliendo...")
        break