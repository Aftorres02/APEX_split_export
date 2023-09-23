import json
import os

# Función para crear carpetas y archivos
def create_folders_and_files(input_path):

  # Leer el JSON desde el archivo de entrada
  with open(input_path, 'r') as json_file:
      all_json_data = json.load(json_file)

  # Obtener la ubicación del directorio del archivo JSON
  input_dir = os.path.dirname(input_path)
  #print(input_dir)
  # Nombre de la carpeta raíz (usando el nombre del archivo JSON sin extensión)
  root_folder = os.path.splitext(os.path.basename(input_path))[0]

  # Ruta de la carpeta raíz en el mismo nivel que el archivo JSON de entrada
  base_folder = os.path.join(input_dir, root_folder)
  print(base_folder)

  if not os.path.exists(base_folder):
      os.makedirs(base_folder)

  # Subdividir los datos según los nodos 'Regions', 'Page Items' y 'Buttons'
  for node in ['Regions', 'Page Items', 'Buttons', 'Validations', 'Processes','Branches']:
    
    # Verificar si el nodo está presente y tiene datos
    if node in all_json_data and all_json_data[node]:
      node_data = all_json_data[node]

      # Crear una carpeta para el nodo si no existe
      node_folder = os.path.join(base_folder, node)
      
      if not os.path.exists(node_folder):
        os.makedirs(node_folder)
  
      if node in all_json_data:
        node_data = all_json_data[node]
        #print(node)
   
        # Recorrer los datos y crear archivos para cada sub objeto
        for i, item in enumerate(node_data):
        
          # Obtener el nombre del archivo desde los datos del nodo
          if 'Title' in item['Identification']:
            item_name = item['Identification']['Title']
          elif 'Name' in item['Identification']:
            item_name = item['Identification']['Name']
          elif 'Button Name' in item['Identification']:
            item_name = item['Identification']['Button Name']
          else:
            item_name = f'item_{i + 1}'
  
          item_name_valid = item_name.replace('/', '_')
  
          # Construir la ruta del archivo para este sub objeto
          item_file_path = os.path.join(node_folder, f'{item_name_valid}.json')
          
          # Escribir los datos del sub objeto en el archivo correspondiente
          with open(item_file_path, 'w') as item_file:
              json.dump(item, item_file, indent=4)
  
  # Guardar los nodos que no están en la lista en un archivo separado

  other_nodes = {key: value for key, value in all_json_data.items() if key not in ['Regions', 'Page Items', 'Buttons', 'Validations', 'Processes', 'Branches']}
  page_json_name = root_folder + '.json'
  other_file_path = os.path.join(base_folder, page_json_name)
  with open(other_file_path, 'w') as other_file:
      json.dump(other_nodes, other_file, indent=4)

#C:\MyPc\1_Git\APEX_split_export\f192\readable\application\pages\p00020.json

""" # Ruta del archivo JSON de entrada
input_path = '../f192/readable/application/pages/p00020.json'

# Llamar a la función para crear carpetas y archivos
create_folders_and_files(input_path)

print(f'Carpetas y archivos creados en: {input_path}')
 """

# Ruta del directorio que contiene los archivos JSON a procesar
input_dir = '../f192/readable/application/pages'

# Obtener la lista de archivos JSON en el directorio
json_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]

contador = 0
# Procesar cada archivo JSON en el directorio
for json_file in json_files:
  contador = contador + 1
  #print (json_file)
  if contador <= 10:
    json_file_path = os.path.join(input_dir, json_file)
    # Llamar a la función para crear carpetas y archivos
    create_folders_and_files(json_file_path)