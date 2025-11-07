from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс-родитель для классов продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass
