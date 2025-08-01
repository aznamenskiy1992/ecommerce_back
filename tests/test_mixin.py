from src.product import Smartphone


def test_print_object_info(capsys):
    """Тестирует вывод в консоль информации о созданном объекте"""
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    captured = capsys.readouterr()

    name = "Samsung Galaxy S23 Ultra"
    description = "256GB, Серый цвет, 200MP камера"
    price = 180000.0
    quantity = 5

    assert captured.out.strip() == f"Smartphone ({name}, {description}, {price}, {quantity})"
