import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


# Використання початковий код
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

# Фабрика для США
us_vehicle_factory = USVehicleFactory()
us_car = us_vehicle_factory.create_car("Ford", "Mustang")
us_motorcycle = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")

#  Фабрика для ЄС
eu_vehicle_factory = EUVehicleFactory()
eu_car = eu_vehicle_factory.create_car("Fiat", "500")
eu_motorcycle = eu_vehicle_factory.create_motorcycle("Vespa", "111111")

# Використання нових моделей
us_car.start_engine()
us_motorcycle.start_engine()

eu_car.start_engine()
eu_motorcycle.start_engine()
