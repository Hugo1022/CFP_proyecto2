class Menu:

    def __init__(self, texto):
        self.texto = texto

    def imprimirMenu(self):
        print(self.texto)

    def guardarOpcion(self):
        opcion = int(input("Por favor ingrese una opcion.\n"))
        return opcion
    