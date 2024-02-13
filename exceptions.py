try:
    print(x)
except:
    print("Name error occured")

try:
    num1 = 20
    num2 = 10
    print(num1 / num2)
except:
    print("Zero Division occured")
finally:
    print("Success")

#user defined function
try:
    def sum (first, second):
        return first + second
except:
    print("Exceptions occured")
finally:
    print("Success")
print(sum(10, 20))
