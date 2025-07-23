class Product:
    """Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (property): Свойство для работы с ценой товара (с проверкой валидности)
        quantity (int): Количество товара в наличии

    Методы:
        new_product: Создает новый товар из словаря с данными (классовый метод)
    """

    name: str
    description: str
    __price: float  # Приватный атрибут для хранения цены
    quantity: int

    @classmethod
    def new_product(cls, product: dict):
        """Фабричный метод для создания нового товара из словаря.

        Args:
            product (dict): Словарь с данными о товаре, должен содержать ключи:
                - name: название товара
                - description: описание товара
                - price: цена товара
                - quantity: количество товара

        Returns:
            Product: Созданный экземпляр класса Product

        Примечание:
            Используется для удобного создания товаров из данных,
            например, при загрузке из JSON или базы данных
        """
        return cls(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"],
        )

    def __init__(self, name, description, price, quantity):
        """Инициализирует экземпляр класса Product.

        Args:
            name (str): Название товара
            description (str): Описание товара
            price (float): Цена товара (должна быть положительной)
            quantity (int): Количество товара в наличии

        Примечание:
            Цена хранится в приватном атрибуте __price для контроля валидности
        """
        self.name = name
        self.description = description
        self.__price = price  # Устанавливаем через приватный атрибут
        self.quantity = quantity

    def __str__(self):
        """Выводит информацию о товаре"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Выводит сумму по стоимости 2-х товаров"""
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self):
        """Геттер для получения цены товара.

        Returns:
            float: Текущая цена товара
        """
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для изменения цены с проверкой валидности.

        Args:
            new_price (float): Новая цена товара

        Примечание:
            Если новая цена меньше или равна 0, изменение не происходит
            и выводится предупреждение
        """
        if new_price <= 0:
            # Защита от некорректного значения цены
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
