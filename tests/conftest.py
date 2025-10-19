import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_one() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_one(product_one: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций " "для удобства жизни",
        [product_one],
    )
