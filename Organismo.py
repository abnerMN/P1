#clase para los objetos Organismo
class Organismo:
    def __init__(self, codigo:str, nombre:str):
        self.codigo = codigo
        self.nombre = nombre

    
    def imprimir(self):
        print("\norganismo------", "\ncodigo: " , self.codigo, "\nnombre: ", self.nombre)