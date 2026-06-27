def square (number):
    return number * number
def cube (number):
    return(number)


def calculator (a,b):
    print("1.Addititon: ")
    print("2,Subtraction: ")
    print("3.Multiplication: ")
    print("4.Division: ")
    print("5.square: ")
    print("6.cube")
    choice = input("Enter your choice: ")
    if choice == "1":
        
        print("Answer=",a+b)
    elif choice == "2":
        print("Answer=",a-b)
    elif choice == "3":
        print("Answer=",a*b)
    elif choice =="4":
        print("Answer=",a/b)
    elif choice == "5":
        print("square=",square(a))
    elif choice == "6":
        print("cube=",cube(a))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calculator(num1, num2)