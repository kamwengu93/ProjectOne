# In built functions
number = max(34, 78, 90, 123)
print(number)

y = min(4, 67, 45, 23)
print(y)

z = pow(2,3)
print(z)

# User defined functions
def name():
    print("Mark")
name() #calling a function

def details():
    name = "Aziz"
    age = 18
    course = "MIT"
    print(name, age, course)
details()
# Parameters and Arguments
def patient(name, gender, age, marriage_status):
    print(name, gender, age, marriage_status)
patient("Lucas", "Male", 18, "single")
patient("Maria", "Female", "23", "married")


def multiply(x,y):
    print(x * y)
multiply(10,20)
multiply(30,40)
multiply(100,200)
multiply(30,267)

#create a user-defined function : Display details of five employees usibg the following parameters. Full name, Age, Position , Salary.

def employee(full_name, age, position, salary):
    print(full_name, age, position, salary)
employee("Derrick Oloo", "23", "Intern", "20000")
employee("Eric Mwangi", "25", "Sales Executive", "35000")
employee("Mary Mwangi", "38", "Marketing Assistant", "60000")
employee("Mary Njeri", "43", "Marketing Manager", "90000")
employee("Enos Mungai", "45", "Driver", "20000")

