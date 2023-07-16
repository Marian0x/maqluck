class menu:
    def __init__(self, *args, opcion):
        self.opcion = opcion
        self.args = args

    def mostrar(self):
        for arg in self.args:
            print

