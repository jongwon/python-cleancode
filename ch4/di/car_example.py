
class Engine:
    pass


class GasolineEngine(Engine):
    pass


class DieselEngine(Engine):
    pass


class ElectricEngine(Engine):
    pass


class Car:
    def __init__(self, engine):
        self._engine = engine


gasoline_car = Car(GasolineEngine())
print(gasoline_car._engine)

