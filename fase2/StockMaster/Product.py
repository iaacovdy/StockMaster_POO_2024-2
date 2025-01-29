class Product():
    # Constructor
    def __init__(self, id: int, name: str, price: float, stock: int) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    # Producto-str
    def __str__(self):
        return (
        f'Id: {self.id}\n'
        f'    Name: {self.name}\n'
        f'    Price: ${self.price}\n'
        f'    Stock: {self.stock}')
    
    def product_to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }
    
