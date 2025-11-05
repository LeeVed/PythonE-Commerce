from src.base_product import BaseProduct
from src.product import Product


def test_base_product_parenting() -> None:
    """Тест, что класс Product наследует от BaseProduct"""

    assert issubclass(Product, BaseProduct)
