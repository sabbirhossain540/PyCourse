
while True:
    try:
        age = int(input("Enter your age: "))
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("please rnter number with zero division")
    else:
        print("Thank you")
        break
    finally:
        print("ok, I am finally done")

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except:
#         print("Something is wrong. Please enter Number")
# print(sum(2, 1))