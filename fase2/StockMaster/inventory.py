from Product import Product
import json

class Inventory():
    # Constructor
    def __init__(self, json_file='inventario.json'):
        self.products = {}  # Diccionario de productos
        self.json_file = json_file
        self.load_inventory()

    # Cargar inventario desde JSON
    def load_inventory(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                for item in data['Productos']:
                    product = Product(**item)
                    self.products[product.id] = product
        except FileNotFoundError:
            print("El archivo JSON no se encontró, iniciando con un inventario vacío.")

            
    # Guardar inventario a JSON
    def save_inventory(self):
        with open(self.json_file, 'w') as file:
            data = {'Productos': [product.product_to_dict() for product in self.products.values()]}
            json.dump(data, file, indent=4)

    # Agrega productos al inventario
    def add_product(self, product):
        if product.id in self.products:   # Verifica si el producto ya existe
            print('Product already exists')
            return False
        else:
            self.products[product.id] = product
            self.save_inventory()
            print('Product added successfully')

    # Muestra los productos del inventario
    def show_products(self):
        print('Products in inventory')
        for product in self.products.values():
            print(product)
            print ()

    def search_product(self, id):
        if id in self.products:  # Verifica si el producto existe
            print(self.products.get(id))
            return self.products.get(id)
        else:
            print('Product not found')
            return False
    
    def change_stock(self, id, change_stock):
        product = self.search_product(id)
        if product:
            product.stock = change_stock
            self.save_inventory()
            print('Stock updated successfully')
            return True
        return False

    # Actualiza un producto del inventario
    def update_product(self, id, name, price, stock):
        product = self.search_product(id)
        if product:
            product.name = name
            product.price = price
            product.stock = stock
            self.save_inventory()
            print('Product updated successfully')
            return True
        return False
    
    # Elimina un producto del inventario
    def delete_product(self, id):
        product = self.search_product(id)
        if product:
            self.products.pop(id)
            self.save_inventory()
            print('Product deleted successfully')
            return True
        return False
