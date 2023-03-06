import os, random
from tkinter import filedialog
#from Lector import Lector
import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Muestra import Muestra
from Organismo import Organismo
from CeldaViva import CeldaViva

class Menu:

    def __init__(self) -> None:
        self.muestra=None

    #funcion para limpiar la consola
    def limpiar__consola(self):
        os.system('clear' if os.name == 'posix' else 'cls')
       

    #metodo para pausar la ejecucion
    def pausa_informacion(self):
        print('        ******** presiona una enter para continuar *****')
        ms_tp= input()

    #impresion del menu
    def print_menu(self):
        self.limpiar__consola()
        print(
                    '''
        ------------- MENU --------------
        |  1. Cargar Nuevo Archivo      |
        |  2. Ver informacion cargada   |
        |  3. Graficar                  |
        |  4. Ingresar nueva celda      |
        |  5. Salir                     |
        ---------------------------------
                    '''
                )
    
    #inicio del menu
    def inicio(self):
        while True:
            self.print_menu()
            try:
                sl = int(input('Seleccione una opcion: \n'))
                if sl == 1:
                    nombre_archivo= filedialog.askopenfilename() 
                    self.leer_archivo(nombre_archivo)
                    print('*** archivos cargados exitosamente ***')
                    self.pausa_informacion()
                    self.limpiar__consola()
                elif sl ==2:
                    self.imprimir_infoActual()
                    self.pausa_informacion()
                elif sl == 3:
                    self.graficar()
                    os.startfile("grafica.png")
                    self.pausa_informacion()
                elif sl == 4:
                    self.nueva_celula()
                    self.pausa_informacion()
                elif sl ==5:
                    print('bye')
                    break
                else:
                    print ('*** Opcion no disponible ***')
                    self.pausa_informacion()
            except:
                print('*** Por favor seleccione una opcion valida -Err: menu***')
                self.pausa_informacion()

#--------------------------------------- lectura y archivo de datos ----------------------------
#metodo para leer los archivos xml
    def leer_archivo(self, direccion:str):
        self.muestra=Muestra()
        tree = ET.parse(direccion)
        root = tree.getroot()

        #iterando cada organismo
        cont_organismo=1
        
        for organismos in root.iter('listaOrganismos'):
            #aceediendo a los datos: 
            for organismo in organismos:
                codigo = organismo.find('codigo').text
                nombre = organismo.find('nombre').text
                
                if cont_organismo<=1000:
                    letra=self.obtener_letra_aleatoria()
                    color=self.asignar_color()
                    a=Organismo(codigo,nombre,letra,color,cont_organismo)
                    self.muestra.listaOrganismos.append(a)
                    cont_organismo+=1

                else:
                    print('**** el organismo ',codigo, " - ", nombre,'se puede agregar, se ha llegado al limite de 1000 ***')


        #iterando cada muestra
        for muestras in root.iter('listadoMuestras'):
            #accediendo a los datos
            for muestra in muestras:
                codigo_muestra = muestra.find('codigo').text
                descripcion = muestra.find('descripcion').text
                fila_matriz = int(muestra.find('filas').text)
                columna_matriz = int(muestra.find('columnas').text)

                if fila_matriz<=10000:
                    if columna_matriz <=10000:
                        self.muestra.agregarDatos(codigo_muestra,descripcion,fila_matriz,columna_matriz)
                        #iterando cada celda viva
                        for celdas_vivas in muestra.iter('listadoCeldasVivas'):
                            #accediendo a los datos 
                            for celda_viva in celdas_vivas:
                                fila = celda_viva.find('fila').text
                                columna = celda_viva.find('columna').text
                                codigo_organismo = celda_viva.find('codigoOrganismo').text
                                b=CeldaViva(fila,columna,codigo_organismo)
                                self.muestra.listaCeldasVivas.append(b)
                    else:
                        print('*** La muestra: ',codigo_muestra,' no se puede agregar por que las columnas exceden los 10,000 ***')

                else:
                    print('*** La muestra: ',codigo_muestra,' no se puede agregar por que las filas exceden los 10,000 ***')

    def nueva_celula(self):
        while(True):
            if self.muestra != None:
                print('*** Ingrese numero de organismo a ingresar ***\n')
                nodo_actual = self.muestra.getListaOrganismos().cabeza
                print('0 .- Salir')
                while nodo_actual != None:
                    tcodigo=nodo_actual.valor.getCodigo()
                    tnombre=nodo_actual.valor.getNombre()
                    tid=nodo_actual.valor.getId()
                    print(tid,'.-',tcodigo, ' - ', tnombre)
                    nodo_actual = nodo_actual.nodo_siguiente
                try:
                    sl=int(input())
                    if sl !=0:
                        try:
                            posicion_x=int(input('Ingrese coordenada en X:\n'))
                            posicion_y=int(input('Ingrese coordenada en Y:\n'))
                            if (posicion_x <= self.muestra.getX()) and (posicion_y<= self.muestra.getY()):
                                tOrganismo=None
                                nodo_actual = self.muestra.getListaOrganismos().cabeza
                                while nodo_actual != None:
                                    if sl == nodo_actual.valor.getId():
                                        tOrganismo=nodo_actual.valor
                                        break
                                    nodo_actual = nodo_actual.nodo_siguiente
                                tOrganismo.imprimir()
                                ttcodigo=tOrganismo.getCodigo()
                                bandera=False
                                nodo_actual = self.muestra.getListaCeldasVivas().cabeza
                                while nodo_actual != None:
                                    if (posicion_x == int(nodo_actual.valor.getX())) and (posicion_y==int(nodo_actual.valor.getY())):
                                        bandera=True
                                    else:pass
                                    nodo_actual = nodo_actual.nodo_siguiente
                                    break
                                if bandera ==False:
                                    self.muestra.listaCeldasVivas.append(CeldaViva(posicion_x,posicion_y,ttcodigo))
                                    self.graficar()
                                    os.startfile("grafica.png")
                                    print('*** se agrego la muestra ***')
                                else:
                                    print('*** no se puede agregar por que esta corrdenada ya esta ocupada ***')
                                break
                            else:
                                print('*** coordenadas X o Y fuera de rango ***')
                                self.pausa_informacion()
                                self.limpiar__consola()
                        except:
                            print('*** coordenadas no validas')
                            self.pausa_informacion()
                            self.limpiar__consola()
                    else:
                        break
                except:
                    print('*** entrada no valida ****')
                    self.pausa_informacion()
                    self.limpiar__consola()


            else:
                print('*** No hay datos almacenados ***')
                break

