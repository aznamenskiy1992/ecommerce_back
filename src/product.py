class Product:
    """Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара в наличии
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует экземпляр класса Product.

        Args:
            name (str): Название товара
            description (str): Описание товара
            price (int): Цена товара
            quantity (int): Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        """Возвращает цену товара"""
        return self.__price
