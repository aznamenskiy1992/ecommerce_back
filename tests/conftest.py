import pytest

from main import Category


@pytest.fixture
def category_attributes():
    """Фикстура создаёт объекты класса Category"""
    return Category(
        'Электроника',
        'Описание категории электроника',
        ['Мониторы', 'Ноутбуки', 'Компьютеры']
    )
