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
        self.__products = products
        # активируем подсчет атрибутов класса:категорий и продуктов
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def add_product(self, product: Product) -> None:
            """Метод экземпляра добавляет товар в категорию"""
            self.__products.append(product)
            Category.product_count += 1


    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в строке нужного формата"""
        if not self.__products:
            return "В этой категории пока нет товаров"

        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return "\n".join(products_list)
