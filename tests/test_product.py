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
