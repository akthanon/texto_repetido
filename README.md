##Detección de Bloques de Texto Duplicados
Este script de Python se diseñó para encontrar bloques de texto duplicados dentro de un archivo dado. Los bloques se definen como secuencias consecutivas de palabras, y el programa busca coincidencias exactas.

##Requisitos
Python 3.x
##Uso
Opciones
--num_pal: Número de palabras por bloque (por defecto: 40)
--archivo: Ruta al archivo de entrada (obligatorio)
##Ejemplo de Ejecución
bash
Copy code
python script.py --num_pal 40 --archivo ejemplo.txt
##Descripción
Argumentos de Línea de Comandos

El script utiliza el módulo argparse para manejar los argumentos de línea de comandos. Se pueden especificar la cantidad de palabras por bloque (--num_pal) y la ruta al archivo de entrada (--archivo).

python
Copy code
import argparse

parser = argparse.ArgumentParser(description='Encuentra bloques de texto duplicados en un archivo.')
parser.add_argument('--num_pal', type=int, default=40, help='Número de palabras por bloque')
parser.add_argument('--archivo', type=str, required=True, help='Ruta al archivo de entrada')
args = parser.parse_args()
Función encontrar_duplicados

La función encontrar_duplicados toma un bloque de texto y devuelve una lista de bloques duplicados. Utiliza conjuntos para realizar un seguimiento de bloques únicos y una lista para almacenar bloques duplicados.

python
Copy code
def encontrar_duplicados(texto):
    # ... (ver código para detalles)
    return bloques_duplicados
Procesamiento del Archivo

El script lee el contenido del archivo especificado y llama a la función encontrar_duplicados para identificar bloques duplicados.

python
Copy code
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

duplicados = encontrar_duplicados(contenido)
##Impresión de Bloques Duplicados

Los bloques duplicados se imprimen en la consola. Se realiza un pequeño proceso adicional para imprimir cada bloque duplicado solo una vez.

python
Copy code
dupliant=""
maxdup=0
numdup=1
nummax=len(duplicados)
for i, duplicado in enumerate(duplicados, 1):
    dusplit=duplicado.split(" ")
    if dupliant[1:]!=dusplit[:-1]:
        print(f'{numdup}: {duplicado}')
        maxdup=0
        numdup=numdup+1
    if maxdup<num_pal-1:
        maxdup=maxdup+1
        dupliant=duplicado.split(" ")
Notas
Asegúrate de tener permisos de lectura para el archivo especificado.
Ajusta el número de palabras por bloque según sea necesario para adaptarse a tus requisitos específicos.
