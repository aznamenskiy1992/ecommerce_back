import pytest

from main import Category


def test_init_category(category_attributes):
    """Тестирует корректность инициализации объектов класса Category"""
    assert category_attributes.name == 'Электроника'
    assert category_attributes.description == 'Описание категории электроника'
    assert category_attributes.products == ['Мониторы', 'Ноутбуки', 'Компьютеры']
