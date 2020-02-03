class Engine:
    """
    자동차 엔진 클래스
    """

class GasolineEngine(Engine):
    """
    가솔린 엔진
    """
    def __init__(self):
        print("GasolineEngine created")

class DiselEngine(Engine):
    """
    디젤 엔진
    """
    def __init__(self):
        print("DiselEngine created")

class ElectricEngine(Engine):
    """
    전기차 엔진
    """
    def __init__(self):
        print("ElectricEngine created")