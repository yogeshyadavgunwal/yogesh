
def addition(first_numbe, second_numbe):
    return ((first_numbe) + (second_numbe))


def substraction(first_numbe, second_numbe):
    return ((first_numbe) - (second_numbe))


def multiplication(first_numbe, second_numbe):
    return ((first_numbe) * (second_numbe))


def divison(first_numbe, second_numbe):
    return ((first_numbe) / (second_numbe))


first_number = int(input("first number="))
second_number = int(input("second number="))
operation = input(
    "Out of + , - ,*, /  operations \n which operation do you want to perform ")
if operation =='+':
    print(addition(first_number, second_number))

elif operation == '-'  :
    print(substraction(first_number, second_number))

elif operation == '*':
    print(multiplication(first_number, second_number))

elif operation == '/':
    print(divison(first_number, second_number))

else:
    print("please input correct input")
