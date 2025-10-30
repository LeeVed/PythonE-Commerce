from typing import Any


class Product:
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
        self.quantity = quantity

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
