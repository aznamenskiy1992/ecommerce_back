from src.category import Category


def test_init_category(category_attributes):
    """
    Тестирует:
        1. Корректность инициализации объектов класса Category;
        2. Подсчёт количества продуктов в добавленных категориях;
        3. Подсчёт количества добавленных категорий
    """
    assert category_attributes[0].name == "Электроника"
    assert category_attributes[0].description == "Описание категории электроника"
    assert category_attributes[0].products == ["Мониторы", "Ноутбуки", "Компьютеры"]

    assert category_attributes[1].name == "Аксессуары для электроники"
    assert category_attributes[1].description == "Описание категории аксессуары для электроники"
    assert category_attributes[1].products == ["Батарейки", "Внешние аккумуляторы"]

    assert Category.product_count == len(category_attributes[0].products) + len(category_attributes[1].products)
    assert Category.category_count == 2
