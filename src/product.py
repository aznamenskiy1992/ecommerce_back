from abc import ABC, abstractmethod

from src.mixin import MixinLog


class BaseProduct(ABC):
    """Абстрактный базовый класс, определяющий интерфейс для всех товаров.

    Задает обязательные методы, которые должны быть реализованы в дочерних классах.
    Использует абстрактные методы для обеспечения единого интерфейса товаров.

    Обязательные методы:
        __init__: Инициализация товара
        __str__: Строковое представление
        __add__: Сложение товаров
        new_product: Альтернативный конструктор

    Пример использования:
        class ConcreteProduct(BaseProduct):
            ...  # реализация всех абстрактных методов
    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """Абстрактный метод инициализации товара.

        Args:
            *args: Позиционные аргументы
            **kwargs: Именованные аргументы

        Примечание:
            Должен быть реализован в дочерних классах
        """
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод строкового представления товара.

        Returns:
            str: Информация о товаре в читаемом формате

        Примечание:
            Реализация должна возвращать строку с основными характеристиками
        """
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения товаров.

        Args:
            other: Другой товар для сложения

        Returns:
            Числовой результат сложения стоимостей

        Примечание:
            Реализация должна учитывать типы товаров при сложении
        """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        """Абстрактный фабричный метод создания товара.

        Args:
            product_data: Данные для создания товара (обычно dict)

        Returns:
            Экземпляр класса товара

        Примечание:
            Альтернативный конструктор для создания из словаря данных
        """
        pass


class Product(MixinLog, BaseProduct):
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
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price  # Устанавливаем через приватный атрибут
        self.quantity = quantity
        super().__init__()

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
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity

        raise TypeError("Складывать можно только товары одного класса")

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
    """Класс для представления смартфонов в магазине.

    Наследует базовый функционал класса Product и добавляет специфичные для смартфонов атрибуты.

    Атрибуты:
        efficiency (float): Производительность (например, в GHz)
        model (str): Модель смартфона
        memory (int): Объем памяти в GB
        color (str): Цвет устройства
        Все атрибуты родительского класса Product

    Методы:
        __init__: Инициализирует экземпляр смартфона
        __add__: Складывает стоимость товаров с проверкой типа
    """

    efficiency: float  # Производительность процессора
    model: str  # Модельный номер устройства
    memory: int  # Объем памяти в гигабайтах
    color: str  # Цвет корпуса

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализирует новый экземпляр смартфона.

        Args:
            name (str): Название модели
            description (str): Описание характеристик
            price (float): Цена в рублях
            quantity (int): Количество на складе
            efficiency (float): Производительность процессора
            model (str): Модельный номер
            memory (int): Объем памяти (GB)
            color (str): Цвет устройства

        Примечание:
            Первые 4 параметра передаются в родительский класс Product
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # Устанавливаем специфичные для смартфона параметры
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы в магазине.

    Наследует базовый функционал класса Product и добавляет специфичные атрибуты
    для газонной травы.

    Атрибуты:
        country (str): Страна-производитель травы
        germination_period (str): Период прорастания (например, '2-3 недели')
        color (str): Цвет травы (например, 'ярко-зеленый')
        Все атрибуты родительского класса Product

    Методы:
        __init__: Инициализирует экземпляр газонной травы
        __add__: Складывает стоимость товаров с проверкой типа
    """

    country: str  # Страна происхождения травосмеси
    germination_period: str  # Срок прорастания в днях/неделях
    color: str  # Оттенок зелени

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализирует новый экземпляр газонной травы.

        Args:
            name (str): Название травосмеси
            description (str): Описание состава и характеристик
            price (float): Цена за упаковку в рублях
            quantity (int): Количество упаковок на складе
            country (str): Страна производства (например, 'Германия')
            germination_period (str): Срок прорастания (например, '14-21 день')
            color (str): Цвет травы (например, 'изумрудный')

        Примечание:
            Первые 4 параметра передаются в родительский класс Product
        """
        super().__init__(name, description, price, quantity)
        self.country = country  # Устанавливаем страну-производителя
        self.germination_period = germination_period  # Срок до первых всходов
        self.color = color  # Цвет травяного покрова
