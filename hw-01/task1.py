from abc import ABC, abstractmethod
from typing import Type
import logging

logger = logging.getLogger("VehicleLogger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def region_spec(self) -> str:
        pass

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self.region_spec()})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self.region_spec()})")


class USVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "US Spec"


class EUVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "EU Spec"


class JPVehicleFactory(VehicleFactory):
    def region_spec(self) -> str:
        return "JP Spec"


if __name__ == "__main__":
    eu_factory: Type[VehicleFactory] = EUVehicleFactory

    vehicle1: Vehicle = eu_factory().create_car("Ford", "Puma")
    vehicle1.start_engine()

    us_factory: Type[VehicleFactory] = USVehicleFactory
    vehicle2: Vehicle = us_factory().create_car("Tesla", "Model 3")
    vehicle2.start_engine()

    vehicle3: Vehicle = us_factory().create_motorcycle("Harley-Davidson", "Sportster")
    vehicle3.start_engine()

    jp_factory: Type[VehicleFactory] = JPVehicleFactory
    vehicle4: Vehicle = jp_factory().create_car("Toyota", "Corolla")
    vehicle4.start_engine()
