from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()


    def agregar_libro(self, libro):
        self.libros[libro.get_isbn()] = libro
        print("Libro agregado.")


    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")


    def registrar_usuario(self, usuario):

        if usuario.get_id() in self.ids_usuarios:
            print("Usuario ya registrado")
            return

        self.ids_usuarios.add(usuario.get_id())
        self.usuarios[usuario.get_id()] = usuario
        print("Usuario registrado")


    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")


    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no disponible")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.agregar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente")


    def devolver_libro(self, libro, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)

        self.libros[libro.get_isbn()] = libro

        print("Libro devuelto")