# number checker

valid = False
while not valid:

    error = "Please enter a number that is more than zero"

    try:
        width = float(input("Width: "))

        if width <= 0:
            print(error)
        else:
            print(width)
            valid = True

    except ValueError:
        print(error)

valid = False
while not valid:

    error = "Please enter a number that is more than zero"

    try:
        width = float(input("Height: "))

        if width <= 0:
            print(error)
        else:
            print(width)
            valid = True

    except ValueError:
        print(error)

