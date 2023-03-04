from ListaSimple import ListaSimple
#clase para los objetos muestra
class Muestra:
    def __init__(self, codigo:str, descripcion:str, x:int,y:int) -> None:
        self.codigo = codigo
        self.descripcion = descripcion
        self.x = x
        self.y = y
        self.listaOrganismos = ListaSimple()
        self.listaCeldasVivas = ListaSimple()
    
    def imprimir(self):
        print("MUESTRA_____","\ncodigo: ", self.codigo, "\ndescripcion: ",self.descripcion,"\nx: ", self.x, "\ny: ",self.y )
    



