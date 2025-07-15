class Category:
    """Класс для представления категории товаров в магазине.

    Атрибуты:
        product_count (int): Общее количество товаров во всех категориях (статический)
        category_count (int): Общее количество категорий (статический)
        name (str): Название категории
        description (str): Описание категории
        products (list): Список товаров в данной категории

    Методы:
        __init__: Инициализирует категорию и обновляет счетчики
    """

    product_count: int = 0
    category_count: int = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Инициализирует экземпляр класса Category.

        Args:
            name (str): Название категории
            description (str): Описание категории
            products (list): Список товаров в категории

        Примечание:
            При инициализации автоматически увеличивает счетчики:
            - product_count на количество товаров в категории
            - category_count на 1
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем общее количество товаров
        Category.product_count += len(self.products)
        # Увеличиваем счетчик категорий
        Category.category_count += 1


class Product:
    """Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (int): Цена товара
        quantity (int): Количество товара в наличии
    """

    name: str
    description: str
    price: int
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
        self.price = price
        self.quantity = quantity
