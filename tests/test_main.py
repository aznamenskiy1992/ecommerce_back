import pytest

from main import Category, Product


def test_init_category(category_attributes):
    """Тестирует корректность инициализации объектов класса Category"""
    assert category_attributes.name == 'Электроника'
    assert category_attributes.description == 'Описание категории электроника'
    assert category_attributes.products == ['Мониторы', 'Ноутбуки', 'Компьютеры']


def test_init_product(product_attributes):
    """Тестирует корректность инициализации объектов класса Product"""
    assert product_attributes.name == 'Монитор MSI PRO'
    assert product_attributes.description == 'Описание товара Монитор MSI PRO'
    assert product_attributes.price == 25000
    assert product_attributes.quantity == 20
