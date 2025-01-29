from inventory import Inventory
from Product import Product
from User import User
from records import Record


def main():
    control = True
    while control ==True:
        User.load_users('usuarios.json')
        inventario = Inventory()
        Record.create_empty_json('records.json')

        print('\nWelcome to StockMaster')
        print("\nPlease login")

        account = input('Name: ')
        password = input('Password: ')
        role = input('Role: ')
        
        if not User.login(account, password, role):
            control = True
        else:
            control = False

    print("\nWelcome to our system.")
   
    while control ==False:
        print('\nMenu:')
        print('1. Add product')
        print('2. Show products')
        print('3. Search product')
        print('4. Change stock')
        print('5. Update product')
        print('6. Delete product')
        print('7. Exit')

        option = input('Select an option: ')

        match option: 
            case '1':
                id = int(input('Enter product id: '))
                name = str(input('Enter product name: '))
                price = float(input('Enter product price: '))
                stock = int(input('Enter product stock: '))
                product = Product(id, name, price, stock)
                inventario.add_product(product)
                Record.add_record_to_json(id, stock, 'addedfel', json_file='records.json')

            case '2':
                inventario.show_products()

            case '3':
                id = int(input('Enter product id: '))
                inventario.search_product(id)

            case '4':
                id = int(input('Enter product id: '))
                stock = int(input('Enter the value to adjust the stock: '))
                inventario.change_stock(id, stock)
                Record.add_record_to_json(id, stock, 'Stock Changed', json_file='records.json')

            case '5':
                id = int(input('Enter product id: '))
                name = input('Enter product name: ')
                price = float(input('Enter product price: '))
                stock = int(input('Enter product stock: '))
                inventario.update_product(id, name, price, stock)
                Record.add_record_to_json(id, stock, 'updated', json_file='records.json')

            case '6':
                id = int(input('Enter product id: '))
                inventario.delete_product(id)
                Record.add_record_to_json(id, stock, 'removed', json_file='records.json')
            case '7':
                print("Exiting the program...")
                control = True
                break

            case _:
                print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()
