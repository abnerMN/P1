from ListaSimple import ListaSimple
#clase para los objetos muestra
class Muestra:
    def __init__(self) -> None:
        self.codigo:str
        self.descripcion:str
        self.x:int
        self.y:int
        self.listaOrganismos = ListaSimple()
        self.listaCeldasVivas = ListaSimple()

    def agregarDatos(self, codigo:str, descripcion:str, x:int,y:int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.x = x
        self.y = y


    def getCodigo(self):
        return self.codigo
    
    def getDescripcion(self):
        return self.descripcion
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setListaOrganismos(self, Lista:ListaSimple()):
        self.listaOrganismos=Lista
    
    def getListaOrganismos(self):
        return self.listaOrganismos
    
    def setListaCeldasVivas(self,Lista: ListaSimple()):
        self.listaCeldasVivas=Lista
    
    def getListaCeldasVivas(self):
        return self.listaCeldasVivas
    
    def imprimir(self):
        print("\nMUESTRA_____","\ncodigo: ", self.codigo, "\ndescripcion: ",self.descripcion,"\nx: ", self.x, "\ny: ",self.y )
    



