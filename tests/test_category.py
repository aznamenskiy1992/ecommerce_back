from src.category import Category
from src.product import Product


def test_add_category(smartphone_category):
    """Тестирует корректность создания новой категории"""
    assert smartphone_category.name == "Смартфоны"
    assert smartphone_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(smartphone_category.products) == 2


def test_add_product_in_category(smartphone_category, tv_product):
    """Тестирует добавление товара в список товаров категории"""
    smartphone_category.add_product(tv_product)
    assert len(smartphone_category.products) == 3

    index_added_product = smartphone_category.products.index(tv_product)
    assert smartphone_category.products[index_added_product].name == "55\" QLED 4K"
    assert smartphone_category.products[index_added_product].description == "Фоновая подсветка"
    assert smartphone_category.products[index_added_product].price == 123000.0
    assert smartphone_category.products[index_added_product].quantity == 7


# def test_init_category(electronic_category, electronics_accessories_category):
#     """Тестирует корректность инициализации объектов класса Category"""
#     assert electronic_category.name == "Электроника"
#     assert electronic_category.description == "Описание категории электроника"
#     assert electronic_category.products == ["Мониторы", "Ноутбуки", "Компьютеры"]
#
#     assert electronics_accessories_category.name == "Аксессуары для электроники"
#     assert electronics_accessories_category.description == "Описание категории аксессуары для электроники"
#     assert electronics_accessories_category.products == ["Батарейки", "Внешние аккумуляторы"]
#
#
# def test_len_product_in_category():
#     """Тестирует подсчёт количества продуктов в добавленных категориях"""
#     assert Category.product_count == 5
#
#
# def test_count_added_categories():
#     """Тестирует подсчёт количества добавленных категорий"""
#     assert Category.category_count == 2
#
#

#
#
# def test_len_product_in_category_after_add_product():
#     """Тестирует подсчёт количества продуктов в добавленных категориях после добавления товара в категорию"""
#     assert Category.product_count == 9
