#clase para los objetos Organismo
class Organismo:
    def __init__(self, codigo:str, nombre:str, letra:str, color:str,id:int):
        self.codigo = codigo
        self.nombre = nombre
        self.letra =letra
        self.color = color
        self.id=id
    
    def getId(self):
        return self.id
    
    def getColor(self):
        return self.color

    def getLetra(self):
        return self.letra
    
    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre
    

    
    def imprimir(self):
        print("\norganismo------", "\ncodigo: " , self.codigo, "\nnombre: ", self.nombre)