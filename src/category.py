from src.product import Product


class Category:
    """Класс для категории продуктов"""

    # атрибуты класса для подсчета категорий и продуктов
    category_count = 0
    product_count = 0
    # атрибуты класса
    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
        # активируем подсчет атрибутов класса:категорий и продуктов
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
