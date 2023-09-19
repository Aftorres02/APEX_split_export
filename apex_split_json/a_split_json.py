import json
import os

# Cambia la ubicación del archivo de entrada a dos niveles arriba y tres niveles abajo
input_path = '../readable/application/pages/p00001.json'

# Obtén el nombre del archivo JSON de entrada sin la extensión
input_filename = os.path.splitext(os.path.basename(input_path))[0]

# Crea la ruta de la carpeta de destino con el mismo nombre que el archivo JSON
carpeta_destino = os.path.join(os.path.dirname(input_path), input_filename)

# Verifica que la carpeta de destino exista o créala si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Leer el JSON desde el nuevo archivo de entrada
with open(input_path, 'r') as json_file:
    data = json.load(json_file)

# Supongamos que deseas dividir el JSON en archivos separados según el nodo 'personas'
if 'Regions' in data:
    personas_data = data['Regions']

    """ # Guardar cada conjunto de datos en un archivo separado en la carpeta de destino
    for i, persona in enumerate(personas_data):
        # Construir el nombre del archivo con la extensión ".json"
        nombre_archivo = os.path.join(carpeta_destino, f'Regions{i + 1}.json')

        # Guardar el subconjunto en el archivo
        with open(nombre_archivo, 'w') as archivo_persona:
            json.dump(persona, archivo_persona, indent=4) """

for i, persona in enumerate(personas_data):
    # Obtener el título de la persona
    titulo = persona.get('Identification', {}).get('Title', 'Desconocido')

    # Eliminar caracteres no deseados del título para usarlo como nombre de archivo
    titulo = ''.join(c for c in titulo if c.isalnum() or c.isspace())
    titulo = titulo.replace(' ', '_')  # Reemplazar espacios con guiones bajos

    # Construir el nombre del archivo con la extensión ".json"
    nombre_archivo = os.path.join(carpeta_destino, f'{titulo}_{i + 1}.json')

    # Guardar el subconjunto en el archivo
    with open(nombre_archivo, 'w') as archivo_persona:
        json.dump(persona, archivo_persona, indent=4)

print(f'Archivos guardados en la carpeta de destino: {carpeta_destino}')
