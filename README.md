## Detección de Bloques de Texto Duplicados
Este script de Python se diseñó para encontrar bloques de texto duplicados dentro de un archivo dado. Los bloques se definen como secuencias consecutivas de palabras, y el programa busca coincidencias exactas.
## Requisitos
Python 3.x
## Uso
Opciones
--num_pal: Número de palabras por bloque (por defecto: 40)
--archivo: Ruta al archivo de entrada (obligatorio)
##Ejemplo de Ejecución
bash
Copy code
python script.py --num_pal 40 --archivo ejemplo.txt
## Descripción
Argumentos de Línea de Comandos

El script utiliza el módulo argparse para manejar los argumentos de línea de comandos. Se pueden especificar la cantidad de palabras por bloque (--num_pal) y la ruta al archivo de entrada (--archivo).

La función encontrar_duplicados toma un bloque de texto y devuelve una lista de bloques duplicados. Utiliza conjuntos para realizar un seguimiento de bloques únicos y una lista para almacenar bloques duplicados.

## Procesamiento del Archivo
El script lee el contenido del archivo especificado y llama a la función encontrar_duplicados para identificar bloques duplicados.

## Impresión de Bloques Duplicados

Los bloques duplicados se imprimen en la consola. Se realiza un pequeño proceso adicional para imprimir cada bloque duplicado solo una vez.


## Notas
Asegúrate de tener permisos de lectura para el archivo especificado.
Ajusta el número de palabras por bloque según sea necesario para adaptarse a tus requisitos específicos.
