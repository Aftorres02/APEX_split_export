import json
import os

input_path = '../readable/application/pages/p00001.json'

# Lee el contenido del archivo 'pagina_1.json'
with open(input_path, 'r') as json_file:
    data = json.load(json_file)

# Crea una carpeta con el mismo nombre que el archivo sin la extensión
folder_name = os.path.splitext('pagina_1.json')[0]
os.makedirs(folder_name, exist_ok=True)

# Procesa el nodo 'Regions'
if 'Regions' in data:
    regions_data = data['Regions']
    for region in regions_data:
        # Obtiene el nombre del archivo del atributo 'Identification.Title'
        file_name = os.path.join(folder_name, f"{region['Identification']['Title']}.json")
        # Guarda el subconjunto en el archivo correspondiente
        with open(file_name, 'w') as region_file:
            json.dump(region, region_file, indent=4)

# Procesa el nodo 'Page Items'
if 'Page Items' in data:
    page_items_data = data['Page Items']
    for page_item in page_items_data:
        # Obtiene el nombre del archivo del atributo 'Identification.Name'
        file_name = os.path.join(folder_name, f"{page_item['Identification']['Name']}.json")
        # Guarda el subconjunto en el archivo correspondiente
        with open(file_name, 'w') as page_item_file:
            json.dump(page_item, page_item_file, indent=4)

# Procesa el nodo 'Buttons'
if 'Buttons' in data:
    buttons_data = data['Buttons']
    for button in buttons_data:
        # Obtiene el nombre del archivo del atributo 'Identification.Button Name'
        file_name = os.path.join(folder_name, f"{button['Identification']['Button Name']}.json")
        # Guarda el subconjunto en el archivo correspondiente
        with open(file_name, 'w') as button_file:
            json.dump(button, button_file, indent=4)

print('Archivos JSON generados en la carpeta', folder_name)
