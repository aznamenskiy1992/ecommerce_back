def test_add_category(smartphone_category):
    """Тестирует корректность создания новой категории"""
    assert smartphone_category.name == "Смартфоны"
    assert smartphone_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"


def test_add_product_in_category(smartphone_category, tv_product):
    """Тестирует добавление товара в список товаров категории"""
    smartphone_category.add_product(tv_product)

    assert smartphone_category.products.strip() == f"Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n55\" QLED 4K, 123000.0 руб. Остаток: 7 шт."


def test_print_products_in_category(smartphone_category):
    """Тестирует возврат списка товаров из категории"""
    assert smartphone_category.products.strip() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт."
