class Menu:
    def __init__(self, *args):
        self.args = args
    
    def mostrar(self):
        for i, arg in enumerate(self.args):
            print(i+1,' - ',arg)
        print(f"\n{0}", " - ", "Salir")

def ingresa_opciones():
    print("*** Ingresa opciones de tu menú *** ")
    opcion = "S"
    lista = []
    while opcion.upper() == "S":
        entrada_menu = input("Ingresa opción: ")
        lista.append(entrada_menu)
        opcion = input("¿Ingresar otra opción? (s/n): ")
    return lista

# Instancias ejemplos
menu_lucky = Menu("Agregar", "Mostrar", "Buscar")
menu_lucky.mostrar()