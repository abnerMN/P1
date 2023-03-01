import xml.etree.ElementTree as ET

# Abrir el archivo
tree = ET.parse('prueba.xml')

# Obtener la raíz del archivo
root = tree.getroot()

# Acceder a los elementos del archivo
for organismos in root.iter('listaOrganismos'):
    for organismo in organismos:
        codigo = organismo.find('codigo').text
        nombre = organismo.find('nombre').text
        print("codigo: ",codigo, "nombre: ", nombre)

for muestras in root.iter('listadoMuestras'):
    for muestra in muestras:
        codigo_muestra = muestra.find('codigo').text
        descripcion = muestra.find('descripcion').text
        print('codigo muestra: ',codigo_muestra, 'descripcion: ',descripcion)
        
        for celdas_vivas in muestra.iter('listadoCeldasVivas'):
            for celda_viva in celdas_vivas:
                fila = celda_viva.find('fila').text
                columna = celda_viva.find('columna').text
                codigo_organismo = celda_viva.find('codigoOrganismo').text
                print('fila: ',fila, 'columna: ',columna, 'codigo organismo:',codigo_organismo)