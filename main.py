from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self):
        self.position = 0


class MoveBehavior(ABC):

    @abstractmethod
    def move(self, unit: Unit):
        ...


class Duck(Unit):

    def __init__(self, strategy):
        super().__init__()
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def move(self):
        self._strategy.move(self)


class FlyStrategy(MoveBehavior):

    def move(self, unit: Unit):
        unit.position += 10


class SwimStrategy(MoveBehavior):

    def move(self, unit: Unit):
        unit.position += 1


if __name__ == "__main__":
    fly_strategy = FlyStrategy()
    swim_strategy = SwimStrategy()
    duck = Duck(swim_strategy)
    duck.move()
    duck.move()
    duck.move()
    print(duck.position)
    duck.strategy = fly_strategy
    duck.move()
    duck.move()
    print(duck.position)
