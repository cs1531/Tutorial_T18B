from abc import abstractmethod, ABC

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


class Traveller():

    def __init__(self, vehicle):
        pass

    def start_journey(self, vehicle):
        vehicle.move()

class Car(Vehicle):

    def __init__(self):
        pass

    def move(self):
        print('car is moving')

t = Traveller()
t.start_journey(Car())
