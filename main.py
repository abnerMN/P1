#metodo para pausar la ejecucion del programa
def pausa_informacion():
    print('        ******** presiona una tecla para continuar *****')
    ms_tp= input()

#menu principal
def menu():
    sl= 0
    while (sl !=4):
        print(
            '''

------------- MENU --------------
|       1. Cargar Archivo       |
|       2. gestionar            |
|       3. graficar             |
|       4. salir                |
---------------------------------
            '''
        )
        try:
            sl = int(input('seleccione una opcion: \n'))
            if sl == 1:
                pass

            elif sl ==2:
                pass
            elif sl == 3:
                pass
            elif sl == 4:
                print('bye')
                sl=4
            else:
                print ('*** Opcion no disponible ***')
                pausa_informacion()
        except:
            print('*** Por favor seleccione una opcion valida -Err: menu***')     


#main
if __name__== "__main__":
    menu()
             