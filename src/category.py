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
        self.__products = products

        # Обновляем общее количество товаров
        Category.product_count += len(self.products)
        # Увеличиваем счетчик категорий
        Category.category_count += 1


    def add_product(self, product: str):
        """Добавляет продукт в категорию"""
        self.__products.append(product)

        Category.product_count += 1


    @property
    def products(self):
        """Возвращает список товаров в категории"""
        attribute = self.__products

        products_str: str = ""
        for i in range(len(attribute)):
            products_str += f"{attribute[i].name}, {attribute[i].price} руб. Остаток: {attribute[i].quantity} шт.\n"

        print(products_str)

        return attribute
