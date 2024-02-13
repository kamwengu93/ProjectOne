class Person:
    def __init__(self,first_name,age,gender):
        self.first_name = first_name
        self.age = age
        self.gender = gender


    def details(self):
            print(self.first_name,"is studying")

teacher = Person("John",30,"male")
accountant = Person("Mary", 56, "female")
doctor = Person("Joe", 35, "male")

print(teacher.first_name,teacher.age,teacher.gender)
print(accountant.first_name,accountant.age,accountant.gender)
print(doctor.first_name,doctor.age,doctor.gender)

teacher.details()