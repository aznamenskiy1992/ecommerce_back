from src.category import Category


def test_init_category(electronic_category, electronics_accessories_category):
    """Тестирует корректность инициализации объектов класса Category"""
    assert electronic_category.name == "Электроника"
    assert electronic_category.description == "Описание категории электроника"
    assert electronic_category.products == ["Мониторы", "Ноутбуки", "Компьютеры"]

    assert electronics_accessories_category.name == "Аксессуары для электроники"
    assert electronics_accessories_category.description == "Описание категории аксессуары для электроники"
    assert electronics_accessories_category.products == ["Батарейки", "Внешние аккумуляторы"]


def test_len_product_in_category():
    """Тестирует подсчёт количества продуктов в добавленных категориях"""
    assert Category.product_count == 5


def test_count_added_categories():
    """Тестирует подсчёт количества добавленных категорий"""
    assert Category.category_count == 2
