from src.category import Category
from src.product import Product


def test_add_category(smartphone_category):
    """Тестирует корректность создания новой категории"""
    assert smartphone_category.name == "Смартфоны"
    assert smartphone_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(smartphone_category.products) == 2


def test_count_added_categories():
    """Тестирует подсчёт количества добавленных категорий"""
    assert Category.category_count == 1


def test_len_product_in_category():
    """Тестирует подсчёт количества продуктов в добавленных категориях"""
    assert Category.product_count == 2


def test_add_product_in_category(smartphone_category, tv_product):
    """Тестирует добавление товара в список товаров категории"""
    smartphone_category.add_product(tv_product)
    assert len(smartphone_category.products) == 3

    index_added_product = smartphone_category.products.index(tv_product)
    assert smartphone_category.products[index_added_product].name == "55\" QLED 4K"
    assert smartphone_category.products[index_added_product].description == "Фоновая подсветка"
    assert smartphone_category.products[index_added_product].price == 123000.0
    assert smartphone_category.products[index_added_product].quantity == 7


def test_increase_product_counter_after_add_product():
    """Тестирует увеличение счётчика продуктов при добавлении продукта в список продуктов категории"""
    assert Category.product_count == 5


def test_print_products_in_category(capsys, smartphone_category):
    """Тестирует вывод списка товаров из категории"""
    captured = capsys.readouterr()
    assert captured.out.strip() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт."
