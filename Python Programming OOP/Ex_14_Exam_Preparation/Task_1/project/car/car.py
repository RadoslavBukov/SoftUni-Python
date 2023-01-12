from abc import ABC, abstractmethod


class Car(ABC):

    MAX_SPEED = 0

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed_limit = value

    @abstractmethod
    def train(self):
        pass

