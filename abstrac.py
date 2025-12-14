from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print("BMW Started")

b = BMW()
b.start()
