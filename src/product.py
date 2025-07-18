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

    @classmethod
    def new_product(cls, product: dict):
        """Возвращает созданный товар"""
        return cls(
            name=product['name'],
            description = product['description'],
            price = product['price'],
            quantity = product['quantity']
        )


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


    @price.setter
    def price(self, new_price: float):
        """Изменяет цену товара"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
