from src.product import Product


class Category:
    """Класс для представления категории товаров в магазине.

    Атрибуты:
        product_count (int): Общее количество товаров во всех категориях (статический)
        category_count (int): Общее количество категорий (статический)
        name (str): Название категории
        description (str): Описание категории
        products (property): Свойство для получения форматированного списка товаров

    Методы:
        __init__: Инициализирует категорию и обновляет счетчики
        add_product: Добавляет новый товар в категорию
    """

    product_count: int = 0
    category_count: int = 0

    name: str
    description: str
    __products: list  # Приватный атрибут для хранения списка товаров

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
            - Список товаров хранится в приватном атрибуте __products
        """
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем общее количество товаров
        Category.product_count += len(self.__products)
        # Увеличиваем счетчик категорий
        Category.category_count += 1

    def __str__(self):
        """Возвращает строку с информацией об остатках товаров категории.

        Returns:
            str: Строка в формате "Название, количество продуктов: X шт."
                 где X - суммарное количество всех товаров категории

        Пример:
            print(category) -> "Электроника, количество продуктов: 15 шт."
        """
        sum_quantity = 0  # Счетчик общего количества товаров

        # Суммируем количество каждого товара в категории
        for product in self.__products:
            sum_quantity += product.quantity

        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    def add_product(self, product: str):
        """Добавляет новый товар в категорию и обновляет общий счетчик товаров.

        Args:
            product (str): Товар для добавления в категорию

        Примечание:
            После добавления товара увеличивает статический счетчик product_count на 1
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        else:
            self.__products.append(product)

        # Увеличиваем общий счетчик товаров
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает форматированное строковое представление списка товаров.

        Returns:
            str: Строка с информацией о всех товарах категории в формате:
                 "Название, цена руб. Остаток: количество шт."
                 Каждый товар на новой строке
        """
        attribute = self.__products

        products_str: str = ""
        # Формируем строку с информацией о каждом товаре
        for product in attribute:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return products_str

    def middle_price(self):
        """Возвращает среднее значение всех товаров в категории"""
        try:
            sum_products = 0
            for product in self.__products:
                sum_products += product.price

            return sum_products / len(self.__products)

        except ZeroDivisionError:
            return 0
