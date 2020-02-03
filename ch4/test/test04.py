

class A:
    def save(self):
        print("A saved")

class B(A):
    pass

class C(A):
    def save(self):
        print("C saved")

class D(B, C):
    pass


d = D()
d.save()