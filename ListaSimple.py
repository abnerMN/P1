from Organismo import Organismo
from CeldaViva import CeldaViva

class ListaSimple:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_siguiente = None

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

#imprimir elementos de la lista
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual != None:
            nodo_actual.valor.imprimir()
            nodo_actual = nodo_actual.nodo_siguiente

    
#agregar elemento
    def append(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1


#prueba lista
nuevo = Organismo("scp096", "metamorfo")
nuevo1 = Organismo("sct056", "reptiliano")
nuevo2 = CeldaViva(12,12,"SCP986")
nuevo3 = CeldaViva(2,3,"SCP999")

list= ListaSimple()
list.append(nuevo)
list.append(nuevo1)
list.append(nuevo2)
list.append(nuevo3)
list.imprimir()
