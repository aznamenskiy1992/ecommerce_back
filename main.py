
class Category:
    """Класс хранит названия категорий и список товаров категории"""
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
