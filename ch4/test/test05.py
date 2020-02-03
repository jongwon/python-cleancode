
class Base:
    def f(self):
        self.g()
    def g(self):
        print("Base")

class Der(Base):
    def g(self):
        print("Derived")

b = Base()
a = Der()

b.f()
a.f()