#------------------ imprimir informacion almacenada ----------------------------
    def imprimir_infoActual(self):
        if self.muestra!= None:
            self.muestra.imprimir()
            tmp_org=self.muestra.getListaOrganismos()
            tmp_org.imprimir()
            tmp_cv= self.muestra.getListaCeldasVivas()
            tmp_cv.imprimir()
        else:
            print('*** No hay datos almacenados ***')

    #---------------------------- grafica-------------------------------------------   

    def graficar(self):
        if self.muestra!=None:
            arch_dot = open("imagen.dot","w")
            txt='''
digraph structs {
	    label="'''+self.muestra.getDescripcion()+'''";
    	labelloc="top";
	    node [shape=plaintext]
	    struct3 [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="50">
        /*encabezado*/     
<TR>
    '''
            filas=self.muestra.getX()
            columnas=self.muestra.getY()

            #titulo fila
            cont_y=1
            txt+='''
<TD>X/Y</TD> 
            '''
            for i in range (1,columnas+1):
                if i !=columnas:
                    txt+='''
<TD >'''+str(cont_y)+'''</TD>'''
                    cont_y+=1
                else:
                    txt+='''
<TD >'''+str(cont_y)+'''</TD>  
</TR>'''

            #titulo columna
            cont_x=1
            for j in range (1,filas+1):
                cont_y=1
                txt+='''
<TR>
<TD >'''+str(cont_x)+'''</TD>'''
                
                #datos dentro de la matriz
                for i in range (1,columnas+1):
                    if i != columnas:
                        nodo_actual = self.muestra.getListaCeldasVivas().cabeza
                        a=0
                        while nodo_actual != None:
                            tcodigo=nodo_actual.valor.getCodigo()
                            tempX=int(nodo_actual.valor.getX())
                            tempY=int(nodo_actual.valor.getY())
                            tcolor=self.obtenerColor(tcodigo)
                            if  tempX==j and tempY==i:                                
                                txt+='''<TD bgcolor="'''+tcolor+'''">'''+tcodigo+'''</TD>\n'''
                                a=i
                                a+=1
                                break
                            else:a=i
                            nodo_actual = nodo_actual.nodo_siguiente
                        if a==i:
                            txt+='''<TD></TD>\n'''
                        else:pass
                        cont_y+=1
                    else:
                        nodo_actual = self.muestra.getListaCeldasVivas().cabeza
                        a=0
                        while nodo_actual != None:
                            tcodigo=nodo_actual.valor.getCodigo()
                            tempX=int(nodo_actual.valor.getX())
                            tempY=int(nodo_actual.valor.getY())
                            tcolor=self.obtenerColor(tcodigo)
                            if  tempX==j and tempY==i:
                                txt+='''<TD bgcolor="'''+tcolor+'''">'''+tcodigo+'''</TD> 
</TR>'''                              
                                a=i
                                a+=1
                                break
                            else:a=i
                            nodo_actual = nodo_actual.nodo_siguiente
                        if a==i:
                            txt+='''<TD></TD> 
</TR>'''
                        else:pass

                cont_x+=1
                
            
            txt+='''
</TABLE>>
]
}           
            '''   
            arch_dot.write(txt)
            arch_dot.close()
            
            os.system("dot.exe -Tpng imagen.dot -o grafica.png")
        else:
            print('----- No se puede graficar, No hay elementos registrados Err: graficar-----')

    
    def obtenerLetra(self,codigo):
        try:
            nodo_actual = self.muestra.getListaOrganismos().cabeza
            respuesta=None
            while nodo_actual != None:
                if codigo==nodo_actual.valor.getCodigo():
                    respuesta=nodo_actual.valor.getLetra()
                    break
                else: pass
                nodo_actual = nodo_actual.nodo_siguiente
            return respuesta
        except:
            print('error al obtener la letra')
        
    def obtenerColor(self,codigo):
        try:
            nodo_actual = self.muestra.getListaOrganismos().cabeza
            respuesta=None
            while nodo_actual != None:
                if codigo==nodo_actual.valor.getCodigo():
                    respuesta=nodo_actual.valor.getColor()
                    break
                else: pass
                nodo_actual = nodo_actual.nodo_siguiente
            return respuesta
        except:
            print('error al obtener el color')
    
    def obtener_letra_aleatoria(self):
    #Devuelve una letra aleatoria en mayúscula
        letra = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return letra
    
    def asignar_color(self):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        return color
    
    def aaa(self):
        nodo_actual = self.muestra.getListaCeldasVivas().cabeza
        while nodo_actual != None:
            tcodigo=nodo_actual.valor.getCodigo()
            tempX=int(nodo_actual.valor.getX())
            tempY=int(nodo_actual.valor.getY())
            tcolor=self.obtenerColor(tcodigo)
            if j==tempX and i==tempY:
                txt+='''<TD bgcolor="'''+tcolor+'''"></TD>\n'''
            else:pass
            nodo_actual = nodo_actual.nodo_siguiente
