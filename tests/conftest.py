import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def electronic_category():
    """Фикстура создаёт категорию электроника"""
    return Category("Электроника", "Описание категории электроника", ["Мониторы", "Ноутбуки", "Компьютеры"])


@pytest.fixture
def electronics_accessories_category():
    """Фикстура создаёт категорию аксессуары для электроники"""
    return Category(
        "Аксессуары для электроники",
        "Описание категории аксессуары для электроники",
        ["Батарейки", "Внешние аккумуляторы"],
    )


@pytest.fixture
def product_attributes():
    """Фикстура создаёт объекты класса Product"""
    return Product("Монитор MSI PRO", "Описание товара Монитор MSI PRO", 25000, 20)
