
class Calculator:
    def addition(num1, num2):
        return num1 + num2
    
    def subtraction(num1, num2):
        return num1 - num2
    
    def multipli(num1, num2):
        return num1 * num2
    
    def divition(num1, num2):
        return num1 / num2


calc = Calculator

sign = input("What you want to do? ")
number1 = int(input("Enter your first Number: "))
number2 = int(input("Enter your second Number: "))

if sign == "+":
    print(calc.addition(number1, number2))
elif sign == "-":
    print(calc.subtraction(number1, number2))
elif sign == "*":
    print(calc.multipli(number1, number2))
elif sign == "/":
    print(calc.subtraction(number1, number2))


        


