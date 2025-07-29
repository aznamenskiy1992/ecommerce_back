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
        """Возвращает строковое представление товара.

        Returns:
            str: Строка в формате "Название, цена руб. Остаток: кол-во шт."
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает стоимость товаров (цена * количество).

        Args:
            other (Product): Другой товар для сложения

        Returns:
            float: Общая стоимость товаров

        Исключения:
            TypeError: Если other не является Product
        """
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Можно суммировать только объекты класса Product или его наследников")

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


class Smartphone(Product):
    """ Класс для товара Смартфоны """
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """ Инициализирует подкласс Smartphone """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ Складывает стоимость товаров (цена * количество) """
        if type(other) == self.__class__:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError('Складывать можно только товары одного класса')


class LawnGrass(Product):
    """ Класс для товара Трава газонная """
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """ Инициализирует подкласс LawnGrass """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ Складывает стоимость товаров (цена * количество) """
        if type(other) == self.__class__:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError('Складывать можно только товары одного класса')
