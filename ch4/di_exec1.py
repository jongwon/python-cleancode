from example2.cars import Car
from example2.engines import GasolineEngine, DiselEngine, ElectricEngine

if __name__ == '__main__':
    gasoline_car = Car(GasolineEngine())
    diesel_car = Car(DiselEngine())
    electric_car = Car(ElectricEngine())
    print(gasoline_car)
    print(diesel_car)
    print(electric_car)