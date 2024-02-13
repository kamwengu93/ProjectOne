# This is the Parent class/super class/bass class
class Animal:
    def sound(self):
        print("Animal is Speaking")

# child class/sub class/derived class
class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

a = Animal()
d = Dog()
d.sound()
c = Cat()

