import atexit
from inventory import Inventory

def main():
  inventory = Inventory()

  inventory.load_products()   # Carga los datos
  atexit.register(inventory.save_products)    # Guarda los datos al salir

  while True:
    print('''
| StockMaster |
1. Add product        5. Update product
2. Show products      6. Delete product
3. Search product     7. Exit
4. Change stock
    ''')
    option = input('Select an option: ')

    if option == '1':
      id = int(input('Enter product id: '))
      name = str(input('Enter product name: '))
      price = float(input('Enter product price: '))
      stock = int(input('Enter product stock: '))
      inventory.add_product(id, name, price, stock)

    elif option == '2':
      inventory.show_products()

    elif option == '3':
      id = int(input('Enter product id: '))
      product = inventory.search_product(id)
    
    elif option == '4':
      id = int(input('Enter product id: '))
      stock = int(input('Enter the value to adjust the stock: '))
      inventory.change_stock(id, stock)

    elif option == '5':
      id = int(input('Enter product id: '))
      name = input('Enter product name: ')
      price = float(input('Enter product price: '))
      stock = int(input('Enter product stock: '))
      inventory.update_product(id, name, price, stock)

    elif option == '6':
      id = int(input('Enter product id: '))
      inventory.delete_product(id)

    elif option == '7':
      break

    else:
      print('Invalid option')

if __name__ == '__main__':
  main()

