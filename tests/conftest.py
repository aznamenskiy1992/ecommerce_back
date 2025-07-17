import pytest

from src.category import Category
from src.product import Product


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


@pytest.fixture
def smartphone_category(samsung_product, iphone_product):
    """Фикстура создаёт категорию Смартфоны"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [samsung_product, iphone_product]
    )
