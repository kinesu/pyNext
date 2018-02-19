class Animal():
    _is_alive = True

    def __init__(self, name):
        self.name = name

    def func(self):
        return 'test'

    def kill(self):
        self._is_alive = False

    def is_dead(self):
        if self._is_alive:
            print(self.name, 'is ok')

        else:
            print(self.name, 'is dead')

class Mutant(Animal):
    def func(self):
        response = super().func()
        response += 'aaaa'

        return response

    def is_dead(self):
        print(self.name, 'is ok')

    def kill(self):
        pass

dog = Animal(name = "Ringo")  #tworzymy instancje klasy Animal
dog.is_dead()
dog.kill()
dog.is_dead()

cat = Animal(name = "Mruczek")
cat.is_dead()
cat.kill()
cat.is_dead()


mutant = Mutant(name="Hulk")
mutant.is_dead()
mutant.kill()
mutant.is_dead()