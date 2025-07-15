
class Category:
    """Класс хранит названия категорий и список товаров категории"""
    products_cnt: int = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.products_cnt += len(self.products)


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
