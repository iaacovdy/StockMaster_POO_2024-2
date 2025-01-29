import json

# Clase Producto
class Product():
  # Constructor
  def __init__(self, id: int, name: str, price: float, stock:int) -> None:
    self.id = id
    self.name = name
    self.price = price
    self.stock = stock

  # Producto-str
  def __str__(self):
    return f'Id: {self.id}  -  Name: {self.name}  -  Price: {self.price}  -  Stock: {self.stock}'

# Clase Inventario
class Inventory():
  # Constructor
  def __init__(self):
    self.products = {}    # Diccionario de productos

  # Agrega productos al inventario
  def add_product(self, id, name, price, stock):
    if id in self.products:   # Verifica si el producto ya existe
      print('Product already exists')
      return False
    else:
      self.products[id] = Product(id, name, price, stock)
      print('Product added successfully')

  # Muestra los productos del inventario
  def show_products(self):
    print('Products in inventory')
    for product in self.products.values():
      print(product)


  def search_product(self, id):
    if id in self.products:   # Verifica si el producto existe
      print(self.products.get(id))
  
    else:
      print('Product not found')
      return None
  
  def change_stock(self, id, change_stock):
    product = self.search_product(id)
    if product:
      self.products.get(id).stock += change_stock
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
      print('Product updated successfully')
      return True
    return False
    
  # Elimina un producto del inventario
  def delete_product(self, id):
    product = self.search_product(id, 'Not found')
    if product:
      self.products.pop(id)
      print('Product deleted successfully')
      return True
    return False

  def save_products(self):
    with open('products.json', 'w') as file:
        json.dump(
            {str(id): product.__dict__ for id, product in self.products.items()}, 
            file, 
            indent=4
        )
    print('Products saved successfully.')


  def load_products(self):
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)  # Carga el JSON como un diccionario
            self.products = {int(id): Product(**product) for id, product in data.items()}
        print('Products loaded successfully.')
    except FileNotFoundError:
        self.products = {}
        print('No saved products found.')
    except json.JSONDecodeError:
        print('Error: The JSON file is corrupted or incorrectly formatted.')



# #Prueba
# inventory1 = Inventory()    # Crea un inventario 
# producto1 = Product(id=1, name='Laptop', price=1000, stock=10)  # Crea un producto
# producto2 = Product(id=2, name='Mouse', price=50, stock=20)  

# inventory1.add_product(producto1)    # Agrega productos al inventario 
# inventory1.add_product(producto2)
# inventory1.show_products()    # Muestra los productos del inventario

# searched_product = inventory1.search_product(1)   # Busca un producto
# searched_product = inventory1.search_product(3)   # Busca un producto que no existe

# inventory1.change_stock(1, 5)    # Cambia el stock de un producto

# inventory1.update_product(1, 'Laptop HP', 1200, 5)   # Actualiza un producto
# inventory1.show_products()    # Muestra los productos del inventario

# inventory1.delete_product(1)    # Elimina un producto
# inventory1.show_products()    # Muestra los productos del inventario
