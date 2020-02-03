

class MyClass:

    def set(self, v):
        self.value = v

    def put(self):
        print(self.value)


c = MyClass()
c.set('egg')
c.put()


