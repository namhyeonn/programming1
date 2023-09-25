class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
class Dog(Pet):
    def bark(self, n):
        for _ in range(n):
            print('bark!')
    def human_age(self):
        return self.age * 4
class Cat(Pet):
    def meow(self, n):
        for _ in range(n):
            print('meow~')
    def human_age(self):
        return self.age * 4

if __name__ == '__main__':
    popo = Dog('popo', 10)
    popo.bark(3)
    print(popo)
    print('사람 나이로 환산:', popo.human_age())

    pipi = Cat('pipi', 5)
    pipi.meow(4)
    print(pipi)
    print('사람 나이로 환산:', pipi.human_age())
