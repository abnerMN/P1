#clase para las celdas vivas
class CeldaViva:
    def __init__(self, x:int, y:int, codigoOrganismo:str):
        self.x=x
        self.y=y
        self.codigoOrganismo=codigoOrganismo
    
    def imprimir(self):
        print("\ncelda viva:-----", "\nx: ", self.x, "\ny: ", self.y, "\ncodigo: ",self.codigoOrganismo )