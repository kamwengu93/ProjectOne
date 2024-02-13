# Data Type

number = 67  # int
num = 78.98  # float
greeting = "Hello there!"  # str
isPythonInteresting = True  # bool

# a variable storing multiple values
languages = ["Python", "PHP", "Java"]  # list
fruits = ("banana", "apple", "pineapple")  # tuple
countries = {"Kenya", "China", "North America"}  # set
# Dictionary
details = {"firstname": "Brian",
           "age": 18,
           "course": "MIT",
           "nationality": "Kenyan"}

print(number)
print(isPythonInteresting)
print(countries)
print(fruits)
print(details)
print(details["course"])
print(details["nationality"])

# determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# typecasting - converting one data type to another

print(float(number))
print(int(num))

