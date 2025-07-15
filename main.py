
class Category:
    """Класс хранит названия категорий и список товаров категории"""
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Product:
    """Класс хранит информацию по товарам магазина"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name,description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
