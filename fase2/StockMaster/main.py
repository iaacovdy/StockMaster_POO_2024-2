from inventory import Inventory
from Product import Product
from User import User


def main():
    User.load_users('usuarios.json')
    inventario = Inventory()

    while True:
        
        print('Welcome to StockMaster')
        print ("Please login")

        account = input('Name: ')
        password = input('Password: ')
        role = input('Role: ')
        access = User.login(account,password,role)
        if access == False:
            pass
        else:
            print ('Welcome to our sistem.')
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

                case '2':
                    inventario.show_products()

                case '3':
                    id = int(input('Enter product id: '))
                    product = inventario.search_product(id)
        
                case '4':
                    id = int(input('Enter product id: '))
                    stock = int(input('Enter the value to adjust the stock: '))
                    inventario.change_stock(id, stock)

                case '5':
                    id = int(input('Enter product id: '))
                    name = input('Enter product name: ')
                    price = float(input('Enter product price: '))
                    stock = int(input('Enter product stock: '))
                    inventario.update_product(id, name, price, stock)

                case '6':
                    id = int(input('Enter product id: '))
                    inventario.delete_product(id)

                case '7':
                    print("Exiting the program...")
                    break


if __name__ == '__main__':
    main()