import pytest

from main import Category, Product


@pytest.fixture
def category_attributes():
    """Фикстура создаёт объекты класса Category"""
    return Category(
        'Электроника',
        'Описание категории электроника',
        ['Мониторы', 'Ноутбуки', 'Компьютеры']
    )


@pytest.fixture
def product_attributes():
    """Фикстура создаёт объекты класса Product"""
    return Product(
        'Монитор MSI PRO',
        'Описание товара Монитор MSI PRO',
        25000,
        20
    )
