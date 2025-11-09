from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для описания продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        """Строковое представление в следующем виде: Название продукта, 80 руб. Остаток: 15 шт."""

        return f"{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод для сложения продуктов.
        Возвращает общую стоимость всех товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")

            # Общая стоимость = (цена × количество) + (цена × количество)
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> Any:
        """Класс-метод принимает параметры товара в словаре и возвращает созданный объект класса"""
        name = product_data.get("name")
        description = product_data.get("description", "")
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        if not name:
            raise ValueError("Название товара является обязательным параметром")

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установки цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            # Новую цену не устанавливаем, оставляем старую
        else:
            self.__price = new_price
