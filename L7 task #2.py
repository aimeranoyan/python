# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from typing import Any


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def fabric_needed(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def calc_fabric_needed(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._fabric_needed = None

        self._clothes.append(self)

    def calc_fabric_needed(self):
        raise NotImplemented

    @property
    def fabric_needed(self) -> float:
        if not self._fabric_needed:
            self.calc_fabric_needed()

        return self._fabric_needed

    @property
    def measuring(self) -> Any:
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        self._measuring = measuring
        self._fabric_needed = None

    @property
    def total_fabric_needed(self):
        return f"Total amount of fabric needed: {sum([item.fabric_needed for item in self._clothes])} m²"


class Coat(Clothes):
    def calc_fabric_needed(self):
        self._fabric_needed = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.measuring

    @V.setter
    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"Coat in {self.measuring} size: {self.fabric_needed} m²"


class Suit(Clothes):
    def calc_fabric_needed(self):
        self._fabric_needed = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.measuring

    @H.setter
    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"Height {self.measuring} cm: {self.fabric_needed} m²"


if __name__ == "__main__":
    coat = Coat("Burberry coat", 3)
    print(coat)
    coat.V = 6
    print(coat)

    suit = Suit("Dior mini-skirt suit", 132)
    print(suit)
    suit.H = 194
    print(suit)

    print(coat.total_fabric_needed)
    print(suit.total_fabric_needed)