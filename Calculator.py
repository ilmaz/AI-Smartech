add = lambda a, b: a + b
sub = lambda a, b: a - b
div = lambda a, b: a / b
mul = lambda a, b: a * b

message = """
*****************************

The result is {}

*****************************
"""

while True:
    print("Choose a command!\nA)Add\nB)Subtract\nC)Divide\nD)Multiply")
    command = input("Enter=> A|B|C|D\n")
    if command.lower() in ("a", "b", "c", "d"):
        numberOne = int(input("Enter the number one: "))
        numberTwo = int(input("Enter the number two: "))
        command = command.lower()
        if command == "a":
            print(message.format(add(numberOne, numberTwo)))
        elif command == "b":
            print(message.format(sub(numberOne, numberTwo)))
        elif command == "c":
            print(message.format(div(numberOne, numberTwo)))
        elif command == "d":
            print(message.format(mul(numberOne, numberTwo)))
    else:
        print("Invalid command!!!")
