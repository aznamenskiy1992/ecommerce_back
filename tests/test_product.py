import pytest

from src.product import Product


def test_init_product(samsung_product, iphone_product):
    """Тестирует корректность создания нового товара"""
    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5

    assert iphone_product.name == "Iphone 15"
    assert iphone_product.description == "512GB, Gray space"
    assert iphone_product.price == 210000.0
    assert iphone_product.quantity == 8


def test_add_product_from_dict(samsung_product_in_dict):
    """Тестирует создание товара из словаря"""
    samsung_product_instance = Product.new_product(samsung_product_in_dict)

    name = samsung_product_in_dict["name"]
    description = samsung_product_in_dict["description"]
    price = samsung_product_in_dict["price"]
    quantity = samsung_product_in_dict["quantity"]

    assert samsung_product_instance.name == name
    assert samsung_product_instance.description == description
    assert samsung_product_instance.price == price
    assert samsung_product_instance.quantity == quantity


@pytest.mark.parametrize("price", [-1, 0])
def test_new_price_less_0(capsys, price, samsung_product):
    """Тестирует кейс, когда новая цена <= 0"""
    samsung_product.price = price

    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_price_more_0(capsys, samsung_product):
    """Тестирует кейс, когда новая цена > 0"""
    samsung_product.price = 25000.99

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" not in captured.out.strip()

    assert samsung_product.price == 25000.99
