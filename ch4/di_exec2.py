

import example2.cars
import example2.engines

import dependency_injector.containers as containers
import dependency_injector.providers as providers

class Engines(containers.DeclarativeContainer):
    gasoline = providers.Factory(example2.engines.GasolineEngine)

class Cars(containers.DeclarativeContainer):
    gasoline = providers.Factory(example2.cars.Car, engine=Engines.gasoline)


if __name__ == '__main__':
    gasoline_car = Cars.gasoline();
