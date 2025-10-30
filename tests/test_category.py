from src.category import Category
from src.product import Product


def test_category_init(category_one: Category) -> None:
    assert category_one.name == "Смартфоны"
    assert category_one.description == (
        "Смартфоны, как средство не только коммуникации, но и получение " "дополнительных функций для удобства жизни"
    )

    products_output = category_one.products
    assert "Samsung Galaxy S23 Ultra" in products_output
    assert "180000" in products_output
    assert "Остаток: 5 шт." in products_output
    # Для счетчиков
    assert Category.category_count >= 1
    assert Category.product_count >= 1


def test_products_property_empty_category() -> None:
    """Тест геттера для пустой категории"""

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получение "
        "дополнительных функций для удобства жизни",
        [],
    )

    result = category.products

    assert result == "В этой категории пока нет товаров"


def test_products_property_full_category() -> None:
    """Тест геттера для категории с несколькими товарами"""

    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                        "но и получение дополнительных функций для удобства жизни",
                        [product1, product2, product3])

    result = category.products

    lines = result.split('\n')
    assert len(lines) == 3
    assert "Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт." in lines
    assert "Iphone 15, 210000 руб. Остаток: 8 шт." in lines
    assert "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт." in lines


def test_products_property_access() -> None:
    """Тест что геттер работает как property (без вызова метода)"""

    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 5)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получение "
        "дополнительных функций для удобства жизни",
        [product],
    )

    result = category.products

    assert "Samsung Galaxy C23 Ultra" in result
    assert "18000" in result


def test_products_property_after_adding() -> None:
    """Тест что геттер обновляется после добавления товара"""

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получение "
        "дополнительных функций для удобства жизни",
        [],
    )
    product = Product("Мышь", "Беспроводная", 5000.0, 15)

    category.add_product(product)
    result = category.products

    assert "Мышь" in result
    assert "5000" in result
    assert "Остаток: 15 шт." in result
