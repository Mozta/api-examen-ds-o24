from flask import Flask, jsonify

app = Flask(__name__)

# Definir los ítems del menú como una lista de diccionarios
menu_items = [
    {"id": 1, "name": "Pizza Margherita", "price": 8.99, "description": "Classic pizza with tomatoes, mozzarella, and basil"},
    {"id": 2, "name": "Caesar Salad", "price": 5.99, "description": "Crisp romaine lettuce with Caesar dressing and croutons"},
    {"id": 3, "name": "Spaghetti Carbonara", "price": 12.50, "description": "Traditional pasta with bacon, eggs, and Parmesan"},
    {"id": 4, "name": "Tiramisu", "price": 6.75, "description": "Classic Italian dessert with mascarpone cheese and espresso"},
]

# Ruta para obtener todos los ítems del menú
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items), 200

# Ruta para obtener un ítem del menú por ID
@app.route('/menu/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    item = next((item for item in menu_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
