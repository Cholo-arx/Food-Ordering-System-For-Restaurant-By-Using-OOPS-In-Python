from abc import ABC, abstractmethod
from food_ordering_system import FoodApp


class AbstractApp(ABC, FoodApp):

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self, email, password):
        pass
