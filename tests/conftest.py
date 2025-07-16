import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_attributes():
    """Фикстура создаёт объекты класса Category"""
    electronics = Category("Электроника", "Описание категории электроника", ["Мониторы", "Ноутбуки", "Компьютеры"])
    electronics_accessories = Category(
        "Аксессуары для электроники",
        "Описание категории аксессуары для электроники",
        ["Батарейки", "Внешние аккумуляторы"],
    )
    return electronics, electronics_accessories


@pytest.fixture
def product_attributes():
    """Фикстура создаёт объекты класса Product"""
    return Product("Монитор MSI PRO", "Описание товара Монитор MSI PRO", 25000, 20)
