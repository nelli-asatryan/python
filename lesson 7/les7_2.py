from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def costs(self):
        pass


class Coat(Wear):
    def __init__(self, param):
        super().__init__(param)

    @property
    def costs(self):
        return self.param / 6.5 + 0.5

    def __str__(self):
        return f"Расход на производство этого пальто: {self.costs} ед "


class Costume(Wear):
    def __init__(self, param):
        super().__init__(param)

    @property
    def costs(self):
        return 2 * self.param + 0.3


coat1 = Coat(6.5)
print(coat1)
costume1 = Costume(6.5)
print(f"Расход на производство: {costume1.costs} ед")