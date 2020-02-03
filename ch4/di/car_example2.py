import dependency_injector.containers as containers
import dependency_injector.providers as providers


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


class Engines(containers.DeclarativeContainer):
    gasoline = providers.Factory(GasolineEngine)
    diesel = providers.Factory(DieselEngine)
    electric = providers.Factory(ElectricEngine)


class Cars(containers.DeclarativeContainer):
    gasoline = providers.Factory(Car, engine=Engines.gasoline)
    diesel = providers.Factory(Car, engine=Engines.diesel)
    electric = providers.Factory(Car, engine=Engines.electric)


gasoline_car = Car(GasolineEngine())
print(gasoline_car._engine)
print(Cars.gasoline()._engine)

