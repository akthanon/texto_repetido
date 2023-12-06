import sys

# Verificar si hay argumentos en la línea de comandos
if len(sys.argv) > 1:
    # Si hay argumentos, intentar convertir el primer argumento a un número
    try:
        num_pal = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un número. Se utilizará el valor por defecto (40).")
        num_pal = 40
else:
    # Si no hay argumentos, establecer el valor por defecto (40)
    num_pal = 40

def encontrar_duplicados(texto):
    # Dividir el texto en bloques de 6 palabras
    palabras = texto.split()
    bloques = [palabras[i:i+num_pal] for i in range(len(palabras)-num_pal-1)]

    # Conjunto para almacenar bloques de texto únicos
    bloques_unicos = set()

    # Lista para almacenar bloques duplicados
    bloques_duplicados = []

    for bloque in bloques:
        bloque_str = ' '.join(bloque)

        # Verificar si el bloque ya ha sido encontrado
        if bloque_str not in bloques_unicos:
            # Agregar a bloques únicos
            bloques_unicos.add(bloque_str)
        else:
            # Agregar a bloques duplicados si es la primera vez que se encuentra
            if bloque_str not in bloques_duplicados:
                bloques_duplicados.append(bloque_str)
                # Remover el bloque duplicado de bloques únicos
                bloques_unicos.remove(bloque_str)

    return bloques_duplicados

# Leer el contenido del archivo
with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Encontrar duplicados en el texto
duplicados = encontrar_duplicados(contenido)

# Imprimir los bloques de texto duplicados
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
    
