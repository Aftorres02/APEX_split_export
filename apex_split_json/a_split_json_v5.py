import json
import os
import shutil
import argparse

# Función para borrar carpetas creadas por el código anterior
def delete_existing_folders(input_path):
    root_folder = os.path.splitext(os.path.basename(input_path))[0]
    base_folder = os.path.join(os.path.dirname(input_path), root_folder)

    if os.path.exists(base_folder):
        shutil.rmtree(base_folder)


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
  for node in ['Regions', 'Page Items', 'Buttons', 'Validations', 'Processes','Branches','Dynamic Actions']:
    
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

  other_nodes = {key: value for key, value in all_json_data.items() if key not in ['Regions', 'Page Items', 'Buttons', 'Validations', 'Processes', 'Branches','Dynamic Actions']}
  page_json_name = root_folder + '.json'
  other_file_path = os.path.join(base_folder, page_json_name)
  with open(other_file_path, 'w') as other_file:
      json.dump(other_nodes, other_file, indent=4)

def main(number):
    # Configura la ruta del directorio basada en el número proporcionado
    input_dir = f'../f{number}/readable/application/pages'
    print(input_dir)
    # Obtener la lista de archivos JSON en el directorio
    json_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]

    # Eliminar todas las carpetas creadas por el código anterior
    for json_file in json_files:
        delete_existing_folders(os.path.join(input_dir, json_file))

    contador = 0
    # Procesar cada archivo JSON en el directorio
    for json_file in json_files:
      contador = contador + 1

      if contador <= 100:
        json_file_path = os.path.join(input_dir, json_file)
        # Llamar a la función para crear carpetas y archivos
        create_folders_and_files(json_file_path)

if __name__ == "__main__":
    # Configura el argumento de línea de comandos para el número
    parser = argparse.ArgumentParser(description='Procesar archivos JSON basados en un número.')
    parser.add_argument('number', type=int, help='Número que se utilizará en la ruta del directorio.')


    # Parsea los argumentos
    args = parser.parse_args()
    print(args)
    main(args.number)