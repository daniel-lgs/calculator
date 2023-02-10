from art import logo
from replit import clear

print(logo)


def add(n1, n2):
    return n1 + n2

    
def subtract(n1, n2):
    return n1 - n2

    
def multiply(n1, n2):
    return n1 * n2

    
def divide(n1, n2):
    return n1 / n2
    
    
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

reset_op = True

while True:
    if reset_op:
        num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    operator = input("Choose the operator: ")
    num2 = float(input("What is the second number? "))
    
    if operator == "+" or operator == "-" or operator == "*" or operator == "/": 
        operation_function = operations[operator]
        result = operation_function(num1, num2)

        print("------------------------------------------")
        print(f"{num1} {operator} {num2} = {result}")
        print("------------------------------------------")

        if input("Type 'y' to continue with the same number or any key to reset: ") == "y":
            reset_op = False
            num1 = result
        else:
            reset_op = True
            clear()
            
