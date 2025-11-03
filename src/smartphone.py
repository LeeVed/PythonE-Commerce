from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Product) -> float:
        """
        Магический метод для сложения одного типа продуктов(подкласса)

        """
        if type(other) is not type(self):
            raise TypeError("Можно складывать только объекты класса Smartphone")

        # Используем родительскую логику для расчета стоимости
        return super().__add__(other)
