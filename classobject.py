# a class is a blueprint of an object
# an object is an instance of a class

class Person:
    # Properties/Attributes/Characteristics/Variables
    name = "Joe"
    age = 24

    # This is a method/function/behaviour

    def talk (self):
        print("Person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)
