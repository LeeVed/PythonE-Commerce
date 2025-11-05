import pytest
from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(product_one: Product) -> None:
    """Тест по инициализации атрибутов"""
    assert product_one.name == "Samsung Galaxy S23 Ultra"
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0
    assert product_one.quantity == 5


# Тесты для класс-метода
def test_new_product_full_data() -> None:
    """Тест создания товара через класс-метод с полными данными"""

    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product_no_name() -> None:
    """Тест что класс-метод вызывает ошибку при отсутствии названия"""

    product_data = {"description": "Описание", "price": 1000.0, "quantity": 1}

    with pytest.raises(ValueError, match="Название товара является обязательным параметром"):
        Product.new_product(product_data)


# Тесты для геттера
def test_price_getter() -> None:
    """Тест геттера для получения цены"""

    product = Product("Тестовый товар", "Описание", 5000.0, 10)

    price = product.price  # Используем геттер как атрибут

    assert price == 5000.0
    assert isinstance(price, float)


# Тесты для сеттера
def test_price_setter_valid() -> None:
    """Тест сеттера с корректной ценой"""

    product = Product("Товар", "Описание", 1000.0, 1)

    product.price = 2000.0  # Используем сеттер

    assert product.price == 2000.0


def test_price_setter_negative(capsys: CaptureFixture[str]) -> None:
    """Тест сеттера с отрицательной ценой (вывод сообщения)"""

    product = Product("Товар", "Описание", 1000.0, 1)

    product.price = -500.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000.0


def test_price_setter_zero(capsys: CaptureFixture[str]) -> None:
    """Тест сеттера с нулевой ценой (вывод сообщения)"""

    product = Product("Товар", "Описание", 1000.0, 1)

    product.price = 0.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000.0


def test_product_addition() -> None:
    """Тест сложения двух товаров"""
    product1 = Product("Товар1", "Описание1", 100.0, 10)
    product2 = Product("Товар2", "Описание2", 200.0, 2)

    result = product1 + product2
    expected = 100 * 10 + 200 * 2

    assert result == expected
    assert isinstance(result, float)


def test_product_addition_with_different_types() -> None:
    """Тест проверки на несовместимость с другими типами данных"""

    product = Product("Товар", "Описание", 100.0, 5)

    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
        product + 100  # type: ignore[operator]

    with pytest.raises(TypeError):
        product + "строка"  # type: ignore[operator]


# Тесты для строкового представления
def test_product_str_representation() -> None:
    """Тест строкового представления продукта"""
    # Arrange
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Act
    result = str(product)

    # Assert
    expected = "Iphone 15, 210000 руб. Остаток: 8 шт."
    assert result == expected


def test_product_str_price_formatting() -> None:
    """Тест что цена форматируется как целое число"""

    product = Product("Тестовый", "Товар", 12345.67, 3)

    result = str(product)

    assert "12345 руб." in result
    assert "12345.67" not in result
