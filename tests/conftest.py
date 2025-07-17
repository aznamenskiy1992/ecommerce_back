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
def samsung_product():
    """Фикстура создаёт продукт Samsung"""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def iphone_product():
    """Фикстура создаёт продукт Iphone"""
    return Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
