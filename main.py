from inventory import Inventory
from Product import Product
from user import User
from records import Record

from getpass import getpass     # Oculta la contraseña

# Función para obtener las credenciales del usuario
def get_user_credentials():
    print("\nPlease login")
    account = input('  Name: ')
    password = getpass('  Password: ')  # Oculta la contraseña
    role = input('  Role: ')
    
    return account, password, role

def main():
    User.load_users('data/usuarios.json')   # Carga los usuarios
    Record.initialize_json_file('records.json')    # Crea un archivo JSON vacío
    inventario = Inventory()    # Instancia de la clase Inventory

    # Bucle para el inicio de sesión
    while True:
        print('\nWelcome to StockMaster')
        account, password, role = get_user_credentials()    # Obtiene las credenciales del usuario
        
        if User.login(account, password, role):     # Verifica las credenciales del usuario
            break
   
   # Bucle para el menú de opciones
    while True:
        print('\nMenu:')   
        print('1. Add product')
        print('2. Show products')
        print('3. Search product')
        print('4. Change stock')
        print('5. Update product')
        print('6. Delete product')
        print('7. Exit')
        option = input('  Select an option: ')  # Opción seleccionada por el usuario

        match option: 
            case '1':   # Agregar producto
                id = int(input('Enter product id: '))
                name = str(input('Enter product name: '))
                price = float(input('Enter product price: '))
                stock = int(input('Enter product stock: '))
                product = Product(id, name, price, stock)
                inventario.add_product(product)
                Record.add_record_to_json(id, stock, 'addedfel', json_file='records.json')

            case '2':  # Mostrar productos
                inventario.show_products()

            case '3':   # Buscar producto
                id = int(input('Enter product id: '))
                inventario.search_product(id)

            case '4':   # Cambiar stock
                id = int(input('Enter product id: '))
                stock = int(input('Enter the value to adjust the stock: '))
                inventario.change_stock(id, stock)
                Record.add_record_to_json(id, stock, 'Stock Changed', json_file='records.json')

            case '5':   # Actualizar producto
                id = int(input('Enter product id: '))
                name = input('Enter product name: ')
                price = float(input('Enter product price: '))
                stock = int(input('Enter product stock: '))
                inventario.update_product(id, name, price, stock)
                Record.add_record_to_json(id, stock, 'updated', json_file='records.json')

            case '6':   # Eliminar producto
                id = int(input('Enter product id: '))
                inventario.delete_product(id)
                Record.add_record_to_json(id, stock, 'removed', json_file='records.json')

            case '7':   # Salir del programa
                print("Exiting the program...")
                break

            case _:     # Opción inválida
                print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()
