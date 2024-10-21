from flask import Flask, jsonify
import json

app = Flask(__name__)

# Cargar los ítems del menú desde un archivo JSON
def load_menu_items():
    with open('menu.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def home():
    return "Welcome to the API of the Menu of the Restaurant 🌮"


# Ruta para obtener todos los ítems del menú
@app.route('/menu', methods=['GET'])
def get_menu():
    menu_items = load_menu_items()
    return jsonify(menu_items), 200

# Ruta para obtener un ítem del menú por ID
@app.route('/menu/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    menu_items = load_menu_items()
    item = next((item for item in menu_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
