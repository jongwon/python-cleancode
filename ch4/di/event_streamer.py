
class EventStreamer:

    def __init__(self):
        pass


class Duck:
    def quack(self): print("꽥꽥!")
    def feathers(self): print("오리에게 흰색, 회색 깃털이 있습니다.")


class Person:
    def quack(self): print("이 사람이 오리를 흉내내네요.")
    def feathers(self): print("사람은 바닥에서 깃털을 주어서 보여 줍니다.")


def in_the_forest(duck:Duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()