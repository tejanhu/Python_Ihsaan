class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking ...')

    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) +' years old.')

mohamed = Person('Mohamed', 32)
mariatou = Person('Mariatou', 29)

print(mohamed.name + ' ' + str(mohamed.age))
mohamed.speak()
mohamed.walk()

print(mariatou.name + ' ' + str(mariatou.age))
mariatou.walk()
mariatou.speak()