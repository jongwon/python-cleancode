

class Base:
    def f(self):
        print("base")

    def __add__(self, other):
        print("add %s" % other)

class Deer(Base):
    pass



b = Deer()
b.f()
b + 3