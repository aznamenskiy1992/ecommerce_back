





def test_init_product(product_attributes):
    """Тестирует корректность инициализации объектов класса Product"""
    assert product_attributes.name == "Монитор MSI PRO"
    assert product_attributes.description == "Описание товара Монитор MSI PRO"
    assert product_attributes.price == 25000
    assert product_attributes.quantity == 20
