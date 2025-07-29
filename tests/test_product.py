import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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


def test_print_products_info(samsung_product, iphone_product, capsys):
    """Тестирует вывод информации о продукте"""

    print(str(samsung_product))
    print(str(iphone_product), end="")

    captured = capsys.readouterr()
    captured_out = captured.out.split("\n")

    product_1 = captured_out[0]
    product_2 = captured_out[1]

    assert product_1 == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product_2 == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_sum_products(samsung_product, iphone_product, capsys):
    """Тестирует вывод суммы товаров"""
    print(samsung_product + iphone_product, end="")

    captured = capsys.readouterr()

    expected_result = samsung_product.price * samsung_product.quantity + iphone_product.price * iphone_product.quantity

    assert captured.out == str(expected_result)


def test_other_is_not_product_object(samsung_product):
    """Тестирует кейс, когда 2-ой аргумент для суммы не экземпляр класса Product"""
    with pytest.raises(TypeError) as exc_info:
        print(samsung_product + 25000)
    assert str(exc_info.value) == "Можно суммировать только объекты класса Product или его наследников"


def test_init_smartphone_class(smartphone_product):
    """ Тестирует создание товара Смартфон """
    assert smartphone_product.name == 'Samsung Galaxy S23 Ultra'
    assert smartphone_product.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone_product.price == 180000.0
    assert smartphone_product.quantity == 5
    assert smartphone_product.efficiency == 95.5
    assert smartphone_product.model == 'S23 Ultra'
    assert smartphone_product.memory == 256
    assert smartphone_product.color == 'Серый'


def test_smartphone_isinstance_product(smartphone_product):
    """ Проверяет, является ли класс Smartphone подклассом Product """
    assert isinstance(smartphone_product, Product)


def test_init_lawn_grass_class(lawn_grass_product):
    """ Тестирует создание товара Трава газонная """
    assert lawn_grass_product.name == 'Газонная трава'
    assert lawn_grass_product.description == 'Элитная трава для газона'
    assert lawn_grass_product.price == 500.0
    assert lawn_grass_product.quantity == 20
    assert lawn_grass_product.country == 'Россия'
    assert lawn_grass_product.germination_period == '7 дней'
    assert lawn_grass_product.color == 'Зеленый'
