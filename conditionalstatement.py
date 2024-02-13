temperature = 34
if temperature > 25 :
    print("It is hot")
else:
    print("It is cold")

# a program that determines the largest number among three numbers
num1 = 78
num2 = 100
num3 = 30

if num1 > num2 and num1 >num3:
    print(num1,"is the largest number")
elif num2 > num1 and num2 > num3:
        print(num2, "is the largest number")
else: print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 43
if number % 2 == 0:
    print(number, "is an even number")
else: print(number, "is an odd number")


#A program that checks whether a number is prime or not

num = 9

# If number is greater than 1
if num > 1:
    # Check if factor exist
    for x in range(2, num):
        if (num % x) == 0:
            print(num, "is not a prime number")
            break 
    else:
        print(num, "is a prime number")

# Else if the input number is less than or equal to 1
else:
    print(num, "is not a prime number")