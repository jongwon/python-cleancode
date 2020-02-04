class Person:
    @staticmethod
    def identify():
        return 0

class Man(Person):
    @staticmethod
    def identify():
        return 1

class Woman(Person):
    @staticmethod
    def identify():
        return 2

for cls in Person.__subclasses__():
    print(cls.identify())