'''
PALABRAS COMUNES
Encuentra o crea algunos textos que te gustaría analizar 
(puedes visitar Project Gutenberg (http://gutenberg.org/) 
o crear textos usando ChatGPT). Copia el texto sin formato desde tu navegador 
en un archivo de texto en tu computadora (o descarga los archivos). 
Averigua cuántasveces aparece una palabra o frase en el texto 
(puedes usar el método count()).
'''

#Abrir el texto.
with open('archivo_analizar.txt') as archivo:
    contenido = archivo.read()#Leer el texto
    busqueda = input("Introduce la letra o palabra que quieres buscar; ")
    num_veces = contenido.count(busqueda)#Contar el numero de veces 
                                           #que sale una palabra o letra.
    print(num_veces)
#La funcion .count() hace todo el trabajo.
