import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(lawngrass1: LawnGrass) -> None:
    """Тест на проверку инициализации"""
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"


def test_lawngrass_add_successful(lawngrass1: LawnGrass, lawngrass2: LawnGrass) -> None:
    """Тест на проверку корректного складывания объектов одного класса"""
    assert lawngrass1 + lawngrass2 == 16750.0


def test_lawngrass_add_error(lawngrass1: LawnGrass, lawngrass2: LawnGrass) -> None:
    """Тест на проверку ошибки при сложении разных типов объектов"""
    with pytest.raises(TypeError):
        result = lawngrass1 + 2  # type: ignore
